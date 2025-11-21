# source/objetos/kevin.py
from OpenGL.GL import *		# type: ignore
from OpenGL.GLUT import *	# type: ignore
from OpenGL.GLU import *	# type: ignore

from source.objetos.objeto import Objeto
import utils.estado as est

class Dodecaedro(Objeto):
	def __init__(self):
		super().__init__()
		self.posicion = est.objetos["Dodecaedro"][0]
		self.radius = est.objetos["Dodecaedro"][1]

	def draw(self):
		glPushMatrix()
		glTranslate(self.posicion[0], self.posicion[1], self.posicion[2])
		glRotatef(glutGet(GLUT_ELAPSED_TIME) / 40.0, 0, 1, 0)
		self.dibuja_dodecaedro()
		glPopMatrix()
	
	def dibuja_dodecaedro(self):
		glPushMatrix()
		self.set_material_properties(self.rgb(80, 97, 141))
		glScale(0.5, 0.5, 1)
		glutSolidDodecahedron()
		glPopMatrix()
