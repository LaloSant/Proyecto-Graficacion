# source/objetos/don_corru.py
from OpenGL.GL import *        # type: ignore
from OpenGL.GLUT import *      # type: ignore
from OpenGL.GLU import *        # type: ignore

from source.objetos.objeto import Objeto    # type: ignore
import utils.estado as est
import source.objetos.pers_args as pers_args

class DonCorru(Objeto):

    def apagado(self, r, g, b):
        gris = (r + g + b) // 90
        r2 = int(r * 0.4 + gris * 0.6)
        g2 = int(g * 0.4 + gris * 0.6)
        b2 = int(b * 0.4 + gris * 0.6)
        return self.rgb(r2, g2, b2)

    def draw(self, selected=False):
        glPushMatrix()
        glScalef(1.1, 1.1, 1.1)
        glRotatef(-90, 0, 1, 0)
        self.dibuja_torso(selected)
        self.dibuja_cabeza(selected)
        self.dibuja_piernas(selected)
        self.dibuja_brazos(selected)
        self.dibuja_sombrero(selected)
        glPopMatrix()

    def dibuja_torso(self, selected):
        glPushMatrix()
        color = self.rgb(181, 23, 35) if selected else self.apagado(181, 23, 35)
        self.set_material_properties(color)
        glScalef(0.42, 1.13, 1)
        glutSolidCube(1)
        glPopMatrix()

    def dibuja_cabeza(self, selected):
        glPushMatrix()
        color = self.rgb(176, 149, 116) if selected else self.apagado(176, 149, 116)
        self.set_material_properties(color)
        glScalef(0.5, 0.5, 0.46)
        glTranslate(0, 1.6, 0)
        glutSolidCube(1)
        self.dibuja_cara(selected)
        glPopMatrix()

    def dibuja_cara(self, selected):
        # OJOS (siempre negros)
        glPushMatrix()
        self.set_material_properties(self.rgb(0, 0, 0))
        glScalef(0.2, 0.2, 0.15)
        glTranslate(2.3, 0.8, -1.8)
        glutSolidCube(1)
        glPopMatrix()

        glPushMatrix()
        self.set_material_properties(self.rgb(0, 0, 0))
        glScalef(0.2, 0.2, 0.15)
        glTranslate(2.3, 0.8, 1.8)
        glutSolidCube(1)
        glPopMatrix()

        # BOCA
        glPushMatrix()
        color = self.rgb(255, 255, 255) if selected else self.apagado(255, 255, 255)
        self.set_material_properties(color)

        rotacion = 10 if est.estado_pers[0] == est.estados_pers[0] else -10
        glRotatef(rotacion, 1, 0, 0)
        glScalef(0.2, 0.15, 0.8)
        glTranslate(2.3, -1.2, 0)
        glutSolidCube(1)
        glPopMatrix()

    def dibuja_piernas(self, selected):
        glPushMatrix()
        color = self.rgb(23, 23, 23) if selected else self.apagado(23, 23, 23)
        self.set_material_properties(color)

        glRotatef(pers_args.caminando, 0, 0, 1)
        glScalef(0.2, 0.66, 0.23)
        glTranslate(0, -1.2, 1)
        glutSolidCube(1)
        glPopMatrix()

        glPushMatrix()
        color = self.rgb(23, 23, 23) if selected else self.apagado(23, 23, 23)
        self.set_material_properties(color)

        glRotatef(-pers_args.caminando, 0, 0, 1)
        glScalef(0.2, 0.66, 0.23)
        glTranslate(0, -1.2, -1)
        glutSolidCube(1)
        glPopMatrix()

    def dibuja_brazos(self, selected):
        glPushMatrix()
        glTranslatef(0, 1, 0)

        brazo_color = self.rgb(176, 149, 116) if selected else self.apagado(176, 149, 116)

        # BRAZO DERECHO
        glPushMatrix()
        self.set_material_properties(brazo_color)
        if pers_args.brazos_arriba:
            glRotatef(180, 0, 0, 1)
            glTranslatef(0, 1.2, 0)
        else:
            glRotatef(-pers_args.caminando, 0, 0, 1)
        glScalef(0.2, 0.66, 0.23)
        glTranslate(0, -1.4, 2.7)
        glutSolidCube(1)
        glPopMatrix()

        # BRAZO IZQUIERDO
        glPushMatrix()
        self.set_material_properties(brazo_color)
        if pers_args.brazos_arriba:
            glRotatef(180, 0, 0, 1)
            glTranslatef(0, 1.2, 0)
        else:
            glRotatef(pers_args.caminando, 0, 0, 1)
        glScalef(0.2, 0.66, 0.23)
        glTranslate(0, -1.4, -2.7)
        glutSolidCube(1)
        glPopMatrix()

        glPopMatrix()

    def dibuja_sombrero(self, selected):
        sombrero_color = self.rgb(75, 44, 15) if selected else self.apagado(75, 44, 15)

        # ALA
        glPushMatrix()
        self.set_material_properties(sombrero_color)
        glScalef(0.98, 0.15, 0.98)
        glTranslate(0, 7.5, 0)
        glutSolidCube(1)
        glPopMatrix()

        # PARTE SUPERIOR
        glPushMatrix()
        self.set_material_properties(sombrero_color)
        glScalef(0.46, 0.26, 0.46)
        glTranslate(0, 5, 0)
        glutSolidCube(1)
        glPopMatrix()
