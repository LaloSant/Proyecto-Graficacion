# source/escenas/escena.py
from OpenGL.GL import * # type: ignore
import utils.estado as est
import utils.texturas as text
from source.objetos.objeto import Objeto

class Escena(Objeto):
	def __init__(self) -> None:
		self.texturas = list()
		self.texturas.append(text.load_texture("resources/imgs/piso1.jpg"))
		self.texturas.append(text.load_texture("resources/imgs/pared1.jpg"))
		self.texturas.append(text.load_texture("resources/imgs/techo1.jpg"))
		self.texturas.append(text.load_texture("resources/imgs/piso2.jpg"))
		self.texturas.append(text.load_texture("resources/imgs/pared2.jpg"))
		self.texturas.append(text.load_texture("resources/imgs/techo2.jpg"))
		self.texturas.append(text.load_texture("resources/imgs/piso3.jpg"))
		self.texturas.append(text.load_texture("resources/imgs/pared3.jpg"))
		self.texturas.append(text.load_texture("resources/imgs/techo3.jpg"))


		est.texturas_escena["Piso"] = self.texturas[0]
		est.texturas_escena["Pared"] = self.texturas[1]
		est.texturas_escena["Techo"] = self.texturas[2]
		self.escenario = 0
	
	def set_escenario(self, num):
		if self.escenario == num:
			return
		self.escenario = num
		if num == 0:
			est.texturas_escena["Piso"] = self.texturas[0]
			est.texturas_escena["Pared"] = self.texturas[1]
			est.texturas_escena["Techo"] = self.texturas[2]
		elif num == 1:
			est.texturas_escena["Piso"] = self.texturas[3]
			est.texturas_escena["Pared"] = self.texturas[4]
			est.texturas_escena["Techo"] = self.texturas[5]
		elif num == 2:
			est.texturas_escena["Piso"] = self.texturas[6]
			est.texturas_escena["Pared"] = self.texturas[7]
			est.texturas_escena["Techo"] = self.texturas[8]

	def draw_room(self, nivel):
		self.set_escenario(nivel)
		glEnable(GL_TEXTURE_2D)
		self.set_material_properties(self.rgb(255, 255, 255))

		bounds = est.scene_bounds
		x_min, x_max = bounds["x"]
		y_min, y_max = bounds["y"]
		z_min, z_max = bounds["z"]

		# Floor
		glPushMatrix()
		glBindTexture(GL_TEXTURE_2D, est.texturas_escena["Piso"])
		glBegin(GL_QUADS)
		glNormal3f(0, 1, 0) 
		glTexCoord2f(0, 0); glVertex3f(x_min, y_min, z_min)
		glTexCoord2f(1, 0); glVertex3f(x_max, y_min, z_min)
		glTexCoord2f(1, 1); glVertex3f(x_max, y_min, z_max)
		glTexCoord2f(0, 1); glVertex3f(x_min, y_min, z_max)
		glEnd()
		glPopMatrix()

		# Ceiling
		glBindTexture(GL_TEXTURE_2D, est.texturas_escena["Techo"])
		glBegin(GL_QUADS)
		glNormal3f(0, -1, 0) 
		glTexCoord2f(0, 0); glVertex3f(x_min, y_max, z_max)
		glTexCoord2f(1, 0); glVertex3f(x_max, y_max, z_max)
		glTexCoord2f(1, 1); glVertex3f(x_max, y_max, z_min)
		glTexCoord2f(0, 1); glVertex3f(x_min, y_max, z_min)
		glEnd()

		# Back Wall (z_max)
		glBindTexture(GL_TEXTURE_2D, est.texturas_escena["Pared"])
		glBegin(GL_QUADS)
		glNormal3f(0, 0, -1) 
		glTexCoord2f(0, 0); glVertex3f(x_min, y_min, z_max)
		glTexCoord2f(1, 0); glVertex3f(x_max, y_min, z_max)
		glTexCoord2f(1, 1); glVertex3f(x_max, y_max, z_max)
		glTexCoord2f(0, 1); glVertex3f(x_min, y_max, z_max)
		glEnd()

		# Front Wall (z_min)
		glBegin(GL_QUADS)
		glNormal3f(0, 0, 1) 
		glTexCoord2f(0, 0); glVertex3f(x_min, y_min, z_min)
		glTexCoord2f(1, 0); glVertex3f(x_max, y_min, z_min)
		glTexCoord2f(1, 1); glVertex3f(x_max, y_max, z_min)
		glTexCoord2f(0, 1); glVertex3f(x_min, y_max, z_min)
		glEnd()

		# Left Wall (x_min)
		glBegin(GL_QUADS)
		glNormal3f(1, 0, 0) 
		glTexCoord2f(0, 0); glVertex3f(x_min, y_min, z_min)
		glTexCoord2f(1, 0); glVertex3f(x_min, y_min, z_max)
		glTexCoord2f(1, 1); glVertex3f(x_min, y_max, z_max)
		glTexCoord2f(0, 1); glVertex3f(x_min, y_max, z_min)
		glEnd()

		# Right Wall (x_max)
		glBegin(GL_QUADS)
		glNormal3f(-1, 0, 0) 
		glTexCoord2f(0, 0); glVertex3f(x_max, y_min, z_max)
		glTexCoord2f(1, 0); glVertex3f(x_max, y_min, z_min)
		glTexCoord2f(1, 1); glVertex3f(x_max, y_max, z_min)
		glTexCoord2f(0, 1); glVertex3f(x_max, y_max, z_max)
		glEnd()

		glDisable(GL_TEXTURE_2D)