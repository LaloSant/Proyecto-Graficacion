# main.py
from OpenGL.GL import *		# type: ignore
from OpenGL.GLUT import *	# type: ignore
from OpenGL.GLU import *	# type: ignore
import math
from utils.lighting import LightingManager
from utils.input_handler import InputHandler
from utils.texturas import load_texture
from utils.audio import Audio
from utils.juego import *
import utils.estado as est
import utils.update as updt
import utils.audio as audio

from source.objetos.don_corru import DonCorru
from source.objetos.kevin import Kevin
from source.objetos.kenny import Kenny
from source.objetos.base_piramide import BasePiramide
from source.objetos.disco import Disco
from source.escenas.escena import Escena
from source.escenas.menu import Menu

def render_text(x, y, text):
	glRasterPos2f(x, y)
	for char in text:
		glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char)) # type: ignore

class MainWindow:
	def __init__(self, width=1200, height=650):
		self.width = width
		self.height = height
		self.lighting_manager = LightingManager()
		self.don_corru = DonCorru()
		self.kevin = Kevin()
		self.kenny = Kenny()
		self.piramides = [BasePiramide(-5), BasePiramide(0), BasePiramide(5)]
		est.audio = Audio()
		self.niveles:list[Nivel] = [Nivel1(), Nivel2(), Nivel3()]
		self.escena = Escena()
		self.menu = Menu(
			on_jugar = self._on_jugar,
		)
		
		self.game_state = est.estados_juego[0]  # ["Menu", "Sel_pers", "Sel_nivel", "Nivel_1", "Nivel_2", "Nivel_3"]
		self.input_handler = InputHandler(self.lighting_manager, self.menu, self.game_state)
		self.logo_tex = load_texture("resources/imgs/Fondo.png")
		self.titulo = load_texture("resources/imgs/Titulo.png")

	def _on_jugar(self):
		self.game_state = est.estados_juego[1]
		nivel = self.niveles[est.nivel_sel]
		nivel.reiniciar()
		est.total_movimientos_discos = 0
		est.juego_completado = False

	def init_gl(self):
		glEnable(GL_DEPTH_TEST)
		glEnable(GL_LIGHTING)
		glEnable(GL_LIGHT0)
		glClearColor(0.0, 0.0, 0.0, 1.0)
		self.lighting_manager.setup_lighting()

	def reshape(self, width, height):
		self.width = width
		self.height = height
		glViewport(0, 0, width, height)
		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()
		gluPerspective(45, width/height, 0.1, 100)
		glMatrixMode(GL_MODELVIEW)

	def display(self):
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # type: ignore
		glLoadIdentity()
		angle_y_rad = math.radians(est.camera_angle_y)
		angle_x_rad = math.radians(est.camera_angle_x)
		eye_x = est.camera_z * math.sin(angle_y_rad) * math.cos(angle_x_rad)
		eye_y = est.camera_z * math.sin(angle_x_rad)
		eye_z = est.camera_z * math.cos(angle_y_rad) * math.cos(angle_x_rad)
		gluLookAt(eye_x, eye_y, eye_z, 0, 0, 0, 0, 1, 0)
		
		if not self.menu.active:
			for piramide in self.piramides:
				piramide.draw()
			for disco in est.discos:
				glPushMatrix()
				disco.draw()
				glPopMatrix()
			self.escena.draw_room(est.nivel_sel)
			self.lighting_manager.apply_lighting()
			glPushMatrix()
			x, y, z = est.posiciones_pers[est.posicion_pers_sel]
			glTranslatef(x, y, z)
			if est.personaje_sel == est.personajes[0]:
				self.kevin.draw(selected=True)
			elif est.personaje_sel == est.personajes[1]:
				self.don_corru.draw(selected=True)
			elif est.personaje_sel == est.personajes[2]:
				self.kenny.draw(selected=True)
			glPopMatrix()
			self.dibuja_contador_movimientos()

		if self.menu.active:
			self.dibuja_menu_bg()
			self.game_state = est.estados_juego[0]
			self.menu.draw(self.width, self.height)
		glutSwapBuffers()

	def dibuja_contador_movimientos(self):
		glMatrixMode(GL_PROJECTION)
		glPushMatrix()
		glLoadIdentity()
		glOrtho(0, self.width, self.height, 0, -1, 1)
		glMatrixMode(GL_MODELVIEW)
		glPushMatrix()
		glLoadIdentity()
		glDisable(GL_LIGHTING)
		glDisable(GL_DEPTH_TEST)
		glEnable(GL_BLEND)
		glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
		box_x, box_y = 20, 80 
		box_height = 160 if est.mostrarControles else 55
		box_width = 300 
		#caja en la esquina superior derecha
		if est.nivel_sel == 0:

			box_height2 = 210
			box_width2 = 450
			box2_x = self.width - box_width2 - 20
			box2_y = 20

			glColor4f(0, 0, 0, 0.7)
			glBegin(GL_QUADS)
			glVertex2f(box2_x, box2_y)
			glVertex2f(box2_x + box_width2, box2_y)
			glVertex2f(box2_x + box_width2, box2_y + box_height2)
			glVertex2f(box2_x, box2_y + box_height2)
			glEnd()
			
			glColor4f(1, 1, 1, 1) 
			glLineWidth(2)

			glBegin(GL_LINE_LOOP)
			glVertex2f(box2_x, box2_y)
			glVertex2f(box2_x + box_width2, box2_y)
			glVertex2f(box2_x + box_width2, box2_y + box_height2)
			glVertex2f(box2_x, box2_y + box_height2)
			glEnd()

			glLineWidth(1)

			render_text(box2_x + 10, box2_y + 30, "Ayuda: ")
			render_text(box2_x + 30, box2_y + 55, "Objetivo del juego:")
			render_text(box2_x + 50, box2_y + 75, "Mover todos los discos de la pirámide izquierda")
			render_text(box2_x + 50, box2_y + 95, "a la pirámide derecha.")
			render_text(box2_x + 30, box2_y + 115, "Controles:")
			render_text(box2_x + 50, box2_y + 135, "1: Usa 'B' para sostener o soltar un disco.")
			render_text(box2_x + 50, box2_y + 155, "2: No puedes colocar un disco más grande")
			render_text(box2_x + 70, box2_y + 175, "sobre uno más pequeño.")


		glColor4f(0, 0, 0, 0.7)
		glBegin(GL_QUADS)
		glVertex2f(box_x, box_y)
		glVertex2f(box_x + box_width, box_y)
		glVertex2f(box_x + box_width, box_y + box_height)
		glVertex2f(box_x, box_y + box_height)
		glEnd()

		glColor4f(1, 1, 1, 1)
		glLineWidth(2)
		glBegin(GL_LINE_LOOP)
		glVertex2f(box_x, box_y)
		glVertex2f(box_x + box_width, box_y)
		glVertex2f(box_x + box_width, box_y + box_height)
		glVertex2f(box_x, box_y + box_height)
		glEnd()
		
		glLineWidth(1)

		text_y = box_y + 30
		glColor3f(1, 1, 1)
		render_text(box_x + 10, text_y - 5, f"Total de Movimientos: {est.total_movimientos_discos}")
		
		if est.tiempo_limite > 0:
			tiempo_texto = f"Tiempo: {int(est.tiempo_limite)}s"
			glColor3f(1, 1, 1) if est.tiempo_limite > 10 else glColor3f(1, 0, 0)  
			render_text(box_x + 10, text_y + 15, tiempo_texto)
		if est.mostrarControles:
			render_text(box_x + 10, text_y + 35, "Controles: ")
			render_text(box_x + 30, text_y + 55, "A / D : Mover personaje")
			render_text(box_x + 30, text_y + 75, "B : Agarrar o dejar disco")
			render_text(box_x + 30, text_y + 95, "P : Ir a menu")
			render_text(box_x + 30, text_y + 115, "I : Mostrar / ocultar instrucciones")

		if est.juego_completado:
			text_y -= 25
			cx = self.width // 2
			cy = self.height // 2
			w = 520
			h = 240
			bx = cx - w//2
			by = cy - h//2
			glColor4f(0, 0, 0, 0.5)
			glBegin(GL_QUADS)
			glVertex2f(bx + 12, by + 12)
			glVertex2f(bx + w + 12, by + 12)
			glVertex2f(bx + w + 12, by + h + 12)
			glVertex2f(bx + 12, by + h + 12)
			glEnd()
			glColor4f(0.96, 0.58, 0.2, 0.98)
			glBegin(GL_QUADS)
			glVertex2f(bx, by)
			glVertex2f(bx + w, by)
			glVertex2f(bx + w, by + h)
			glVertex2f(bx, by + h)
			glEnd()
			glLineWidth(3)
			glColor3f(1, 1, 1)
			glBegin(GL_LINE_LOOP)
			glVertex2f(bx, by)
			glVertex2f(bx + w, by)
			glVertex2f(bx + w, by + h)
			glVertex2f(bx, by + h)
			glEnd()
			glLineWidth(1)
			title = "NIVEL COMPLETADO!!"
			est.audio.canal_audio_voz.stop()
			glColor3f(1, 1, 1)
			render_text(cx - len(title)*7, by + h - 200, title)
			glColor3f(1, 1, 1)
			if est.total_movimientos_discos == 0:
				puntaje = 0
			else:
				puntaje = self.niveles[est.nivel_sel].movimientos_optimos / est.total_movimientos_discos * 100
			render_text(bx + 40, by + h - 120, f"PUNTAJE: {puntaje:.2f}")
			render_text(bx + 40, by + h - 160, f"CLASIFICACION: {self.niveles[est.nivel_sel].calcular_clasificacion(puntaje)}")
			
			btn_w = 200
			btn_h = 50
			left_btn_x = int(bx + w*0.25 - btn_w/2)
			right_btn_x = int(bx + w*0.75 - btn_w/2)
			btn_y = int(by + h - 80)
			# Botón izquierdo - Menú principal (fondo oscuro)
			glColor4f(0.12, 0.12, 0.12, 0.95)
			glBegin(GL_QUADS)
			glVertex2f(left_btn_x, btn_y)
			glVertex2f(left_btn_x + btn_w, btn_y)
			glVertex2f(left_btn_x + btn_w, btn_y + btn_h)
			glVertex2f(left_btn_x, btn_y + btn_h)
			glEnd()
			# Borde botón izquierdo
			glLineWidth(2)
			glColor3f(1, 1, 1)
			glBegin(GL_LINE_LOOP)
			glVertex2f(left_btn_x, btn_y)
			glVertex2f(left_btn_x + btn_w, btn_y)
			glVertex2f(left_btn_x + btn_w, btn_y + btn_h)
			glVertex2f(left_btn_x, btn_y + btn_h)
			glEnd()
			glLineWidth(1)
			# Texto centrado botón izquierda 
			label_left = "MENÚ PRINCIPAL (P)"
			tx = left_btn_x + btn_w//2 - int(len(label_left) * 4)
			ty = btn_y + btn_h//2 + 6
			glColor3f(1, 1, 1)
			render_text(tx - 20, ty, label_left)

			if est.nivel_sel < 2:

				# Botón derecho - Siguiente nivel (fondo oscuro)
				glColor4f(0.12, 0.12, 0.12, 0.95)
				glBegin(GL_QUADS)
				glVertex2f(right_btn_x, btn_y)
				glVertex2f(right_btn_x + btn_w, btn_y)
				glVertex2f(right_btn_x + btn_w, btn_y + btn_h)
				glVertex2f(right_btn_x, btn_y + btn_h)
				glEnd()
				# Borde botón derecho
				glLineWidth(2)
				glColor3f(0,0,0)
				glBegin(GL_LINE_LOOP)
				glVertex2f(right_btn_x, btn_y)
				glVertex2f(right_btn_x + btn_w, btn_y)
				glVertex2f(right_btn_x + btn_w, btn_y + btn_h)
				glVertex2f(right_btn_x, btn_y + btn_h)
				glEnd()
				glLineWidth(1)
				# Texto centrado botón derecho
				label_right = "SIGUIENTE NIVEL (O)"
				tx2 = right_btn_x + btn_w//2 - int(len(label_right) * 4)
				y2 = btn_y + btn_h//2 + 6
				glColor3f(1, 1, 1)
				render_text(tx2 - 20, y2, label_right)
		
		
		if est.game_over:
			cx = self.width // 2
			cy = self.height // 2
			w = 520
			h = 240
			bx = cx - w//2
			by = cy - h//2
			glColor4f(0, 0, 0, 0.5)
			glBegin(GL_QUADS)
			glVertex2f(bx + 12, by + 12)
			glVertex2f(bx + w + 12, by + 12)
			glVertex2f(bx + w + 12, by + h + 12)
			glVertex2f(bx + 12, by + h + 12)
			glEnd()
			glColor4f(0.8, 0.2, 0.2, 0.98)  # Rojo para game over
			glBegin(GL_QUADS)
			glVertex2f(bx, by)
			glVertex2f(bx + w, by)
			glVertex2f(bx + w, by + h)
			glVertex2f(bx, by + h)
			glEnd()
			glLineWidth(3)
			glColor3f(1, 1, 1)
			glBegin(GL_LINE_LOOP)
			glVertex2f(bx, by)
			glVertex2f(bx + w, by)
			glVertex2f(bx + w, by + h)
			glVertex2f(bx, by + h)
			glEnd()
			glLineWidth(1)
			title = "¡TIEMPO AGOTADO!"
			glColor3f(1, 1, 1)
			render_text(cx - len(title)*7, by + h - 200, title)
			glColor3f(1, 1, 1)
			render_text(bx + 40, by + h - 120, f"MOVIMIENTOS: {est.total_movimientos_discos}")
			render_text(bx + 40, by + h - 160, "PRESIONA ENTER PARA REINTENTAR")
			
			btn_w = 230
			btn_h = 50
			menu_btn_x = int(cx - btn_w/2)
			btn_y = int(by + h - 80)
			# Botón - Menú principal
			glColor4f(0.12, 0.12, 0.12, 0.95)
			glBegin(GL_QUADS)
			glVertex2f(menu_btn_x, btn_y)
			glVertex2f(menu_btn_x + btn_w, btn_y)
			glVertex2f(menu_btn_x + btn_w, btn_y + btn_h)
			glVertex2f(menu_btn_x, btn_y + btn_h)
			glEnd()
			# Borde botón
			glLineWidth(2)
			glColor3f(1, 1, 1)
			glBegin(GL_LINE_LOOP)
			glVertex2f(menu_btn_x, btn_y)
			glVertex2f(menu_btn_x + btn_w, btn_y)
			glVertex2f(menu_btn_x + btn_w, btn_y + btn_h)
			glVertex2f(menu_btn_x, btn_y + btn_h)
			glEnd()
			glLineWidth(1)
			# Texto centrado botón
			label = "MENÚ PRINCIPAL (P)"
			tx = menu_btn_x + btn_w//2 - int(len(label) * 4)
			ty = btn_y + btn_h//2 + 6
			glColor3f(1, 1, 1)
			render_text(tx - 20, ty, label)
		glDisable(GL_BLEND)
		glEnable(GL_DEPTH_TEST)
		glEnable(GL_LIGHTING)
		glPopMatrix()
		glMatrixMode(GL_PROJECTION)
		glPopMatrix()
		glMatrixMode(GL_MODELVIEW)

	def dibuja_menu_bg(self):
			glMatrixMode(GL_PROJECTION)
			glPushMatrix()
			glLoadIdentity()
			glOrtho(0, self.width, self.height, 0, -1, 1)	
			glMatrixMode(GL_MODELVIEW)
			glPushMatrix()
			glLoadIdentity()
			glDisable(GL_LIGHTING)
			glDisable(GL_DEPTH_TEST)
			glEnable(GL_BLEND)
			glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
			glColor4f(96/255, 171/255, 217/255, 1.0)
			glBegin(GL_QUADS)
			glVertex2f(0, 0)
			glVertex2f(self.width, 0)
			glVertex2f(self.width, self.height)
			glVertex2f(0, self.height)
			glEnd()
			glDisable(GL_BLEND)
		
			glEnable(GL_TEXTURE_2D)
			glBindTexture(GL_TEXTURE_2D, self.logo_tex)
			logo_w, logo_h = 256 * 5.5, 128 * 5.5	
			x = (self.width - logo_w) // 2
			y = -50
			glColor4f(1, 1, 1, 1)
			glBegin(GL_QUADS)
			glTexCoord2f(0, 1); glVertex2f(x, y)
			glTexCoord2f(1, 1); glVertex2f(x + logo_w, y)
			glTexCoord2f(1, 0); glVertex2f(x + logo_w, y + logo_h)
			glTexCoord2f(0, 0); glVertex2f(x, y + logo_h)
			glEnd()
			glBindTexture(GL_TEXTURE_2D, 0)
			glDisable(GL_TEXTURE_2D)

			glEnable(GL_BLEND)
			glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
			glEnable(GL_TEXTURE_2D)
			glBindTexture(GL_TEXTURE_2D, self.titulo)
			titulo_w = 600
			titulo_h = 300
			titulo_x = (self.width - titulo_w) // 2
			titulo_y = -50  

			glColor4f(1, 1, 1, 1)
			glBegin(GL_QUADS)
			glTexCoord2f(0, 1); glVertex2f(titulo_x, titulo_y)
			glTexCoord2f(1, 1); glVertex2f(titulo_x + titulo_w, titulo_y)
			glTexCoord2f(1, 0); glVertex2f(titulo_x + titulo_w, titulo_y + titulo_h)
			glTexCoord2f(0, 0); glVertex2f(titulo_x, titulo_y + titulo_h)
			glEnd()

			glBindTexture(GL_TEXTURE_2D, 0)
			glDisable(GL_TEXTURE_2D)
			glDisable(GL_BLEND)

			glEnable(GL_DEPTH_TEST)
			glEnable(GL_LIGHTING)
			glPopMatrix()
			glMatrixMode(GL_PROJECTION)
			glPopMatrix()
			glMatrixMode(GL_MODELVIEW)

def main():
	glutInit()
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)	# type: ignore
	glutInitWindowSize(1000, 600)
	glutCreateWindow(b"Cumbres cognitivas")

	window = MainWindow()
	window.init_gl()
	# est.audio = window.audio

	updt.set_input_handler(window.input_handler, window.escena)
	updt.update(0)
	glutDisplayFunc(window.display)
	glutReshapeFunc(window.reshape)
	glutKeyboardFunc(window.input_handler.keyboard)
	glutSpecialFunc(window.input_handler.special_keys)
	glutMouseFunc(window.input_handler.mouse_click)
	glutMotionFunc(window.input_handler.mouse_motion)
	glutIdleFunc(window.display)

	glutMainLoop()

if __name__ == "__main__":
	main()