# utils/juego.py
import utils.estado as est
from source.objetos.disco import Disco

def agarrar_disco():
	if len(est.piramides[est.posicion_pers_sel]) == 0:
		return False
	est.disco_agarrado = est.piramides[est.posicion_pers_sel].pop()
	est.audio.sonido_corto(5)
	return True

def poner_disco():
	long = len(est.piramides[est.posicion_pers_sel])
	if not posicion_valida():
		return False
	disco = est.disco_agarrado
	est.disco_agarrado = None
	disco.posicion = [disco.posicion[0], est.posiciones_discos_y[long], 0]
	est.piramides[est.posicion_pers_sel].append(disco)
	est.audio.sonido_corto(5)
	return True

def posicion_valida():
	leng = len(est.piramides[est.posicion_pers_sel])
	if leng == 0:
		return True
	disco_peek = est.piramides[est.posicion_pers_sel][leng - 1]
	disco = est.disco_agarrado
	return not disco.tamanio > disco_peek.tamanio

def verificar_victoria():
	if len(est.discos) == 0:
		return False
	if len(est.piramides[1]) != len(est.discos):
		return False
	for i in range(len(est.discos)):
		expected = len(est.discos) - i
		if est.piramides[1][i].tamanio != expected:
			return False
	return True

class Nivel():
	def __init__(self) -> None:
		self.movimientos_optimos = 0
	
	def reiniciar(self):
		pass

	def calcular_clasificacion(self, result:float):
		if result > 100:
			return "HACKEEEERRR"
		elif result > 90 and result <= 100:
			return "PROFESIONAL"
		elif result > 80 and result <= 90:
			return "BUEN JUGADOR"
		elif result > 70 and result <= 80:
			return "APRENDIZ"
		elif result <= 70:
			return "PODEMOS MEJORAR"

class Nivel1(Nivel):
	def __init__(self) -> None:
		self.movimientos_optimos = 11

	def reiniciar(self):
		est.audio.musica_on(1)
		est.discos = [Disco(1)
						,Disco(2)
						,Disco(3)
				]
		est.posicion_pers_sel = 0
		est.rest_pos_pers()
		est.total_movimientos_discos = 0
		est.piramides[-1].clear()
		est.piramides[0].clear()
		est.piramides[1].clear()
		est.piramides[-1].append(est.discos[2])
		est.piramides[-1].append(est.discos[1])
		est.piramides[-1].append(est.discos[0])
		est.discos[0].posicion = [-5, est.posiciones_discos_y[2], 0]
		est.discos[1].posicion = [-5, est.posiciones_discos_y[1], 0]
		est.discos[2].posicion = [-5, est.posiciones_discos_y[0], 0]

class Nivel2(Nivel):
	def __init__(self) -> None:
		self.movimientos_optimos = 11
	
	def reiniciar(self):
		est.audio.musica_on(2)
		est.discos = [Disco(1)
						,Disco(2)
						,Disco(3)
				]
		est.posicion_pers_sel = 0
		est.rest_pos_pers()
		est.total_movimientos_discos = 0
		est.piramides[-1].clear()
		est.piramides[0].clear()
		est.piramides[1].clear()
		est.piramides[-1].append(est.discos[2])
		est.piramides[-1].append(est.discos[1])
		est.piramides[-1].append(est.discos[0])
		est.discos[0].posicion = [-5, est.posiciones_discos_y[2], 0]
		est.discos[1].posicion = [-5, est.posiciones_discos_y[1], 0]
		est.discos[2].posicion = [-5, est.posiciones_discos_y[0], 0]


class Nivel3(Nivel):
	def __init__(self) -> None:
		self.movimientos_optimos = 31
	
	def reiniciar(self):
		est.audio.musica_on(3)
		est.discos = [Disco(1)
						,Disco(2)
						,Disco(3)
						,Disco(4)
				]
		est.posicion_pers_sel = 0
		est.rest_pos_pers()
		est.total_movimientos_discos = 0
		est.piramides[-1].clear()
		est.piramides[0].clear()
		est.piramides[1].clear()
		est.piramides[-1].append(est.discos[3])
		est.piramides[-1].append(est.discos[2])
		est.piramides[-1].append(est.discos[1])
		est.piramides[-1].append(est.discos[0])
		est.discos[0].posicion = [-5, est.posiciones_discos_y[3], 0]
		est.discos[1].posicion = [-5, est.posiciones_discos_y[2], 0]
		est.discos[2].posicion = [-5, est.posiciones_discos_y[1], 0]
		est.discos[3].posicion = [-5, est.posiciones_discos_y[0], 0]