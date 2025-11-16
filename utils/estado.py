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
	"Personaje": [[0, 0, 0], 1],
	"Esfera": [[4, 0, -4], 1],
	"Dodecaedro": [[0, 0, -4], 1],
	"Esfera2": [[-4, 0, 0], 1],
	"Tetera": [[-4, 0, -4], 1],
	"Torus": [[4, 0, 0], 1]
}

audio:Audio

colision = [False, None]

aabb_dimensions = {
    "Personaje": [0.84, 2.98, 2.0], # width, height, depth
    "Esfera": [2.0, 2.0, 2.0],
    "Dodecaedro": [2.0, 2.0, 2.0],
	
}

mouse_hover_area = [0, 0, 200, 200] # x_min, y_min, x_max, y_max

estados_personaje = ["Estatico", "Caminando", "Brazos"]
estado_personaje = [estados_personaje[0], 0]	#estado, porcentaje
