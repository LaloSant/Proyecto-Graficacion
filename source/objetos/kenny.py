from OpenGL.GL import * 	# type: ignore
from OpenGL.GLU import *	# type: ignore
from OpenGL.GLUT import *	# type: ignore
import math
from source.objetos.objeto import Objeto
import utils.estado as est
import source.objetos.pers_args as pers_args

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
		# Brazo derecho (originalmente a la derecha)
		# manga
		glPushMatrix()
		# glColor3f(0, 0, 1.0)
		self.set_material_properties(self.rgb(0, 0, 255))
		glRotatef(pers_args.caminando, 1, 0, 0)
		glTranslatef(1.2, 0, 0)
		glutSolidCube(0.25)
		glPopMatrix()
		# brazo (segmento)
		glPushMatrix()
		# glColor3f(1.0, 0, 0)
		self.set_material_properties(self.rgb(255, 0, 0))
		if est.estado_pers[0] == est.estados_pers[2]:
			glRotatef(-pers_args.brazos,1,0,0) #Brazos
		else:
			glRotatef(pers_args.caminando, 1, 0, 0)
		glTranslatef(1.2, -0.5 , 0)
		glScalef(0.25, 0.8, 0.25)
		glutSolidCube(1)
		glPopMatrix()
		# mano
		glPushMatrix()
		# glColor3f(1.01185, 0.8735, 0.7984)
		self.set_material_properties(self.rgb(255, 222, 201))
		glRotatef(pers_args.caminando, 1, 0, 0)
		glTranslatef(1.2, -1 , 0)
		glutSolidCube(0.25)
		glPopMatrix()

		# Brazo izquierdo
		# manga
		glPushMatrix()
		# glColor3f(0, 0, 1.0)
		self.set_material_properties(self.rgb(1, 0, 255))
		glRotatef(-pers_args.caminando, 1, 0, 0)
		glTranslatef(-0.3, 0, 0)
		glutSolidCube(0.25)
		glPopMatrix()
		# brazo
		glPushMatrix()
		# glColor3f(1.0, 0, 0)
		self.set_material_properties(self.rgb(255, 0, 0))
		glRotatef(-pers_args.caminando, 1, 0, 0)
		glTranslatef(-0.3, -0.5, 0)
		glScalef(0.25, 0.8, 0.25)
		glutSolidCube(1)
		glPopMatrix()
		# mano
		glPushMatrix()
		# glColor3f(1.01185, 0.8735, 0.7984)
		self.set_material_properties(self.rgb(255, 222, 201))
		glRotatef(-pers_args.caminando, 1, 0, 0)
		glTranslatef(-0.3, -1, 0)
		glutSolidCube(0.25)
		glPopMatrix()

	def draw_legs(self):


		# Pierna izquierda (prisma rectangular)
		glPushMatrix()
		
		# glColor3f(1.0, 1.0, 1.0)
		self.set_material_properties(self.rgb(255, 255, 255))
		glRotatef(pers_args.caminando, 1, 0, 0)
		glTranslatef(0 , -1.59, 0)
		glScalef(0.3, 0.5, 0.3)
		glutSolidCube(1.0)
		glPopMatrix()

		# Pierna derecha (prisma rectangular)
		glPushMatrix()
		# glColor3f(1.0, 1.0, 1.0)
		self.set_material_properties(self.rgb(255, 255, 255))
		glRotatef(-pers_args.caminando, 1, 0, 0)
		glTranslatef(0.9  , -1.59, 0)
		glScalef(0.3, 0.5, 0.3)
		glutSolidCube(1.0)
		glPopMatrix()

		# Pie izquierdo
		glPushMatrix()
		# glColor3f(0, 0, 0)
		self.set_material_properties(self.rgb(0, 0, 0))
		glRotatef(pers_args.caminando, 1, 0, 0)
		glTranslatef(0  , -2, 0)
		glRotatef(-90, 1, 0, 0)
		glutSolidCube(0.3)
		glPopMatrix()

		# Pie derecho
		glPushMatrix()
		# glColor3f(0, 0, 0)
		self.set_material_properties(self.rgb(0, 0, 0))
		glRotatef(-pers_args.caminando, 1, 0, 0)
		glTranslatef(0.9, -2, 0)
		glRotatef(-90, 1, 0, 0)
		glutSolidCube(0.3)
		glPopMatrix()

	def draw(self):
		glPushMatrix()
		glScalef(0.9, 0.9, 0.9)
		""" if state.reaction_type == "jump":
			y_offset = math.sin(math.pi * state.reaction_timer / state.reaction_duration) * 0.8
			glTranslatef(0, y_offset, 0)
		elif state.reaction_type == "spin":
			angle = 360 * (state.reaction_timer / state.reaction_duration)
			glRotatef(angle, 0, 1, 0)
		elif state.reaction_type == "shake":
			x_offset = math.sin(state.reaction_timer * 0.5 * math.pi) * 0.2
			glTranslatef(x_offset, 0, 0) """
		glTranslatef(-0.5, 0, 0)
		self.draw_body()
		self.draw_hat()
		self.draw_head()
		self.draw_eyes()
		self.draw_arms()
		self.draw_legs()
		glPopMatrix()
