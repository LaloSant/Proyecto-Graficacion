from OpenGL.GL import *		# type: ignore
from OpenGL.GLUT import *	# type: ignore
from OpenGL.GLU import *	# type: ignore

from source.objetos.objeto import Objeto	# type: ignore
import utils.estado as est
import source.objetos.pers_args as pers_args

class DonCorru (Objeto):
	def __init__(self):
		self.posicion = est.objetos["don_corru"][0]
		self.radius = est.objetos["don_corru"][1]

	def draw(self):
		glPushMatrix()
		glTranslate(self.posicion[0], self.posicion[1], self.posicion[2])
		glRotatef(-90, 0, 1, 0)
		self.dibuja_torso()
		self.dibuja_cabeza()
		self.dibuja_piernas()
		self.dibuja_brazos()
		self.dibuja_sombrero()
		glPopMatrix()

	def dibuja_torso(self):
		glPushMatrix()
		self.set_material_properties(self.rgb(181, 23, 35))
		glScalef(0.42, 1.13, 1)
		glTranslate(0, 0, 0)
		glutSolidCube(1)
		glPopMatrix()

	def dibuja_cabeza(self):
		glPushMatrix()
		self.set_material_properties(self.rgb(176, 149, 116))
		glScalef(0.5, 0.5, 0.46)
		glTranslate(0, 1.6, 0)
		glutSolidCube(1)
		self.dibuja_cara()
		glPopMatrix()

	def dibuja_cara(self):
		glPushMatrix()	#OJOS
		self.set_material_properties(self.rgb(0, 0, 0))
		glScalef(0.2, 0.2, 0.15)
		glTranslate(2.3, 0.8, -1.8)
		glutSolidCube(1)
		glPopMatrix()
		glPushMatrix()
		self.set_material_properties(self.rgb(0, 0, 0))
		glScalef(0.2, 0.2, 0.15)
		glTranslate(2.3, 0.8, 1.8)
		glutSolidCube(1)
		glPopMatrix()

		glPushMatrix()	#BOCA
		self.set_material_properties(self.rgb(255, 255, 255))
		rotacion = 10 if est.estado_don_corru[0] == est.estados_don_corru[0] else -10
		glRotatef(rotacion, 1, 0, 0)
		glScalef(0.2, 0.15, 0.8)
		glTranslate(2.3, -1.2, 0)
		glutSolidCube(1)
		glPopMatrix()

	def dibuja_piernas(self):
		glPushMatrix()
		self.set_material_properties(self.rgb(23, 23, 23))
		glRotatef(pers_args.caminando, 0, 0, 1)
		glScalef(0.2, 0.66, 0.23)
		glTranslate(0, -1.2, 1)
		glutSolidCube(1)
		glPopMatrix()
		glPushMatrix()
		glRotatef(-pers_args.caminando, 0, 0, 1)
		glScalef(0.2, 0.66, 0.23)
		glTranslate(0, -1.2, -1)
		glutSolidCube(1)
		glPopMatrix()

	def dibuja_brazos(self):
		glPushMatrix()
		glTranslatef(0, 1, 0)
		glPushMatrix()
		self.set_material_properties(self.rgb(176, 149, 116))
		glRotatef(-pers_args.caminando, 0, 0, 1)
		glScalef(0.2, 0.66, 0.23)
		glTranslate(0, -1.4, 2.7)
		glutSolidCube(1)
		glPopMatrix()
		glPushMatrix()
		self.set_material_properties(self.rgb(176, 149, 116))
		glRotatef(pers_args.caminando, 0, 0, 1)
		glScalef(0.2, 0.66, 0.23)
		glTranslate(0, -1.4, -2.7)
		glutSolidCube(1)
		glPopMatrix()
		glPopMatrix()

	def dibuja_sombrero(self):
		glPushMatrix()
		self.set_material_properties(self.rgb(75, 44, 15))
		glScalef(0.98, 0.15, 0.98)
		glTranslate(0, 7.5, 0)
		glutSolidCube(1)
		glPopMatrix()
		glPushMatrix()
		self.set_material_properties(self.rgb(75, 44, 15))
		glScalef(0.46, 0.26, 0.46)
		glTranslate(0, 5, 0)
		glutSolidCube(1)
		glPopMatrix()
