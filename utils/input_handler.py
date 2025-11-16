from OpenGL.GLUT import * # type: ignore
import utils.estado as est
import source.objetos.pers_args as pers_args

class InputHandler:
	def __init__(self, lighting_manager):
		self.lighting_manager = lighting_manager
		self.estado = est
		self.mouse_down = False
		self.last_mouse_x = 0
		self.last_mouse_y = 0
		self.keys_pressed = set()
		self.movement_speed = 0.3

	def special_keys(self, key, x, y):
		""" if key == GLUT_KEY_LEFT:
			self.estado.camera_x -= 0.2
		if key == GLUT_KEY_RIGHT:
			self.estado.camera_x += 0.2
		if key == GLUT_KEY_UP:
			self.estado.camera_y += 0.2
		if key == GLUT_KEY_DOWN:
			self.estado.camera_y -= 0.2 """
		glutPostRedisplay()
	
	def special_keys_up(self, key, x, y):
		"""Callback para cuando se suelta una tecla especial"""
		glutPostRedisplay()

	def keyboard(self, key, x, y):
		key = key.decode('utf-8').lower()
		self.keys_pressed.add(key)
		if key == 'q':
			glutLeaveMainLoop()
		if key == 'm':
			est.audio.toggle_musica()
		if key == 'l':
			self.lighting_manager.cycle_lighting_model()
			self.keys_pressed.discard('l')
		if key == 'c':
			if est.estado_don_corru[0] == est.estados_don_corru[0]:
				pers_args.cambiar_estado(1)		#Set caminando
			elif est.estado_don_corru[0] == est.estados_don_corru[1]:
				pers_args.cambiar_estado(0)		#Set estatico
			self.keys_pressed.discard('c')
		
		glutPostRedisplay()
	
	def keyboard_up(self, key, x, y):
		key = key.decode('utf-8').lower()
		self.keys_pressed.discard(key)
		glutPostRedisplay()

	def process_continuous_input(self):
		if 'a' in self.keys_pressed:
			est.objetos["don_corru"][0][0] -= self.movement_speed
		if 'd' in self.keys_pressed:
			est.objetos["don_corru"][0][0] += self.movement_speed
		if 'w' in self.keys_pressed:
			est.objetos["don_corru"][0][2] -= self.movement_speed
		if 's' in self.keys_pressed:
			est.objetos["don_corru"][0][2] += self.movement_speed
	
	def mouse_click(self, button, state, x, y):
		if button == 3:
			self.estado.camera_z -= 0.5
		elif button == 4:
			self.estado.camera_z += 0.5
		
		if button == GLUT_LEFT_BUTTON:
			if state == GLUT_DOWN:
				self.mouse_down = True
				self.last_mouse_x = x
				self.last_mouse_y = y
			elif state == GLUT_UP:
				self.mouse_down = False
		glutPostRedisplay()
	
	def mouse_motion(self, x, y):
		if self.mouse_down:
			dx = x - self.last_mouse_x
			dy = y - self.last_mouse_y
			self.estado.camera_angle_y -= dx
			self.estado.camera_angle_x += dy
			self.last_mouse_x = x
			self.last_mouse_y = y
		glutPostRedisplay()

	def passive_mouse_motion(self, x, y):
		area = self.estado.mouse_hover_area
		if area[0] <= x <= area[2] and area[1] <= y <= area[3]:
			print(f"Cursor sobre el área definida en ({x}, {y})")