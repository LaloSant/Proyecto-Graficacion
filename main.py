from OpenGL.GL import *		# type: ignore
from OpenGL.GLUT import *	# type: ignore
from OpenGL.GLU import *	# type: ignore
import math
from utils.lighting import LightingManager
from utils.input_handler import InputHandler
import utils.estado as est
import utils.update as updt
from utils.audio import Audio
from source.objetos.don_corru import DonCorru
from source.objetos.kevin import Kevin
from source.objetos.kenny import Kenny
from source.escenas.escena import Escena
from source.escenas.menu import Menu

class MainWindow:
	def __init__(self, width=800, height=600):
		self.width = width
		self.height = height
		self.lighting_manager = LightingManager()
		self.don_corru = DonCorru()
		self.kevin = Kevin()
		self.kenny = Kenny()
		self.escena = Escena()
		self.audio = Audio()
		self.menu = Menu(
			on_jugar = self._on_jugar,
		)
		
		self.game_state = est.estados_juego[0]  # ["Menu", "Sel_pers", "Sel_nivel", "Nivel_1", "Nivel_2", "Nivel_3"]
		self.input_handler = InputHandler(self.lighting_manager, self.menu, self.game_state)

	def _on_jugar(self):
		self.game_state = est.estados_juego[1]

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

		if self.menu.active:
			self.game_state = est.estados_juego[0]
			self.menu.draw(self.width, self.height)
		
		glutSwapBuffers()

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
	glutKeyboardUpFunc(window.input_handler.keyboard_up)
	glutSpecialFunc(window.input_handler.special_keys)
	glutMouseFunc(window.input_handler.mouse_click)
	glutMotionFunc(window.input_handler.mouse_motion)
	glutIdleFunc(window.display)

	glutMainLoop()

if __name__ == "__main__":
	main()