# utils/audio.py
import pygame

class Audio():
	def __init__(self) -> None:
		pygame.mixer.init()
		self.canal_audio_sfx = pygame.mixer.Channel(0)
		self.canal_audio_musica = pygame.mixer.Channel(1)
		self.canal_audio_voz = pygame.mixer.Channel(2)

		self.canal_audio_musica.set_volume(0.4)
		self.canal_audio_sfx.set_volume(0.4)
		self.canal_audio_voz.set_volume(0.5)

		self.cancion_act = 0
	
		self.sonidos = [
			self.load("resources/audio/menu.mp3")
			,self.load("resources/audio/nivel_1.mp3")
			,self.load("resources/audio/nivel_2.mp3")
			,self.load("resources/audio/nivel_3.mp3")
			,self.load("resources/audio/win.mp3")
			,self.load("resources/audio/click.mp3")
			,self.load("resources/audio/game_over.mp3")
			,self.load("resources/audio/choose.mp3")
		]

		self.sonidos_narracion= [
			self.load("resources/audio/tutorial_voz.mp3")
		]

		self.musica_on(self.cancion_act)
	
	def load(self, name):
		try:
			return pygame.mixer.Sound(name)
		except Exception as e:
			print("Error cargando sonido", name, e)
			return None

	def sonido_corto(self, num:int):
		sonido = self.sonidos[num]
		sonido.set_volume(1) # type: ignore
		self.canal_audio_sfx.play(sonido) # type: ignore

	def toggle_musica(self):
		if self.canal_audio_musica.get_busy():
			self.musica_off()
		else:
			self.musica_on(self.cancion_act)
	
	def musica_on(self, cancion:int):
		self.cancion_act = cancion
		sonido = self.sonidos[cancion]
		sonido.set_volume(0.7)
		if cancion == 4 or cancion == 6:
			
			self.canal_audio_musica.play(sonido, loops=0)
		else:
			
			self.canal_audio_musica.play(sonido, loops=-1) 

	def play_narracion(self, num:int):
		audio = self.sonidos_narracion[num]
		self.canal_audio_voz.play(audio, loops=0)

	def stop_narracion(self):
		self.canal_audio_voz.stop()


	def musica_off(self):
		self.canal_audio_musica.stop()
		self.canal_audio_voz.stop()