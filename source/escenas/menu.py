from OpenGL.GL import *  # type: ignore
from OpenGL.GLUT import *  # type: ignore
from OpenGL.GLU import *  # type: ignore
from source.objetos.objeto import Objeto
from source.objetos.kevin import Kevin
from source.objetos.don_corru import DonCorru
from source.objetos.kenny import Kenny
import utils.estado as est


class Button:
	def __init__(self, x, y, width, height, label, callback=None):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.label = label
		self.callback = callback
		self.hovered = False
		self.color_normal = (0.3, 0.3, 0.3)
		self.color_hover = (0.6, 0.6, 0.6)
		self.color_text = (1.0, 1.0, 1.0)

	def contains_point(self, mx, my):
		return (self.x - self.width/2 <= mx <= self.x + self.width/2 and
				self.y - self.height/2 <= my <= self.y + self.height/2)

	def draw_2d(self):
		color = self.color_hover if self.hovered else self.color_normal
		glColor3f(*color)
		glBegin(GL_QUADS)
		glVertex2f(self.x - self.width/2, self.y - self.height/2)
		glVertex2f(self.x + self.width/2, self.y - self.height/2)
		glVertex2f(self.x + self.width/2, self.y + self.height/2)
		glVertex2f(self.x - self.width/2, self.y + self.height/2)
		glEnd()
		
		glColor3f(1.0, 1.0, 1.0)
		glBegin(GL_LINE_LOOP)
		glVertex2f(self.x - self.width/2, self.y - self.height/2)
		glVertex2f(self.x + self.width/2, self.y - self.height/2)
		glVertex2f(self.x + self.width/2, self.y + self.height/2)
		glVertex2f(self.x - self.width/2, self.y + self.height/2)
		glEnd()
		
		glColor3f(*self.color_text)
		glRasterPos2f(self.x - len(self.label) * 5, self.y - 5)
		for char in self.label:
			glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char)) # type: ignore

	def click(self):
		if self.callback:
			self.callback()

class Menu:
	def __init__(self, on_jugar=None, on_personaje=None, on_niveles=None, on_salir=None):
		self.active = True
		self.state = est.estados_juego[0]  #["Menu", "Sel_pers", "Sel_nivel", "Nivel_1", "Nivel_2", "Nivel_3"]
		
		self.on_jugar = on_jugar
		self.on_personaje = on_personaje
		self.on_niveles = on_niveles
		self.on_salir = on_salir
		
		self.buttons_main = [
			Button(-200, 50, 120, 40, "Jugar", self._on_jugar),
			Button(0, 50, 250, 40, "Seleccionar Personaje", self._on_personaje),
			Button(200, 50, 100, 40, "Niveles", self._on_niveles),
			Button(-80, -50, 100, 40, "Salir", self._on_salir)
		]
		
		self.buttons_personaje = [
			Button(-200, 20, 100, 40, "Kevin", lambda: self._select_personaje(est.personajes[0])),
			Button(0, 20, 120, 40, "Don Corru", lambda: self._select_personaje(est.personajes[1])),
			Button(200, 20, 100, 40, "Kenny", lambda: self._select_personaje(est.personajes[2])),
			Button(-80, -50, 100, 40, "Volver", self._back_to_main)
		]

		self.buttons_niveles = [
			Button(-200, 20, 100, 40, "Tutorial", lambda: self._select_nivel(0)),
			Button(0, 20, 120, 40, "3 Niveles", lambda: self._select_nivel(1)),
			Button(200, 20, 100, 40, "4 Niveles", lambda: self._select_nivel(2)),
			Button(-80, -50, 100, 40, "Volver", self._back_to_main)
		]
		
		self.kevin = Kevin()
		self.don_corru = DonCorru()
		self.kenny = Kenny()

	def _on_jugar(self):
		if self.on_jugar:
			self.on_jugar()
		self.active = False

	def _on_personaje(self):
		self.state = est.estados_juego[1]

	def _on_niveles(self):
		self.state = est.estados_juego[2]

	def _on_salir(self):
		if self.on_salir:
			self.on_salir()
		self.active = False

	def _select_personaje(self, est_personaje):
		self.selected_personaje = est_personaje
		if self.on_personaje:
			self.on_personaje(est_personaje)
			self.state = est.estados_juego[0]
			est.personaje_sel = est_personaje
	
	def _select_nivel(self, nivel):
		self.selected_nivel = nivel
		if self.on_niveles:
			self.on_niveles(nivel)
			self.state = est.estados_juego[0]

	def _back_to_main(self):
		self.state = est.estados_juego[0]

	def update_mouse(self, x, y):
		buttons = []
		if self.state == est.estados_juego[0]:
			buttons = self.buttons_main
		elif self.state == est.estados_juego[1]:
			buttons = self.buttons_personaje
		elif self.state == est.estados_juego[2]:
			buttons = self.buttons_niveles
		for button in buttons:
			button.hovered = button.contains_point(x, y)

	def handle_click(self, x, y):
		buttons = self.buttons_main if self.state == est.estados_juego[0] else self.buttons_personaje
		for button in buttons:
			if button.contains_point(x, y):
				button.click()
				break
		
		if self.state == est.estados_juego[1]:
			buttons = self.buttons_personaje
		else:
			buttons = self.buttons_niveles
		
		for button in buttons:
			if button.contains_point(x, y):
				button.click()
				break

	def draw(self, width, height):
		if not self.active:
			return
		
		if self.state == est.estados_juego[1]:
			self._draw_personajes_3d(width, height)
		
		glMatrixMode(GL_PROJECTION)
		glPushMatrix()
		glLoadIdentity()
		glOrtho(-width/2, width/2, -height/2, height/2, -1, 1)
		glMatrixMode(GL_MODELVIEW)
		glPushMatrix()
		glLoadIdentity()
		glDisable(GL_LIGHTING)
		glDisable(GL_TEXTURE_2D)
		glDisable(GL_DEPTH_TEST)
		glEnable(GL_BLEND)
		glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
		glColor4f(0, 0, 0, 0.2)
		glBegin(GL_QUADS)
		glVertex2f(-width/2, -height/2)
		glVertex2f(width/2, -height/2)
		glVertex2f(width/2, height/2)
		glVertex2f(-width/2, height/2)
		glEnd()
		glDisable(GL_BLEND)
		glColor3f(1.0, 1.0, 1.0)
		title = ""
		if self.state == est.estados_juego[0]:
			title = "MENU PRINCIPAL"
		elif self.state == est.estados_juego[1]:
			title = "SELECCIONAR PERSONAJE"
		elif self.state == est.estados_juego[2]:
			title = "SELECCIONAR NIVEL"

		glRasterPos2f(-len(title) * 5, height/2 - 50)
		for char in title:
			glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char)) # type: ignore

		if self.state == est.estados_juego[0]:
			for button in self.buttons_main:
				button.draw_2d()
		elif self.state == est.estados_juego[1]:
			for button in self.buttons_personaje:
				button.draw_2d()
		elif self.state == est.estados_juego[2]:
			for button in self.buttons_niveles:
				button.draw_2d()
		
		glEnable(GL_DEPTH_TEST)
		glPopMatrix()
		glMatrixMode(GL_PROJECTION)
		glPopMatrix()
		glMatrixMode(GL_MODELVIEW)
		glEnable(GL_LIGHTING)

	def _draw_personajes_3d(self, width, height):
		preview_size = 120
		positions = [
			(-200, -80, self.kevin),
			(0, -80, self.don_corru),
			(200, -80, self.kenny),
		]
		
		for pos_x, pos_y, modelo in positions:
			viewport_x = int(width/2 + pos_x - preview_size/2)
			viewport_y = int(height/2 - pos_y - preview_size/2)
			glViewport(viewport_x, viewport_y, preview_size, preview_size)
			glMatrixMode(GL_PROJECTION)
			glPushMatrix()
			glLoadIdentity()
			gluPerspective(45, 1.0, 0.1, 100)
			
			glMatrixMode(GL_MODELVIEW)
			glPushMatrix()
			glLoadIdentity()
			glTranslatef(0, 0, -5)
			glRotatef(15, 1, 0, 0)
			glRotatef(30, 0, 1, 0)
			glClear(GL_DEPTH_BUFFER_BIT)
			glEnable(GL_LIGHTING)
			glEnable(GL_DEPTH_TEST)
			glClearColor(0.2, 0.2, 0.2, 1.0)
			glShadeModel(GL_SMOOTH)
			glEnable(GL_NORMALIZE)
			glEnable(GL_LIGHTING)
			modelo.draw()
			glDisable(GL_DEPTH_TEST)
			glDisable(GL_LIGHTING)
			glPopMatrix()
			glMatrixMode(GL_PROJECTION)
			glPopMatrix()
			glMatrixMode(GL_MODELVIEW)

		glViewport(0, 0, width, height)
		glClearColor(0.0, 0.0, 0.0, 1.0)