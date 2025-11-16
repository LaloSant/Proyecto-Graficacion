from OpenGL.GL import *		# type: ignore
from OpenGL.GLUT import *	# type: ignore
from OpenGL.GLU import *	# type: ignore

from objetos.objeto import Objeto
import utils.estado as est

class Torus(Objeto):
	def __init__(self):
		super().__init__()
		self.posicion = est.objetos["Torus"][0]
		self.radius = est.objetos["Torus"][1]

	def draw(self):
		glPushMatrix()
		glTranslate(self.posicion[0], self.posicion[1], self.posicion[2])
		glRotatef(glutGet(GLUT_ELAPSED_TIME) / 20.0, 0, 0, 1)
		self.dibuja_torus()
		glPopMatrix()
	
	def dibuja_torus(self):
		glPushMatrix()
		self.set_material_properties(self.rgb(80, 97, 141))
		glScale(0.5, 0.5, 1)
		glutWireTorus(1, 0.5, 10, 10)
		glPopMatrix()
