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
	if est.estado_pers[0] == est.estados_pers[1]: #Caminando
		paso_pct = 0.05
		paso_pos = 5
		signo = _sign(est.caminando_pct)
		if abs(est.caminando_pct) <= 0.09:
			if est.posicion_pers_sel == 0 :
				est.posiciones_pers[est.posicion_pers_sel][0] = 0
				est.posiciones_pers[-1][0] = 0
				est.posiciones_pers[1][0] = 0
			else:
				est.posiciones_pers[est.posicion_pers_sel][0] = paso_pos * signo
				est.posiciones_pers[0][0] = paso_pos * signo
			est.estado_pers[0] = est.estados_pers[0]
			est.caminando_pct = 0
			pers_args.cambiar_estado(0)
			return
		est.posiciones_pers[est.posicion_pers_sel][0] += paso_pct * signo * paso_pos
		est.caminando_pct -= paso_pct * signo
		if est.personaje_sel == "Aqui le pudieran mover" or True:
			pers_args.caminando = 20 * math.sin(glutGet(GLUT_ELAPSED_TIME) / 200.0)
	if est.estado_pers[0] == est.estados_pers[2]: #Brazos
		if pers_args.brazos < 180:
			pers_args.brazos = min(180, glutGet(GLUT_ELAPSED_TIME) / 50)
		else:
			pers_args.brazos = 180

def _sign(x):
	if x < 0:
		return -1
	elif x == 0:
		return 0
	else:
		return 1

def disco_agarrado():
	if pers_args.brazos_arriba and est.disco_agarrado:
		est.disco_agarrado.posicion = [est.posiciones_pers[est.posicion_pers_sel][0], est.posiciones_pers[est.posicion_pers_sel][1] + 1.7, est.posiciones_pers[est.posicion_pers_sel][2]]

def update(value):
	disco_agarrado()
	animacion()
	glutPostRedisplay()
	glutTimerFunc(16, update, 0)