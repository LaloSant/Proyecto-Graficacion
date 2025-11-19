from OpenGL.GL import *		# type: ignore
from OpenGL.GLUT import *	# type: ignore
from OpenGL.GLU import *	# type: ignore
import math
from utils.lighting import LightingManager
from utils.input_handler import InputHandler
import utils.estado as est
import utils.update as updt
from utils.audio import Audio
from utils.juego import *
from source.objetos.don_corru import DonCorru
from source.objetos.kevin import Kevin
from source.objetos.kenny import Kenny
from source.objetos.base_piramide import BasePiramide
from source.objetos.disco import Disco
from source.escenas.escena import Escena
from source.escenas.menu import Menu

def render_text(x, y, text):
	"""Renderiza texto en la pantalla usando GLUT bitmap fonts"""
	glRasterPos2f(x, y)
	for char in text:
		glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char)) # type: ignore


class MainWindow:
	def __init__(self, width=800, height=600):
		self.width = width
		self.height = height
		self.lighting_manager = LightingManager()
		self.don_corru = DonCorru()
		self.kevin = Kevin()
		self.kenny = Kenny()
		self.piramides = [BasePiramide(-5), BasePiramide(0), BasePiramide(5)]
		self.niveles = [Nivel1(), Nivel2(), Nivel3()]
		self.escena = Escena()
		self.audio = Audio()
		self.menu = Menu(
			on_jugar = self._on_jugar,
		)
		
		self.game_state = est.estados_juego[0]  # ["Menu", "Sel_pers", "Sel_nivel", "Nivel_1", "Nivel_2", "Nivel_3"]
		self.input_handler = InputHandler(self.lighting_manager, self.menu, self.game_state)
		# Cargar textura del logo
		from utils.texturas import load_texture
		self.logo_tex = load_texture("resources/imgs/LogoCC.png")

	def _on_jugar(self):
		self.game_state = est.estados_juego[1]
		nivel = self.niveles[est.nivel_sel + 1]
		nivel.reiniciar()
		# Resetear contadores y estado de victoria
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
				self.kevin.draw()
			elif est.personaje_sel == est.personajes[1]:
				self.don_corru.draw()
			elif est.personaje_sel == est.personajes[2]:
				self.kenny.draw()

			glPopMatrix()
			
			# Dibujar contador de movimientos
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
		box_height = 100 if est.juego_completado else 70
		box_width, box_height = 300, box_height
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
		
		
		text_y = box_y + 15
		glColor3f(1, 1, 1)
		render_text(box_x + 10, text_y, f"Total de Movimientos: {est.total_movimientos_discos}")
		
		
		
		if est.juego_completado:
			text_y -= 25
			glColor3f(0, 1, 0)
			render_text(box_x + 10, text_y, "¡JUEGO COMPLETADO!")
		
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
			logo_w, logo_h = 256 * 1.5, 128 * 1.5
			x = (self.width - logo_w) // 2
			y = 30 
			glColor4f(1, 1, 1, 1)
			glBegin(GL_QUADS)
			glTexCoord2f(0, 1); glVertex2f(x, y)
			glTexCoord2f(1, 1); glVertex2f(x + logo_w, y)
			glTexCoord2f(1, 0); glVertex2f(x + logo_w, y + logo_h)
			glTexCoord2f(0, 0); glVertex2f(x, y + logo_h)
			glEnd()
			glBindTexture(GL_TEXTURE_2D, 0)
			glDisable(GL_TEXTURE_2D)
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
	est.audio = window.audio

	updt.set_input_handler(window.input_handler, window.escena)
	updt.update(0)
	glutDisplayFunc(window.display)
	glutReshapeFunc(window.reshape)
	glutKeyboardFunc(window.input_handler.keyboard)
	# glutKeyboardUpFunc(window.input_handler.keyboard_up)
	glutSpecialFunc(window.input_handler.special_keys)
	glutMouseFunc(window.input_handler.mouse_click)
	glutMotionFunc(window.input_handler.mouse_motion)
	glutIdleFunc(window.display)

	glutMainLoop()

if __name__ == "__main__":
	main()