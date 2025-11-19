import utils.estado as est
from source.objetos.disco import Disco

def agarrar_disco():
	if len(est.piramides[est.posicion_pers_sel]) == 0:
		return False
	est.disco_agarrado = est.piramides[est.posicion_pers_sel].pop()
	return True

def poner_disco():
	long = len(est.piramides[est.posicion_pers_sel])
	if not posicion_valida():
		print("Nao, nao")
		return False
	
	disco = est.disco_agarrado
	est.disco_agarrado = None
	disco.posicion = [disco.posicion[0], est.posiciones_discos_y[long], 0]
	est.piramides[est.posicion_pers_sel].append(disco)
	return True

def posicion_valida():
	leng = len(est.piramides[est.posicion_pers_sel])
	if leng == 0:
		return True
	disco_peek = est.piramides[est.posicion_pers_sel][leng - 1]
	disco = est.disco_agarrado
	return not disco.tamanio > disco_peek.tamanio

def verificar_victoria():
	"""Verifica si la Torre de Hanoi está completa (todos los discos en la posición 1)"""
	if len(est.discos) == 0:
		return False
	if len(est.piramides[1]) != len(est.discos):
		return False
	# Verificar que todos los discos estén en orden correcto
	# El orden en la pila va de abajo (índice 0) a arriba (último índice).
	# El disco más grande tiene tamanio == len(est.discos) y debe estar abajo.
	for i in range(len(est.discos)):
		expected = len(est.discos) - i
		if est.piramides[1][i].tamanio != expected:
			return False
	return True


class Nivel2():
	def __init__(self) -> None:
		self.reiniciar()
	
	def reiniciar(self):
		est.discos = [Disco(1)
						,Disco(2)
						,Disco(3)
				]
		est.piramides[-1].clear()
		est.piramides[0].clear()
		est.piramides[1].clear()
		est.piramides[-1].append(est.discos[2])
		est.piramides[-1].append(est.discos[1])
		est.piramides[-1].append(est.discos[0])
		est.discos[0].posicion = [-5, est.posiciones_discos_y[2], 0]
		est.discos[1].posicion = [-5, est.posiciones_discos_y[1], 0]
		est.discos[2].posicion = [-5, est.posiciones_discos_y[0], 0]

class Nivel1():
	def __init__(self) -> None:
		self.reiniciar()
	
	def reiniciar(self):
		est.discos = [Disco(1)
					,Disco(2)
					,Disco(3)
				]
		est.piramides[-1].clear()
		est.piramides[0].clear()
		est.piramides[1].clear()
		est.piramides[-1].append(est.discos[2])
		est.piramides[-1].append(est.discos[1])
		est.piramides[-1].append(est.discos[0])
		est.discos[0].posicion = [-5, est.posiciones_discos_y[2], 0]
		est.discos[1].posicion = [-5, est.posiciones_discos_y[1], 0]
		est.discos[2].posicion = [-5, est.posiciones_discos_y[0], 0]

class Nivel3():
	def __init__(self) -> None:
		self.reiniciar()
	
	def reiniciar(self):
		est.discos = [Disco(1)
					,Disco(2)
					,Disco(3)
				]
		est.piramides[-1].clear()
		est.piramides[0].clear()
		est.piramides[1].clear()
		est.piramides[-1].append(est.discos[2])
		est.piramides[-1].append(est.discos[1])
		est.piramides[-1].append(est.discos[0])
		est.discos[0].posicion = [-5, est.posiciones_discos_y[2], 0]
		est.discos[1].posicion = [-5, est.posiciones_discos_y[1], 0]
		est.discos[2].posicion = [-5, est.posiciones_discos_y[0], 0]