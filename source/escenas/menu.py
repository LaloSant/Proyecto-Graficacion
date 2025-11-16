from OpenGL.GL import *  # type: ignore
from OpenGL.GLUT import *  # type: ignore
from OpenGL.GLU import *  # type: ignore
import math
from source.objetos.objeto import Objeto
from source.objetos.kevin import Kevin
from source.objetos.don_corru import DonCorru
from source.objetos.dodecaedro import Dodecaedro


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
		
		# Dibujar borde
		glColor3f(1.0, 1.0, 1.0)
		glBegin(GL_LINE_LOOP)
		glVertex2f(self.x - self.width/2, self.y - self.height/2)
		glVertex2f(self.x + self.width/2, self.y - self.height/2)
		glVertex2f(self.x + self.width/2, self.y + self.height/2)
		glVertex2f(self.x - self.width/2, self.y + self.height/2)
		glEnd()
		
		# Dibujar texto (usando GLUT)
		glColor3f(*self.color_text)
		glRasterPos2f(self.x - len(self.label) * 5, self.y - 5)
		for char in self.label:
			glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char)) # type: ignore

	def click(self):
		if self.callback:
			self.callback()


class Menu:
	"""Pantalla de menú principal"""
	def __init__(self, on_jugar=None, on_personaje=None, on_niveles=None, on_salir=None):
		self.active = True
		self.state = "main"  # main, personaje
		self.selected_personaje = None
		
		# Callbacks
		self.on_jugar = on_jugar
		self.on_personaje = on_personaje
		self.on_niveles = on_niveles
		self.on_salir = on_salir
		
		# Botones del menú principal
		self.buttons_main = [
			Button(-200, 50, 120, 40, "Jugar", self._on_jugar),
			Button(0, 50, 250, 40, "Seleccionar Personaje", self._on_personaje),
			Button(200, 50, 100, 40, "Niveles", self._on_niveles),
			Button(-80, -50, 100, 40, "Salir", self._on_salir),
		]
		
		# Botones de selección de personaje
		self.buttons_personaje = [
			Button(-100, 20, 100, 40, "Kevin", lambda: self._select_personaje("kevin")),
			Button(0, 20, 120, 40, "Don Corru", lambda: self._select_personaje("don_corru")),
			Button(100, 20, 100, 40, "Cubo", lambda: self._select_personaje("cubo")),
			Button(-80, -50, 100, 40, "Volver", self._back_to_main),
		]
		
		# Objetos 3D para mostrar
		self.kevin = Kevin()
		self.don_corru = DonCorru()
		self.cubo = Dodecaedro()  # Placeholder: usando dodecaedro como cubo

	def _on_jugar(self):
		if self.on_jugar:
			self.on_jugar()
		self.active = False

	def _on_personaje(self):
		self.state = "personaje"

	def _on_niveles(self):
		if self.on_niveles:
			self.on_niveles()
		self.active = False

	def _on_salir(self):
		if self.on_salir:
			self.on_salir()
		self.active = False

	def _select_personaje(self, personaje):
		self.selected_personaje = personaje
		if self.on_personaje:
			self.on_personaje(personaje)
		self.active = False

	def _back_to_main(self):
		self.state = "main"

	def update_mouse(self, x, y):
		"""Actualiza el estado hover de los botones según la posición del mouse"""
		buttons = self.buttons_main if self.state == "main" else self.buttons_personaje
		
		for button in buttons:
			button.hovered = button.contains_point(x, y)

	def handle_click(self, x, y):
		"""Maneja el click del mouse"""
		buttons = self.buttons_main if self.state == "main" else self.buttons_personaje
		
		for button in buttons:
			if button.contains_point(x, y):
				button.click()
				break

	def draw(self, width, height):
		"""Dibuja el menú"""
		if not self.active:
			return

		# Configurar matriz de proyección 2D
		glMatrixMode(GL_PROJECTION)
		glPushMatrix()
		glLoadIdentity()
		glOrtho(-width/2, width/2, -height/2, height/2, -1, 1)
		
		glMatrixMode(GL_MODELVIEW)
		glPushMatrix()
		glLoadIdentity()

		# Desactivar iluminación y texturas para la UI
		glDisable(GL_LIGHTING)
		glDisable(GL_TEXTURE_2D)
		glDisable(GL_DEPTH_TEST)

		# Dibujar fondo oscuro semi-transparente
		glEnable(GL_BLEND)
		glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
		glColor4f(0, 0, 0, 0.7)
		glBegin(GL_QUADS)
		glVertex2f(-width/2, -height/2)
		glVertex2f(width/2, -height/2)
		glVertex2f(width/2, height/2)
		glVertex2f(-width/2, height/2)
		glEnd()
		glDisable(GL_BLEND)

		# Dibujar título
		glColor3f(1.0, 1.0, 1.0)
		title = "MENU PRINCIPAL" if self.state == "main" else "SELECCIONAR PERSONAJE"
		glRasterPos2f(-len(title) * 5, height/2 - 50)
		for char in title:
			glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char)) # type: ignore

		# Dibujar botones
		if self.state == "main":
			for button in self.buttons_main:
				button.draw_2d()
		elif self.state == "personaje":
			for button in self.buttons_personaje:
				button.draw_2d()
			
			# Dibujar etiquetas de personajes
			self._draw_personaje_labels(width, height)

		glEnable(GL_DEPTH_TEST)

		# Restaurar matriz de proyección
		glPopMatrix()
		glMatrixMode(GL_PROJECTION)
		glPopMatrix()
		glMatrixMode(GL_MODELVIEW)

		# Reactivar iluminación
		glEnable(GL_LIGHTING)

	def _draw_personaje_labels(self, width, height):
		"""Dibuja las etiquetas de los personajes"""
		personajes = ["Kevin", "Don Corru", "Cubo"]
		positions = [
			(-200, 80),
			(0, 80),
			(200, 80),
		]
		
		for personaje, pos in zip(personajes, positions):
			glColor3f(0.7, 0.9, 1.0)
			glRasterPos2f(pos[0] - len(personaje) * 3, pos[1])
			for char in personaje:
				glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, ord(char)) # pyright: ignore[reportUndefinedVariable]
			# glPushMatrix()
