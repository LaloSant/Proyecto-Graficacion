from OpenGL.GL import * 	# type: ignore
from OpenGL.GLU import *	# type: ignore
from OpenGL.GLUT import *	# type: ignore
import math
from .objeto import Objeto

class Kenny(Objeto):
	def draw_hat(self): 
		glPushMatrix()
		glTranslatef(0.45, 1.2, 0)
		glScalef(1.25, 0.4, 1.1) 
		# glColor3f(1, 0, 0)
		self.set_material_properties(self.rgb(255, 0, 0))
		glutSolidCube(1.0)
		glPopMatrix()

		glPushMatrix()
		glTranslatef(0.45, 1, 0.5)
		glScalef(1.25, 0.05, 1) 
		# glColor3f(1, 0, 0)
		self.set_material_properties(self.rgb(255, 0, 0))
		glutSolidCube(1.0)
		glPopMatrix()

	def draw_head(self):
		glPushMatrix()
		glTranslatef(0.45, 0.65, 0)
		# glColor3f(1.01185, 0.8735, 0.7984)
		self.set_material_properties(self.rgb(255, 222, 201))
		glutSolidCube(1.0)
		glPopMatrix()


	def draw_eyes(self):
		glPushMatrix()
		glTranslatef(0.45, 0.65, 0)

		eye_x_offset = 0.15
		eye_y_offset = 0.0 
		eye_z_pos = 0.5 + 0.025

		active = False
		scale_factor = 3.0 if active else 1.0
		sx = 0.05 * scale_factor
		sy = 0.25 * scale_factor
		sz = 0.05 * scale_factor

		# glColor3f(0.0, 0.0, 0.0)
		self.set_material_properties(self.rgb(0, 0, 0))
		# Ojo izquierdo
		glPushMatrix()
		glTranslatef(-eye_x_offset, eye_y_offset, eye_z_pos)
		glScalef(sx, sy, sz)
		glutSolidCube(1.0)
		glPopMatrix()

		# Ojo derecho
		glPushMatrix()
		glTranslatef(eye_x_offset, eye_y_offset, eye_z_pos)
		glScalef(sx, sy, sz)
		glutSolidCube(1.0)
		glPopMatrix()
		glPopMatrix()

	def draw_body(self):
		glPushMatrix()
		glTranslatef(0.45, -0.56, 0)
		glScalef(1.25, 1.5, 0.75) 
		# glColor3f(0, 0, 1)
		self.set_material_properties(self.rgb(0, 0, 255))
		glutSolidCube(1.0)
		glPopMatrix()

	def draw_arms(self):
		active = False
		raise_offset = 0.55 if active else 0.0
		rotate_angle = -80 if active else 0
		rotate_angle_left = 80 if active else 0 
		side_offset = 0.5 if active else 0.0
		hand_offset = 1.15 if active else 0.0
		side_offset_hand = 1 if active else 0.0

		# Brazo derecho (originalmente a la derecha)
		# manga
		glPushMatrix()
		glTranslatef(1.2, 0, 0)
		# glColor3f(0, 0, 1.0)
		self.set_material_properties(self.rgb(0, 0, 255))
		glutSolidCube(0.25)
		glPopMatrix()
		# brazo (segmento)
		glPushMatrix()
		glTranslatef(1.2+side_offset, -0.5 + raise_offset, 0)
		if active:
			glRotatef(rotate_angle, 0, 0, 1)
		# glColor3f(1.0, 0, 0)
		self.set_material_properties(self.rgb(255, 0, 0))
		glScalef(0.25, 0.8, 0.25)
		glutSolidCube(1)
		glPopMatrix()
		# mano
		glPushMatrix()
		glTranslatef(1.2+side_offset_hand, -1 + hand_offset, 0)
		if active:
			glRotatef(rotate_angle, 0, 0, 1)
		# glColor3f(1.01185, 0.8735, 0.7984)
		self.set_material_properties(self.rgb(255, 222, 201))
		glutSolidCube(0.25)
		glPopMatrix()

		# Brazo izquierdo
		# manga
		glPushMatrix()
		glTranslatef(-0.3, 0, 0)
		# glColor3f(0, 0, 1.0)
		self.set_material_properties(self.rgb(1, 0, 255))
		glutSolidCube(0.25)
		glPopMatrix()
		# brazo
		glPushMatrix()
		glTranslatef(-0.3-side_offset, -0.5 + raise_offset, 0)
		if active:
			glRotatef(rotate_angle_left, 0, 0, 1)
		# glColor3f(1.0, 0, 0)
		self.set_material_properties(self.rgb(255, 0, 0))
		glScalef(0.25, 0.8, 0.25)
		glutSolidCube(1)
		glPopMatrix()
		# mano
		glPushMatrix()
		glTranslatef(-0.3-side_offset_hand, -1 + hand_offset, 0)
		if active:
			glRotatef(rotate_angle_left, 0, 0, 1)
		# glColor3f(1.01185, 0.8735, 0.7984)
		self.set_material_properties(self.rgb(255, 222, 201))
		glutSolidCube(0.25)
		glPopMatrix()

	def draw_legs(self):
		active = False
		spread = 0.15 if active else 0.0
		rotate_spread = 15 if active else 0

		# Pierna izquierda (prisma rectangular)
		glPushMatrix()
		glTranslatef(0 - spread, -1.59, 0)
		if active:
			glRotatef(-rotate_spread, 0, 0, 1)
		# glColor3f(1.0, 1.0, 1.0)
		self.set_material_properties(self.rgb(255, 255, 255))
		glScalef(0.3, 0.5, 0.3)
		glutSolidCube(1.0)
		glPopMatrix()

		# Pierna derecha (prisma rectangular)
		glPushMatrix()
		glTranslatef(0.9 + spread, -1.59, 0)
		if active:
			glRotatef(rotate_spread, 0, 0, 1)
		# glColor3f(1.0, 1.0, 1.0)
		self.set_material_properties(self.rgb(255, 255, 255))
		glScalef(0.3, 0.5, 0.3)
		glutSolidCube(1.0)
		glPopMatrix()

		# Pie izquierdo
		glPushMatrix()
		glTranslatef(0 - spread, -2, 0)
		glRotatef(-90, 1, 0, 0)
		if active:
			glRotatef(-rotate_spread, 0, 0, 1)
		# glColor3f(0, 0, 0)
		self.set_material_properties(self.rgb(0, 0, 0))
		glutSolidCube(0.3)
		glPopMatrix()

		# Pie derecho
		glPushMatrix()
		glTranslatef(0.9 + spread, -2, 0)
		glRotatef(-90, 1, 0, 0)
		if active:
			glRotatef(rotate_spread, 0, 0, 1)
		# glColor3f(0, 0, 0)
		self.set_material_properties(self.rgb(0, 0, 0))
		glutSolidCube(0.3)
		glPopMatrix()

	def draw(self):
		glPushMatrix()
		""" if state.reaction_type == "jump":
			y_offset = math.sin(math.pi * state.reaction_timer / state.reaction_duration) * 0.8
			glTranslatef(0, y_offset, 0)
		elif state.reaction_type == "spin":
			angle = 360 * (state.reaction_timer / state.reaction_duration)
			glRotatef(angle, 0, 1, 0)
		elif state.reaction_type == "shake":
			x_offset = math.sin(state.reaction_timer * 0.5 * math.pi) * 0.2
			glTranslatef(x_offset, 0, 0) """
		glTranslatef(-1, 0, 0)
		self.draw_body()
		self.draw_hat()
		self.draw_head()
		self.draw_eyes()
		self.draw_arms()
		self.draw_legs()
		glPopMatrix()
