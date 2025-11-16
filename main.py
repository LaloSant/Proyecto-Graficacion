from OpenGL.GL import *		# type: ignore
from OpenGL.GLUT import *	# type: ignore
from OpenGL.GLU import *	# type: ignore
import math
from utils.lighting import LightingManager
from utils.input_handler import InputHandler
import utils.estado as est
import utils.update as updt
from utils.audio import Audio
from objetos.personaje import Personaje
from objetos.esfera import Esfera
from objetos.dodecaedro import Dodecaedro 
from objetos.tetera import Tetera
from objetos.torus import Torus
from objetos.escena import Escena

class MainWindow:
	def __init__(self, width=800, height=600):
		self.width = width
		self.height = height
		self.lighting_manager = LightingManager()
		self.personaje = Personaje()
		self.esfera = Esfera()
		self.esfera2 = Esfera(name="Esfera2")
		self.dodecaedro = Dodecaedro()
		self.tetera = Tetera()
		self.torus = Torus()
		self.escena = Escena()
		self.input_handler = InputHandler(self.lighting_manager)
		self.audio = Audio()

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

		pos_personaje = est.objetos["Personaje"][0]

		angle_y_rad = math.radians(est.camera_angle_y)
		angle_x_rad = math.radians(est.camera_angle_x)

		eye_x = pos_personaje[0] + est.camera_z * math.sin(angle_y_rad) * math.cos(angle_x_rad)
		eye_y = pos_personaje[1] + est.camera_z * math.sin(angle_x_rad)
		eye_z = pos_personaje[2] + est.camera_z * math.cos(angle_y_rad) * math.cos(angle_x_rad)
		gluLookAt(eye_x, eye_y, eye_z, pos_personaje[0], pos_personaje[1], pos_personaje[2], 0, 1, 0)
		
		self.lighting_manager.apply_lighting()
		self.personaje.draw()
		self.esfera.draw()
		self.esfera2.draw()
		self.dodecaedro.draw()
		self.tetera.draw()
		self.torus.draw()
		self.escena.draw_room()
		self.draw_hud()
		
		glutSwapBuffers()

	def draw_hud(self):
		glMatrixMode(GL_PROJECTION)
		glPushMatrix()
		glLoadIdentity()
		gluOrtho2D(0, self.width, self.height, 0) # Origen en la esquina superior izquierda
		glMatrixMode(GL_MODELVIEW)
		glPushMatrix()
		glLoadIdentity()

		glDisable(GL_LIGHTING)
		glDisable(GL_DEPTH_TEST)

		area = est.mouse_hover_area
		glColor4f(0.5, 0.5, 1.0, 0.4) # Color azul claro semitransparente
		glEnable(GL_BLEND)
		glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
		glBegin(GL_QUADS)
		glVertex2f(area[0], area[1])
		glVertex2f(area[2], area[1])
		glVertex2f(area[2], area[3])
		glVertex2f(area[0], area[3])
		glEnd()
		glDisable(GL_BLEND)

		glEnable(GL_DEPTH_TEST)
		glEnable(GL_LIGHTING)

		glMatrixMode(GL_PROJECTION)
		glPopMatrix()
		glMatrixMode(GL_MODELVIEW)
		glPopMatrix()

def main():
	glutInit()
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)	# type: ignore
	glutInitWindowSize(800, 600)
	glutCreateWindow(b"G1_T4_3")

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
	glutSpecialUpFunc(window.input_handler.special_keys_up)
	glutMouseFunc(window.input_handler.mouse_click)
	glutMotionFunc(window.input_handler.mouse_motion)
	glutPassiveMotionFunc(window.input_handler.passive_mouse_motion)
	glutIdleFunc(window.display)

	glutMainLoop()

if __name__ == "__main__":
	main()