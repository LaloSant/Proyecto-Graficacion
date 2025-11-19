from typing import Optional
from utils.audio import Audio
from source.objetos.disco import Disco

camera_x = 0.0
camera_y = 0.0
camera_z = 15
camera_angle_x = 15
camera_angle_y = 0.0

scene_bounds = {
    "x": (-20, 40),
    "y": (-2, 20),
    "z": (-40, 60)
}

texturas_escena = {"Piso": None
				, "Pared": None
				, "Techo":None }

objetos = {
	"personaje": [[0, 0, 0], 1],
}

""" posiciones_pers = {
	-1: [-5, 0, -2],
	0: [0, 0, -2],
	1: [5, 0, -2]
} """
posiciones_pers = {
	-1: [0.0, 0, -2],
	0: [0.0, 0, -2],
	1: [0.0, 0, -2]
}

def rest_pos_pers():
	global posiciones_pers
	posiciones_pers = {
	-1: [0.0, 0, -2],
	0: [0.0, 0, -2],
	1: [0.0, 0, -2]
}

posicion_pers_sel = 0

posiciones_discos_y = (-1, -0.5, 0, 0.5)

piramides = {
	-1: [],
	0: [],
	1: []
}
discos:list[Disco] = []
disco_agarrado:Disco = None # type: ignore

audio:Audio

# Contador total de movimientos de discos
total_movimientos_discos = 0

# Variable para indicar si el juego está completado
juego_completado = False

estados_juego = ["Menu", "Sel_pers", "Sel_nivel", "Nivel_1", "Nivel_2", "Nivel_3"]

personajes = ["Kevin", "Don_corru", "Kenny"]
personaje_sel = personajes[0]

niveles = {0:"Nivel_1", 1:"Nivel_2", 2:"Nivel_3"}
nivel_sel = 0

estados_pers = ["Estatico", "Caminando", "Brazos"]
caminando_pct = 0
estado_pers = [estados_pers[0], 0]	#estado, porcentaje

