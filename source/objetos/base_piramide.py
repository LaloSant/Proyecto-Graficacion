from OpenGL.GL import *		# type: ignore
from OpenGL.GLUT import *	# type: ignore
from OpenGL.GLU import *	# type: ignore

from .objeto import Objeto	# type: ignore

class BasePiramide (Objeto):
	def __init__(self, posicion_x):
		self.posicion_x = posicion_x

	def draw(self):
		glPushMatrix()
		glTranslatef(self.posicion_x, -1.6, 0)
		self.draw_base()
		self.draw_palo()
		glPopMatrix()
	
	def draw_base(self):
		glPushMatrix()
		self.set_material_properties(self.rgb(126, 84, 48))
		glScalef(1.5, 0.25, 1.5)
		glutSolidCube(1)
		glPopMatrix()
	
	def draw_palo(self):
		glPushMatrix()
		self.set_material_properties(self.rgb(0, 0, 0))
		glScalef(0.2, 2.5, 0.2)
		glTranslate(0, 0.5, 0)
		glutSolidCube(1)
		glPopMatrix()