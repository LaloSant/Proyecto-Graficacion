from OpenGL.GLUT import * # type: ignore
import utils.estado as est
import source.objetos.pers_args as pers_args
from source.escenas.menu import Menu
import utils.juego as game

class InputHandler:
	def __init__(self, lighting_manager, menu:Menu, estado_ventana):
		self.lighting_manager = lighting_manager
		self.menu:Menu = menu
		self.estado_ventana = estado_ventana
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

	def keyboard(self, key, x, y):
		try:
			key = key.decode('utf-8').lower()
		except Exception:
			print("")
		self.keys_pressed.add(key)
		if key == 'q':
			glutLeaveMainLoop()
		if key == 'p':
			self.menu.active = True
			self.estado_ventana = est.estados_juego[0]
		if key == 'm':
			est.audio.toggle_musica()
		""" if key == 'l':
			self.lighting_manager.cycle_lighting_model()
			self.keys_pressed.discard('l') """
		""" if key == 'c':
			if est.estado_pers[0] == est.estados_pers[0]:
				pers_args.cambiar_estado(1)		#Set caminando
			elif est.estado_pers[0] == est.estados_pers[1]:
				pers_args.cambiar_estado(0)		#Set estatico
			self.keys_pressed.discard('c') """
		if not self.menu.active and est.caminando_pct == 0:
			if key == 'a':
				if est.posicion_pers_sel <= -1 or est.caminando_pct != 0:
					return
				est.estado_pers[0] = est.estados_pers[1]
				est.posicion_pers_sel -= 1
				est.caminando_pct = -1
			elif key == 'd':
				if est.posicion_pers_sel >= 1 or est.caminando_pct != 0:
					return
				est.estado_pers[0] = est.estados_pers[1]
				est.posicion_pers_sel += 1
				est.caminando_pct = +1
			elif key == 'b':
				if est.juego_completado:
					return
				if not pers_args.brazos_arriba:
					if game.agarrar_disco():
						est.estado_pers[0] = est.estados_pers[2]
						pers_args.brazos_arriba = not pers_args.brazos_arriba
					else:
						print("No disco")
				else:
					if est.disco_agarrado is None:
						return
					if game.poner_disco():
						est.estado_pers[0] = est.estados_pers[2]
						est.total_movimientos_discos += 1
						if game.verificar_victoria():
							est.juego_completado = True
						pers_args.brazos_arriba = not pers_args.brazos_arriba
					
		glutPostRedisplay()
	
	def keyboard_up(self, key, x, y):
		key = key.decode('utf-8').lower()
		self.keys_pressed.discard(key)
		glutPostRedisplay()
	
	def mouse_click(self, button, state, x, y):
		if self.menu and self.menu.active:
			width = 1000
			height = 600
			gl_x = (x - width/2)
			gl_y = -(y - height/2)
			
			if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
				self.menu.handle_click(gl_x, gl_y)
			glutPostRedisplay()
			return

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