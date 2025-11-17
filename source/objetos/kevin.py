from OpenGL.GL import * 	# type: ignore
from OpenGL.GLU import *	# type: ignore
from OpenGL.GLUT import *	# type: ignore
import math

from .objeto import Objeto

class Kevin(Objeto):
	def draw_head(self):
		glPushMatrix()
		# glColor3f(198/255, 136/255, 99/255)
		self.set_material_properties(self.rgb(198, 136, 99))
		glTranslatef(0, 1.4, 0)
		glScalef(1, 1, 0.8)
		glutSolidCube(1.0)
		glPopMatrix()
		
	def draw_horns(self): 
		for dx in [-0.5, 0.5]:
			glPushMatrix()
			# glColor3f(0, 0, 0)
			self.set_material_properties(self.rgb(0, 0, 0))
			glTranslatef(dx, 1.8, 0)
			glScalef(0.25, 0.9, 0.25)
			glutSolidCube(0.5)
			glPopMatrix()

	def draw_eyes(self, grouwth=0.0):
		#ojo derecho
		glPushMatrix()
		glTranslatef(-0.3, 1.6, 0.41)
		glScalef(1 + grouwth, 1 + grouwth, 1)  
		# glColor3f(1.0, 0.0, 0.0)
		self.set_material_properties(self.rgb(1, 0, 0))
		glutSolidCube(0.1)
		glPopMatrix()
		#ojo izquierdo
		glPushMatrix()
		glTranslatef(0.3, 1.6, 0.41)
		glColor3f(1.0, 0.0, 0.0)
		glutSolidCube(0.1)
		glPopMatrix()

	def draw_mouth(self, growth=0.0):
		glPushMatrix()
		glTranslatef(0, 1.2, 0.41)
		glScalef(1 + growth, 1 + growth, 1)  
		# glColor3f(0.2, 0.2, 0.2) 
		self.set_material_properties(self.rgb(51, 51, 51))
		glScalef(0.6, 0.25, 0.1)
		glutSolidCube(1)
		glPopMatrix()

	def draw_body(self):
		glPushMatrix()
		glTranslatef(0, 0, 0)
		# glColor3f(0,0,0)
		self.set_material_properties(self.rgb(0, 0, 0))
		glScalef(1.6, 1.8, .6)
		glutSolidCube(1.0)
		glPopMatrix()

	def draw_arms(self, raise_angle=0.0):
		# Brazo izquierdo
		glPushMatrix()
		# glColor3f(198/255, 136/255, 99/255)
		self.set_material_properties(self.rgb(198, 136, 99))
		glTranslatef(-1.0, 0.9, 0)
		glRotatef(raise_angle, 1, 0, 0)
		glTranslatef(0, -0.6, 0)
		glScalef(.4, 1.2, .3)
		glutSolidCube(1.0)
		glPopMatrix()

		# Brazo derecho
		glPushMatrix()
		# glColor3f(198/255, 136/255, 99/255)
		self.set_material_properties(self.rgb(198, 136, 99))
		glTranslatef(1.0, 0.9, 0)
		glRotatef(-raise_angle, 1, 0, 0)
		glTranslatef(0, -0.6, 0)
		glScalef(.4, 1.2, .3)
		glutSolidCube(1.0)
		glPopMatrix()

	def draw_legs(self, raise_angle=0.0):
		#pierna izquieda
		glPushMatrix()
		# glColor3f(0.5, 0.5, 0.5) 
		self.set_material_properties(self.rgb(127, 127, 127))
		glTranslatef(-.5, -1.4, 0)
		glRotatef(raise_angle, 1, 0, 0)
		glTranslatef(0, -0.25, 0)
		glScalef(.5, 1.5, .5)
		glutSolidCube(1.0)
		glPopMatrix()

		#pierna derecha
		glPushMatrix()
		# glColor3f(0.5, 0.5, 0.5) 
		self.set_material_properties(self.rgb(127, 127, 127))
		glTranslatef(.5, -1.4, 0)
		glRotatef(-raise_angle, 1, 0, 0)
		glTranslatef(0, -0.25, 0)
		glScalef(.5, 1.5, .5)
		glutSolidCube(1.0)
		glPopMatrix()

	def draw(self):
		glPushMatrix()
		glTranslatef(0, 0, 0)
		arm_angle = 0.0 
		leg_angle = 0.0
		eye_growth = 0.0
		mouth_growth = 0.0
		self.draw_body()
		self.draw_head()
		self.draw_horns()
		self.draw_eyes(eye_growth)
		self.draw_mouth(mouth_growth)
		self.draw_arms(arm_angle)
		self.draw_legs(leg_angle)
		glPopMatrix()

		""" if state.collision_state and state.animation_state:
			t = state.animation_timer

			if state.animation_state == "jump":
				glTranslatef(0, abs(math.sin(t * 6)) * 1.2, 0)
				arm_angle = abs(math.sin(t * 6)) * 45 
				leg_angle = abs(math.sin(t * 6)) * 45

			elif state.animation_state == "wave":
				glRotatef(math.sin(t * 8) * 25, 1, 0, 0)
				eye_growth = 1

			elif state.animation_state == "spin":
				glRotatef((t * 360) % 360, 0, 1, 0)
				mouth_growth = 0.5

			elif state.animation_state == "fall_back":
				glRotatef(-abs(math.sin(t * 3)) * 90, 1, 0, 0)

			elif state.animation_state == "fan_spin":
				glRotatef((t * 720) % 360, 0, 0, 1) """
		
	""" 	def draw_legs(self):
		for dx in [-0.5, 0.5]:
			glPushMatrix()
			glColor3f(0.5, 0.5, 0.5) 
			glTranslatef(dx, -1.4, 0)
			glScalef(0.45, 1, 0.5)
			glutSolidCube(1.0)
			glPopMatrix() """