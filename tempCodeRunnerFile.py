from OpenGL.GL import *		# type: ignore
from OpenGL.GLUT import *	# type: ignore
from OpenGL.GLU import *	# type: ignore
import math

from utils.lighting import LightingManager
from utils.input_handler import InputHandler
from utils.texturas import load_texture
from utils.audio import Audio
from utils.juego import *
import utils.estado as est
import utils.update as updt

from source.objetos.don_corru import DonCorru
from source.objetos.kevin import Kevin
from source.objetos.kenny import Kenny
from source.objetos.base_piramide import BasePiramide
from source.objetos.disco import Disco
from source.escenas.escena import Escena
from source.escenas.menu import Menu