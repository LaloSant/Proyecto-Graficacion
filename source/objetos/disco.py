from OpenGL.GL import *		# type: ignore
from OpenGL.GLUT import *	# type: ignore
from OpenGL.GLU import *	# type: ignore

from .objeto import Objeto	# type: ignore

class Disco (Objeto):
	def __init__(self, tamanio, ):
		self.posicion = [-5, 0, 0]
		if tamanio == 1:
			self.radio_ext = 0.5
			self.radio_int = 0.3
			self.color = (178, 54, 18)
			self.factor_esc_y = 0.8
		elif tamanio == 2:
			self.radio_ext = 0.6
			self.radio_int = 0.4
			self.color = (78, 139, 43)
			self.factor_esc_y = 0.7
		elif tamanio == 3:
			self.radio_ext = 0.8
			self.radio_int = 0.6
			self.color = (198, 154, 30)
			self.factor_esc_y = 0.6
		else:
			self.radio_ext = 1
			self.radio_int = 0.8
			self.color = (194, 114, 34)
			self.factor_esc_y = 0.5
		self.tamanio = tamanio

	def draw(self):
		glPushMatrix()
		glTranslatef(self.posicion[0], self.posicion[1], self.posicion[2])
		glScale(1, self.factor_esc_y, 1)
		glRotatef(90, 1, 0, 0)
		self.draw_dona()
		glPopMatrix()
	
	def draw_dona(self):
		glPushMatrix()
		self.set_material_properties(self.rgb(self.color[0], self.color[1], self.color[2]))
		glutSolidTorus(self.radio_int, self.radio_ext, 20, 20)
		glPopMatrix()
