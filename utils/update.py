import math
from OpenGL.GLUT import *	#type:ignore

from source.escenas.escena import Escena
import utils.estado as est
import source.objetos.pers_args as pers_args

_input_handler = None
_escena:Escena

def set_input_handler(input_handler, escena):
	global _input_handler, _escena
	_input_handler = input_handler
	_escena = escena

def bounding_sphere():
	don_corru_data = est.objetos["don_corru"]
	pos_don_corru, radius_don_corru = don_corru_data
	collision_detected = False
	for nombre_objeto, data_objeto in est.objetos.items():
		if nombre_objeto == "don_corru":
			continue
		pos_objeto, radius_objeto = data_objeto
		distancia_sq = (pos_don_corru[0] - pos_objeto[0])**2 + (pos_don_corru[2] - pos_objeto[2])**2
		suma_radios_sq = (radius_don_corru + radius_objeto)**2
		if distancia_sq <= suma_radios_sq:
			collision_detected = True
			break
	if collision_detected:
		_escena.set_escenario(1)
		pers_args.cambiar_estado(0)
	else:
		_escena.set_escenario(0)
		pers_args.cambiar_estado(1)

def animacion():
	if est.estado_don_corru[0] == est.estados_don_corru[0]: #Estatico
		return
	if est.estado_don_corru[0] == est.estados_don_corru[1]: #Caminando
		pers_args.caminando = 20 * math.sin(glutGet(GLUT_ELAPSED_TIME) / 200.0)
	if est.estado_don_corru[0] == est.estados_don_corru[2]: #Brazos
		return

def update(value):
	animacion()
	glutPostRedisplay()
	glutTimerFunc(16, update, 0)