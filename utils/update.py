import math
from OpenGL.GLUT import *	#type:ignore

from objetos.escena import Escena
import utils.estado as est
import objetos.pers_args as pers_args

_input_handler = None
_escena:Escena

def set_input_handler(input_handler, escena):
	global _input_handler, _escena
	_input_handler = input_handler
	_escena = escena

def bounding_sphere():
	personaje_data = est.objetos["Personaje"]
	pos_personaje, radius_personaje = personaje_data
	collision_detected = False
	for nombre_objeto, data_objeto in est.objetos.items():
		if nombre_objeto == "Personaje":
			continue
		pos_objeto, radius_objeto = data_objeto
		distancia_sq = (pos_personaje[0] - pos_objeto[0])**2 + (pos_personaje[2] - pos_objeto[2])**2
		suma_radios_sq = (radius_personaje + radius_objeto)**2
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
	if est.estado_personaje[0] == est.estados_personaje[0]: #Estatico
		return
	if est.estado_personaje[0] == est.estados_personaje[1]: #Caminando
		pers_args.caminando = 20 * math.sin(glutGet(GLUT_ELAPSED_TIME) / 200.0)
	if est.estado_personaje[0] == est.estados_personaje[2]: #Brazos
		return

def update(value):
	bounding_sphere()
	animacion()
	if _input_handler:
		_input_handler.process_continuous_input()
	glutPostRedisplay()
	glutTimerFunc(16, update, 0)