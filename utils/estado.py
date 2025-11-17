from utils.audio import Audio

camera_x = 0.0
camera_y = 0.0
camera_z = 5
camera_angle_x = 0.0
camera_angle_y = 0.0

scene_bounds = {
    "x": (-40, 40),
    "y": (-2, 20),
    "z": (-60, 60)
}

texturas_escena = {"Piso": None
				, "Pared": None
				, "Techo":None }

objetos = {
	"don_corru": [[0, 0, 0], 1],
	"Esfera": [[4, 0, -4], 1],
	"Dodecaedro": [[0, 0, -4], 1],
	"Esfera2": [[-4, 0, 0], 1],
	"Tetera": [[-4, 0, -4], 1],
	"Torus": [[4, 0, 0], 1]
}

audio:Audio

# colision = [False, None]

mouse_hover_area = [0, 0, 200, 200] # x_min, y_min, x_max, y_max

estados_juego = ["Menu", "Sel_pers", "Sel_nivel", "Nivel_1", "Nivel_2", "Nivel_3"]

personajes = ["Kevin", "Don_corru", "Kenny"]
personaje_sel = personajes[0]

niveles = {0:"Nivel_1", 1:"Nivel_2", 2:"Nivel_3"}
nivel_sel = 0

estados_don_corru = ["Estatico", "Caminando", "Brazos"]
estado_don_corru = [estados_don_corru[0], 0]	#estado, porcentaje
