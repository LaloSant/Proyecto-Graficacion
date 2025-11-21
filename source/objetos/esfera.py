# source/objetos/esfera.py
from OpenGL.GL import *		# type: ignore
from OpenGL.GLUT import *	# type: ignore
from OpenGL.GLU import *	# type: ignore

from source.objetos.objeto import Objeto
import utils.estado as est

class Esfera(Objeto):
	def __init__(self, slices=25, stacks=25, name="Esfera"):
		super().__init__()
		self.name = name
		self.posicion = est.objetos[self.name][0]
		self.radius = est.objetos[self.name][1]
		self.slices = slices
		self.stacks = stacks

	def draw(self):
		glPushMatrix()
		glTranslate(self.posicion[0], self.posicion[1], self.posicion[2])
		glRotatef(glutGet(GLUT_ELAPSED_TIME) / 40.0, 0, 1, 0)
		self.dibuja_esfera()
		glPopMatrix()
	
	def dibuja_esfera(self):
		glPushMatrix()
		self.set_material_properties(self.rgb(255, 255, 255))
		if self.name != "Esfera":
			glutWireSphere(self.radius, self.slices, self.stacks)
		else:
			glutSolidSphere(self.radius, self.slices, self.stacks)
		glPopMatrix()
