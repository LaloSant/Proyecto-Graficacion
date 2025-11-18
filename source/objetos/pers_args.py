import utils.estado as est

#-30 grados
caminando = 0 
brazos = 0

brazos_arriba = False

def cambiar_estado(num):
	global caminando
	global brazos
	if num == 0:
		caminando = 0
		brazos = 0
	elif num == 2:
		brazos = 180
	est.estado_pers[0] = est.estados_pers[num]
