from OpenGL.GL import *		# type: ignore
from OpenGL.GLUT import *	# type: ignore
from OpenGL.GLU import *	# type: ignore

from objetos.objeto import Objeto
import utils.estado as est

class Tetera(Objeto):
	def __init__(self):
		super().__init__()
		self.posicion = est.objetos["Tetera"][0]
		self.radius = est.objetos["Tetera"][1]

	def draw(self):
		glPushMatrix()
		glTranslate(self.posicion[0], self.posicion[1], self.posicion[2])
		glRotatef(glutGet(GLUT_ELAPSED_TIME) / 400.0, 0, 1, 0)
		self.dibuja_tetera()
		glPopMatrix()
	
	def dibuja_tetera(self):
		glPushMatrix()
		self.set_material_properties(self.rgb(203, 135, 78))
		glScale(1, 1, 1)
		glutSolidTeapot(1)
		glPopMatrix()
