# utils/input_handler.py
from OpenGL.GLUT import * # type: ignore
import utils.estado as est
import utils.juego as game
import source.objetos.pers_args as pers_args
from source.escenas.menu import Menu

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
			print("", end="")
		
		# Permitir cerrar overlay de victoria con Enter
		if key in ('\r', '\n'):
			if est.juego_completado and not self.menu.active:
				est.juego_completado = False
				from utils.juego import Nivel1, Nivel2, Nivel3
				niveles = [Nivel1(), Nivel2(), Nivel3()]
				niveles[est.nivel_sel].reiniciar()
				glutPostRedisplay()
				return
			elif est.game_over and not self.menu.active:
				# Reintentar nivel
				est.game_over = False
				pers_args.brazos_arriba =False
				from utils.juego import Nivel1, Nivel2, Nivel3
				niveles = [Nivel1(), Nivel2(), Nivel3()]
				niveles[est.nivel_sel].reiniciar()
				glutPostRedisplay()
				return
			elif self.menu.active and self.menu.state == est.estados_juego[1]:
				self.menu.active = False
				est.menu_activo = False
				from utils.juego import Nivel1, Nivel2, Nivel3
				niveles = [Nivel1(), Nivel2(), Nivel3()]
				niveles[est.nivel_sel].reiniciar()
				glutPostRedisplay()
				return
			elif self.menu.active and self.menu.state == est.estados_juego[0]:
				est.audio.sonido_corto(7)
				self.menu.state = est.estados_juego[1]
				glutPostRedisplay()
				return
		self.keys_pressed.add(key)

		if est.juego_completado:
			if key == 'o' and est.nivel_sel < 2 and not self.menu.active: 
				next_lvl = min(est.nivel_sel + 1, 2)
				if next_lvl == 0:
					lvl = game.Nivel1()
					lvl.reiniciar()
				elif next_lvl == 1:
					lvl = game.Nivel2()
					lvl.reiniciar()
				else:
					lvl = game.Nivel3()
					lvl.reiniciar()
				est.nivel_sel = next_lvl
				est.total_movimientos_discos = 0
				est.juego_completado = False
				glutPostRedisplay()
				return

		if self.menu.active and self.menu.state == est.estados_juego[1]:
			if key == 'a':
				self._move_personaje(-1)
			elif key == 'd':
				self._move_personaje(1)
			elif key == 'n':
				self.menu.state = est.estados_juego[2]

		if self.menu.active and self.menu.state == est.estados_juego[2]:
			if key == '1': 
				self.menu._select_nivel(0)
			elif key == '2':
				self.menu._select_nivel(1)
			elif key == '3': 
				self.menu._select_nivel(2)
		
		if key == '\x1b': 
			if self.menu.active:
				if self.menu.state == est.estados_juego[2]: 
					self.menu.state = est.estados_juego[1] 
				elif self.menu.state == est.estados_juego[1]:
					self.menu.state = est.estados_juego[0] 
				elif self.menu.state == est.estados_juego[0]:
					glutLeaveMainLoop()

		
		
		if key == 'q':
			glutLeaveMainLoop()
		if key == 'p' and not self.menu.active:
			est.game_over=False
			pers_args.brazos_arriba = False
			self.menu.active = True
			est.menu_activo = True
			self.estado_ventana = est.estados_juego[0]
			est.audio.musica_on(0)
			est.audio.canal_audio_voz.stop()
		if key == 'm':
			est.audio.toggle_musica()
		if key == 'i':
			est.mostrarControles = not est.mostrarControles
		""" if key == "w":
			est.juego_completado = True """
		if not self.menu.active and est.caminando_pct == 0:
			if key == 'a':
				if est.posicion_pers_sel <= -1 or est.caminando_pct != 0:
					return
				if est.juego_completado:
					return
				if est.game_over:
					return
				est.estado_pers[0] = est.estados_pers[1]
				est.posicion_pers_sel -= 1
				est.caminando_pct = -1
			elif key == 'd':
				if est.posicion_pers_sel >= 1 or est.caminando_pct != 0:
					return
				if est.juego_completado:
					return
				if est.game_over:
					return
				est.estado_pers[0] = est.estados_pers[1]
				est.posicion_pers_sel += 1
				est.caminando_pct = +1
			elif key == 'b':
				if est.juego_completado:
					return
				if est.game_over:
					return
				if not pers_args.brazos_arriba:
					if game.agarrar_disco():
						est.estado_pers[0] = est.estados_pers[2]
						pers_args.brazos_arriba = not pers_args.brazos_arriba
				else:
					if est.disco_agarrado is None:
						return
					if game.poner_disco():
						est.estado_pers[0] = est.estados_pers[2]
						est.total_movimientos_discos += 1
						if game.verificar_victoria():
							est.juego_completado = True
							est.audio.musica_on(4) 
						pers_args.brazos_arriba = not pers_args.brazos_arriba
					
		glutPostRedisplay()
	
	def _move_personaje(self, direction):
		personajes = est.personajes
		idx = personajes.index(est.personaje_sel)
		new_idx = (idx + direction) % len(personajes)  # ciclar
		est.personaje_sel = personajes[new_idx]
		self.menu.selected_personaje = est.personaje_sel


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

		if est.juego_completado and button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
			
			width = 1000
			height = 600
			cx = width // 2
			cy = height // 2
			w = 520
			h = 240
			bx = cx - w//2
			by = cy - h//2
			
			btn_w = 200
			btn_h = 50
			left_btn_x = int(bx + w*0.25 - btn_w/2)
			right_btn_x = int(bx + w*0.75 - btn_w/2)
			btn_y = int(by + h - 80)
			
			if left_btn_x <= x <= left_btn_x + btn_w and btn_y <= y <= btn_y + btn_h:
				
				self.menu.active = True
				est.menu_activo = True
				est.juego_completado = False
				est.audio.musica_on(0)
				glutPostRedisplay()
				return
			
			if right_btn_x <= x <= right_btn_x + btn_w and btn_y <= y <= btn_y + btn_h:
				
				import utils.juego as game
				next_lvl = min(est.nivel_sel + 1, 2)
				if next_lvl == 0:
					lvl = game.Nivel1()
					lvl.reiniciar()
				elif next_lvl == 1:
					lvl = game.Nivel2()
					lvl.reiniciar()
				else:
					lvl = game.Nivel3()
					lvl.reiniciar()
				est.nivel_sel = next_lvl
				est.total_movimientos_discos = 0
				est.juego_completado = False
				glutPostRedisplay()
				return

		if est.game_over and button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
			pers_args.brazos_arriba =False
			width = 1000
			height = 600
			cx = width // 2
			cy = height // 2
			w = 520
			h = 240
			bx = cx - w//2
			by = cy - h//2
			
			btn_w = 200
			btn_h = 50
			menu_btn_x = int(cx - btn_w/2)
			btn_y = int(by + h - 80)
			
			if menu_btn_x <= x <= menu_btn_x + btn_w and btn_y <= y <= btn_y + btn_h:
				self.menu.active = True
				est.menu_activo = True
				est.game_over = False
				est.juego_completado = False
				est.audio.musica_on(0)
				glutPostRedisplay()
				return

		if button == 3:
			if self.estado.camera_z > 1:
				self.estado.camera_z -= 0.5
		elif button == 4:
			if self.estado.camera_z < 20:
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
			self.estado.camera_angle_y -= dx * self.movement_speed
			self.estado.camera_angle_x += dy * self.movement_speed
			self.estado.camera_angle_x = max(0, min(90, self.estado.camera_angle_x))
			self.last_mouse_x = x
			self.last_mouse_y = y
		glutPostRedisplay()