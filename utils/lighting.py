# utils/lighting.py
from OpenGL.GL import *	# type: ignore

class LightingManager:
	def __init__(self):
		self.current_model = 0 
		self.models = ["Phong", "Gouraud", "Flat"]

	def setup_lighting(self):
		light_position = [5.0, 5.0, 5.0, 1.0]
		light_ambient = [0.2, 0.2, 0.2, 1.0]
		light_diffuse = [1.5, 1.5, 1.5, 1.0]
		light_specular = [1.5, 1.5, 1.5, 1.0]

		glLightfv(GL_LIGHT0, GL_POSITION, light_position)
		glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
		glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
		glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)

	def apply_lighting(self):
		if self.current_model == 0:  # Phong
			glShadeModel(GL_SMOOTH)
			
			glEnable(GL_NORMALIZE)
			glEnable(GL_LIGHTING)
		elif self.current_model == 1:  # Gouraud
			glShadeModel(GL_SMOOTH)
			
			glEnable(GL_LIGHTING)
		else:  # Flat
			glShadeModel(GL_FLAT)
			glEnable(GL_LIGHTING)

	def cycle_lighting_model(self):
		self.current_model = (self.current_model + 1) % 3
		print(f"Modelo: {self.models[self.current_model]} ")