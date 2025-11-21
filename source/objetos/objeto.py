# source/objetos/objeto.py
from OpenGL.GL import *		# type: ignore

class Objeto:
	def __init__(self) -> None:
		self.posicion = [0, 0, 0]

	def set_material_properties(self, color):
		r, g, b = color
		ambient = [r * 0.1, g * 0.1, b * 0.1, 1.0]
		diffuse = [r * 0.9, g * 0.9, b * 0.9, 1.0]
		specular = [0.2, 0.2, 0.2, 1.0]
		shininess = [35.0]
		glMaterialfv(GL_FRONT, GL_AMBIENT, ambient)
		glMaterialfv(GL_FRONT, GL_DIFFUSE, diffuse)
		glMaterialfv(GL_FRONT, GL_SPECULAR, specular)
		glMaterialfv(GL_FRONT, GL_SHININESS, shininess)

	def rgb(self, r, g, b):
		return (r/255, g/255, b/255)