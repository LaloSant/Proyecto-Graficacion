from OpenGL.GL import *		# type: ignore
from OpenGL.GLUT import *	# type: ignore
from OpenGL.GLU import *	# type: ignore

from .objeto import Objeto	# type: ignore

class Disco (Objeto):
	def __init__(self, radio, color):
		self.radio = radio
		self.color = color

	def draw(self):
		glPushMatrix()
		glRotatef(90, 1, 0, 0)
		self.draw_dona()
		glPopMatrix()
	
	def draw_dona(self):
		glPushMatrix()
		self.set_material_properties(self.rgb(self.color[0], self.color[1], self.color[2]))
		glutSolidTorus(2, self.radio, 10, 10)
		glPopMatrix()
