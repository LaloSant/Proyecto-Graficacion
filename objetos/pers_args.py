import utils.estado as est

#-30 grados
caminando = 0 

def cambiar_estado(num):
	global caminando
	if num == 0:
		caminando = 0
	est.estado_personaje[0] = est.estados_personaje[num]