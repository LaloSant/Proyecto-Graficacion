import pygame

class Audio():

	def __init__(self) -> None:
		pygame.mixer.init()
		self.canal_audio_sfx = pygame.mixer.Channel(0)
		self.canal_audio_musica = pygame.mixer.Channel(1)
		self.musica_on()

	def init_audio(self):
		self.musica_on()
	
	def load(self, name):
		try:
			return pygame.mixer.Sound(name)
		except Exception as e:
			print("Error cargando sonido", name, e)
			return None

	def sonido_corto(self, num:int):
		sonido = pygame.mixer.Sound("")
		sonido.set_volume(1)
		self.canal_audio_sfx.play(sonido)

	def toggle_musica(self):
		if self.canal_audio_musica.get_busy():
			self.musica_off()
		else:
			self.musica_on()
	
	def musica_on(self):
		sonido = pygame.mixer.Sound("resources/audio/musica.mp3")
		sonido.set_volume(1)
		self.canal_audio_musica.play(sonido, loops=-1)

	def musica_off(self):
		self.canal_audio_musica.stop()