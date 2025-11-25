# source/escenas/menu.py
import math
from OpenGL.GL import *  # type: ignore
from OpenGL.GLUT import *  # type: ignore
from OpenGL.GLU import *  # type: ignore
from source.objetos.objeto import Objeto
from source.objetos.kevin import Kevin
from source.objetos.don_corru import DonCorru
from source.objetos.kenny import Kenny
import utils.estado as est
import utils.texturas as text
from utils.texturas import load_texture



class Button:
	def __init__(self, x, y, width, height, label, callback=None, texture=None):

		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.label = label
		self.callback = callback
		self.hovered = False
		self.texture = texture
		self.color_normal = (0.3, 0.3, 0.3)
		self.color_hover = (0.6, 0.6, 0.6)
		self.color_text = (1.0, 1.0, 1.0)

	def contains_point(self, mx, my):
		return (self.x - self.width/2 <= mx <= self.x + self.width/2 and
				self.y - self.height/2 <= my <= self.y + self.height/2)

	def draw_2d(self):


		glEnable(GL_BLEND)
		glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

		if self.texture:
			glEnable(GL_TEXTURE_2D)
			glBindTexture(GL_TEXTURE_2D, self.texture)
			glColor3f(1, 1, 1)  # Color blanco para que NO se tinte
		else:
			color = self.color_hover if self.hovered else self.color_normal
			glColor3f(*color)

		# Dibujar botón
		glBegin(GL_QUADS)
		if self.texture:
			glTexCoord2f(0, 0)
		glVertex2f(self.x - self.width/2, self.y - self.height/2)

		if self.texture:
			glTexCoord2f(1, 0)
		glVertex2f(self.x + self.width/2, self.y - self.height/2)

		if self.texture:
			glTexCoord2f(1, 1)
		glVertex2f(self.x + self.width/2, self.y + self.height/2)

		if self.texture:
			glTexCoord2f(0, 1)
		glVertex2f(self.x - self.width/2, self.y + self.height/2)
		glEnd()

		# Desactivar textura
		if self.texture:
			glBindTexture(GL_TEXTURE_2D, 0)
			glDisable(GL_TEXTURE_2D)

		# Borde
		# glColor3f(0,0,0)
		# glBegin(GL_LINE_LOOP)
		# glVertex2f(self.x - self.width/2, self.y - self.height/2)
		# glVertex2f(self.x + self.width/2, self.y - self.height/2)
		# glVertex2f(self.x + self.width/2, self.y + self.height/2)
		# glVertex2f(self.x - self.width/2, self.y + self.height/2)
		# glEnd()

		glDisable(GL_BLEND)

		# Texto
		glColor3f(*self.color_text)
		glRasterPos2f(self.x - len(self.label)*5, self.y - 5)
		for char in self.label:
			glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char)) # type: ignore


	def click(self):
		if self.callback:
			self.callback()

class Menu:
	def __init__(self, on_jugar=None, on_personaje=None, on_niveles=None, on_salir=None):

		self.fondo_kevin = load_texture("resources/imgs/KevinFondo.png")
		self.fondo_doncorru = load_texture("resources/imgs/DonCorruFondo.png")
		self.fondo_kenny = load_texture("resources/imgs/KennyFondo.png")
		self.seleccionar_personaje = load_texture("resources/imgs/seleccion_personajes.png")
		self.derecha = load_texture("resources/imgs/derecha.png")
		self.izquierda = load_texture("resources/imgs/izquierda.png")

		self.active = True
		self.state = est.estados_juego[0]  #["Menu", "Sel_pers", "Sel_nivel", "Nivel_1", "Nivel_2", "Nivel_3"]
		
		self.on_jugar = on_jugar
		self.on_personaje = on_personaje
		self.on_niveles = on_niveles
		self.on_salir = on_salir

		boton_inicio = load_texture("resources/imgs/boton_inicio.png")
		boton_salir = load_texture("resources/imgs/boton_salir.png")
		boton_volver = load_texture("resources/imgs/boton_volver.png")
		boton_jugar = load_texture("resources/imgs/boton_jugar.png")
		boton_niveles = load_texture("resources/imgs/boton_niveles.png")
		boton_tutorial = load_texture("resources/imgs/boton_tutorial.png")
		boton_3_discos = load_texture("resources/imgs/boton_3_discos.png")
		boton_4_discos = load_texture("resources/imgs/boton_4_discos.png")
		
		self.buttons_main = [
			Button(0, 50, 200, 70, "", self._on_personaje, boton_inicio),
			Button(400, -250, 162, 50, "", self._on_salir, boton_salir)
		]

		self.buttons_personaje = [
			Button(-200, -80, 200, 200, "Kevin", lambda: self._select_personaje(est.personajes[0])),
			Button(0, -80, 200, 200, "Don Corru", lambda: self._select_personaje(est.personajes[1])),
			Button(200, -80, 200, 200, "Kenny", lambda: self._select_personaje(est.personajes[2])),

			Button(400, -250, 162, 50 , "", self._back_to_main, boton_volver),
			Button(-150, -230, 180, 60, "", self._on_jugar, boton_jugar),
			Button(150, -230, 180, 60, "", self._on_niveles, boton_niveles)
		]

		self.buttons_niveles = [
			Button(-220,-50,200, 70, "", lambda: self._select_nivel(0), boton_tutorial),
			Button(0,-50, 200, 70, "", lambda: self._select_nivel(1), boton_3_discos),
			Button(220,-50, 200, 70, "", lambda: self._select_nivel(2), boton_4_discos),
			Button(400, -250, 162, 50, "", self._on_personaje, boton_volver)
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
		glutLeaveMainLoop()

	def _select_personaje(self, est_personaje):
		self.selected_personaje = est_personaje
		#self.state = est.estados_juego[0]
		est.personaje_sel = est_personaje
	
	def _select_nivel(self, nivel):
		self.selected_nivel = nivel
		self.state = est.estados_juego[1]
		est.nivel_sel = nivel

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
		buttons = []
		if self.state == est.estados_juego[0]:
			buttons = self.buttons_main
		elif self.state == est.estados_juego[1]:
			buttons = self.buttons_personaje
		elif self.state == est.estados_juego[2]:
			buttons = self.buttons_niveles
		for button in buttons:
			if button.contains_point(x, y):
				button.click()
				break

	def draw(self, width, height):
		if not self.active:
			return

		if self.state == est.estados_juego[1]:
			fondo = self._get_fondo_actual()
			if fondo:
				self._draw_fondo(fondo, width, height)

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
		glColor4f(0, 0, 0, 0.18)
		glBegin(GL_QUADS)
		glVertex2f(-width/2, -height/2)
		glVertex2f(width/2, -height/2)
		glVertex2f(width/2, height/2)
		glVertex2f(-width/2, height/2)
		glEnd()
		glDisable(GL_BLEND)

		glColor4f(1, 1, 1, 1)
		if self.state == est.estados_juego[0]:
			title = "MENU PRINCIPAL"
		elif self.state == est.estados_juego[1]:
			self._draw_textura(self.seleccionar_personaje, width, height, img_w = 750, img_h = 50, offset_y = 150, offset_x = 0)
			self._draw_textura(self.izquierda, width, height, img_w = 230, img_h = 80, offset_y = -60, offset_x = -375)
			self._draw_textura(self.derecha, width, height, img_w = 230, img_h = 80, offset_y = -60, offset_x = 375)
		elif self.state == est.estados_juego[2]:
			title = "SELECCIONAR NIVEL"
		else:
			title = ""

		if self.state == est.estados_juego[0]:
			buttons = self.buttons_main
		elif self.state == est.estados_juego[1]:
			buttons = [b for b in self.buttons_personaje if b.label == "" or b.label == "Jugar" or b.label == "Niveles"]
		elif self.state == est.estados_juego[2]:
			buttons = self.buttons_niveles
		else:
			buttons = []

		for button in buttons:
			button.draw_2d()

		glPopMatrix()
		glMatrixMode(GL_PROJECTION)
		glPopMatrix()
		glMatrixMode(GL_MODELVIEW)
		glEnable(GL_LIGHTING)


	def _draw_personajes_3d(self, width, height):
		preview_size = 250
		positions = [
			(-200, 80, self.kevin, "Kevin"),
			(0, 80, self.don_corru, "Don_corru"),
			(200, 80, self.kenny, "Kenny"),
		]
		
		for pos_x, pos_y, modelo, personaje_name in positions:
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
			glPushMatrix()
			
			es_seleccionado = est.personaje_sel == personaje_name
			if es_seleccionado:
				glRotatef(glutGet(GLUT_ELAPSED_TIME) / 20, 0, 1, 0)
				glClearColor(0.8, 0.8, 0.8, 1.0)
			else:
				glScalef(0.8, 0.8, 0.8)
				glClearColor(0.0, 0.0, 0.0, 1.0)
			modelo.draw(selected=es_seleccionado)
			glPopMatrix()
			glDisable(GL_DEPTH_TEST)
			glDisable(GL_LIGHTING)
			glPopMatrix()
			glMatrixMode(GL_PROJECTION)
			glPopMatrix()
			glMatrixMode(GL_MODELVIEW)

		glViewport(0, 0, width, height)
		glClearColor(0.0, 0.0, 0.0, 1.0)
	
	def _get_fondo_actual(self):
		if self.state != est.estados_juego[1]:
			return None
		if est.personaje_sel == "Kevin":
			return self.fondo_kevin
		if est.personaje_sel == "Don_corru":
			return self.fondo_doncorru
		if est.personaje_sel == "Kenny":
			return self.fondo_kenny

		return None

	def _draw_fondo(self, textura, width, height):
		glMatrixMode(GL_PROJECTION)
		glPushMatrix()
		glLoadIdentity()
		glOrtho(-width/2, width/2, -height/2, height/2, -1, 1)

		glMatrixMode(GL_MODELVIEW)
		glPushMatrix()
		glLoadIdentity()

		glDisable(GL_LIGHTING)
		glDisable(GL_DEPTH_TEST)
		glEnable(GL_TEXTURE_2D)
		glEnable(GL_BLEND)
		glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

		glBindTexture(GL_TEXTURE_2D, textura)
		glColor4f(1, 1, 1, 1)
		glBegin(GL_QUADS)
		glTexCoord2f(0, 0); glVertex2f(-width/2, -height/2)
		glTexCoord2f(1, 0); glVertex2f(width/2, -height/2)
		glTexCoord2f(1, 1); glVertex2f(width/2, height/2)
		glTexCoord2f(0, 1); glVertex2f(-width/2, height/2)
		glEnd()

		glBindTexture(GL_TEXTURE_2D, 0)
		glDisable(GL_TEXTURE_2D)
		glDisable(GL_BLEND)

		glPopMatrix()
		glMatrixMode(GL_PROJECTION)
		glPopMatrix()
		glMatrixMode(GL_MODELVIEW)

	def _draw_textura(self, textura, width, height, img_w, img_h, offset_y=0, offset_x=0):
		glMatrixMode(GL_PROJECTION)
		glPushMatrix()
		glLoadIdentity()
		glOrtho(-width/2, width/2, -height/2, height/2, -1, 1)

		glMatrixMode(GL_MODELVIEW)
		glPushMatrix()
		glLoadIdentity()

		glDisable(GL_LIGHTING)
		glDisable(GL_DEPTH_TEST)
		glEnable(GL_TEXTURE_2D)
		glEnable(GL_BLEND)
		glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

		glBindTexture(GL_TEXTURE_2D, textura)

		half_w = img_w / 2
		half_h = img_h / 2

		glBegin(GL_QUADS)
		glTexCoord2f(0, 0); glVertex2f(-half_w + offset_x, offset_y - half_h)
		glTexCoord2f(1, 0); glVertex2f(half_w + offset_x, offset_y - half_h)
		glTexCoord2f(1, 1); glVertex2f(half_w + offset_x, offset_y + half_h)
		glTexCoord2f(0, 1); glVertex2f(-half_w + offset_x, offset_y + half_h)
		glEnd()

		glBindTexture(GL_TEXTURE_2D, 0)
		glDisable(GL_TEXTURE_2D)
		glDisable(GL_BLEND)

		glPopMatrix()
		glMatrixMode(GL_PROJECTION)
		glPopMatrix()
		glMatrixMode(GL_MODELVIEW)
