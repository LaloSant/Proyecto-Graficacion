# source/objetos/kenny.py
from OpenGL.GL import *     # type: ignore
from OpenGL.GLU import *    # type: ignore
from OpenGL.GLUT import *   # type: ignore
import math
from source.objetos.objeto import Objeto
import utils.estado as est
import source.objetos.pers_args as pers_args

class Kenny(Objeto):

    def apagado(self, r, g, b):
        gris = (r + g + b) // 90
        r2 = int(r * 0.4 + gris * 0.6)
        g2 = int(g * 0.4 + gris * 0.6)
        b2 = int(b * 0.4 + gris * 0.6)
        return self.rgb(r2, g2, b2)

    def draw_hat(self, selected): 
        glPushMatrix()
        glTranslatef(0.45, 1.2, 0)
        glScalef(1.25, 0.4, 1.1)
        if selected:
            self.set_material_properties(self.rgb(255, 0, 0))
        else:
            self.set_material_properties(self.apagado(255, 0, 0))
        glutSolidCube(1.0)
        glPopMatrix()

        glPushMatrix()
        glTranslatef(0.45, 1, 0.5)
        glScalef(1.25, 0.05, 1)
        if selected:
            self.set_material_properties(self.rgb(255, 0, 0))
        else:
            self.set_material_properties(self.apagado(255, 0, 0))
        glutSolidCube(1.0)
        glPopMatrix()

    def draw_head(self, selected):
        glPushMatrix()
        glTranslatef(0.45, 0.65, 0)
        if selected:
            self.set_material_properties(self.rgb(255, 222, 201))
        else:
            self.set_material_properties(self.apagado(255, 222, 201))
        glutSolidCube(1.0)
        glPopMatrix()

    def draw_eyes(self, selected):
        glPushMatrix()
        glTranslatef(0.45, 0.65, 0)

        eye_x_offset = 0.15
        eye_y_offset = 0.0
        eye_z_pos = 0.5 + 0.025

        active = False
        scale_factor = 3.0 if active else 1.0
        sx = 0.05 * scale_factor
        sy = 0.25 * scale_factor
        sz = 0.05 * scale_factor

        if selected:
            self.set_material_properties(self.rgb(0, 0, 0))
        else:
            self.set_material_properties(self.apagado(0, 0, 0))

        # Ojo izquierdo
        glPushMatrix()
        glTranslatef(-eye_x_offset, eye_y_offset, eye_z_pos)
        glScalef(sx, sy, sz)
        glutSolidCube(1.0)
        glPopMatrix()

        # Ojo derecho
        glPushMatrix()
        glTranslatef(eye_x_offset, eye_y_offset, eye_z_pos)
        glScalef(sx, sy, sz)
        glutSolidCube(1.0)
        glPopMatrix()
        glPopMatrix()

    def draw_body(self, selected):
        glPushMatrix()
        glTranslatef(0.45, -0.56, 0)
        glScalef(1.25, 1.5, 0.75)
        if selected:
            self.set_material_properties(self.rgb(0, 0, 255))
        else:
            self.set_material_properties(self.apagado(0, 0, 255))
        glutSolidCube(1.0)
        glPopMatrix()

    def draw_arms(self, selected):
        # Brazo derecho - manga
        glPushMatrix()
        if selected:
            self.set_material_properties(self.rgb(0, 0, 255))
        else:
            self.set_material_properties(self.apagado(0, 0, 255))
        glRotatef(pers_args.caminando, 1, 0, 0)
        glTranslatef(1.2, 0, 0)
        glutSolidCube(0.25)
        glPopMatrix()

        # brazo
        glPushMatrix()
        if selected:
            self.set_material_properties(self.rgb(255, 0, 0))
        else:
            self.set_material_properties(self.apagado(255, 0, 0))
        if pers_args.brazos_arriba:
            glRotatef(180, 0, 0, 1)
            glTranslatef(-0.9, 0, 0)
        else:
            glRotatef(pers_args.caminando, 1, 0, 0)
        glTranslatef(1.2, -0.5 , 0)
        glScalef(0.25, 0.8, 0.25)
        glutSolidCube(1)
        glPopMatrix()

        # mano
        glPushMatrix()
        if selected:
            self.set_material_properties(self.rgb(255, 222, 201))
        else:
            self.set_material_properties(self.apagado(255, 222, 201))
        if pers_args.brazos_arriba:
            glRotatef(180, 0, 0, 1)
            glTranslatef(-0.9, 0, 0)
        else:
            glRotatef(pers_args.caminando, 1, 0, 0)
        glTranslatef(1.2, -1 , 0)
        glutSolidCube(0.25)
        glPopMatrix()

        # Brazo izquierdo - manga
        glPushMatrix()
        if selected:
            self.set_material_properties(self.rgb(1, 0, 255))
        else:
            self.set_material_properties(self.apagado(1, 0, 255))
        glRotatef(-pers_args.caminando, 1, 0, 0)
        glTranslatef(-0.3, 0, 0)
        glutSolidCube(0.25)
        glPopMatrix()

        # brazo
        glPushMatrix()
        if selected:
            self.set_material_properties(self.rgb(255, 0, 0))
        else:
            self.set_material_properties(self.apagado(255, 0, 0))
        if pers_args.brazos_arriba:
            glRotatef(180, 0, 0, 1)
            glTranslatef(-0.9, 0, 0)
        else:
            glRotatef(-pers_args.caminando, 1, 0, 0)
        glTranslatef(-0.3, -0.5, 0)
        glScalef(0.25, 0.8, 0.25)
        glutSolidCube(1)
        glPopMatrix()

        # mano
        glPushMatrix()
        if selected:
            self.set_material_properties(self.rgb(255, 222, 201))
        else:
            self.set_material_properties(self.apagado(255, 222, 201))
        if pers_args.brazos_arriba:
            glRotatef(180, 0, 0, 1)
            glTranslatef(-0.9, 0, 0)
        else:
            glRotatef(-pers_args.caminando, 1, 0, 0)
        glTranslatef(-0.3, -1, 0)
        glutSolidCube(0.25)
        glPopMatrix()

    def draw_legs(self, selected):
        # Pierna izquierda
        glPushMatrix()
        if selected:
            self.set_material_properties(self.rgb(255, 255, 255))
        else:
            self.set_material_properties(self.apagado(255, 255, 255))
        glRotatef(pers_args.caminando, 1, 0, 0)
        glTranslatef(0 , -1.59, 0)
        glScalef(0.3, 0.5, 0.3)
        glutSolidCube(1.0)
        glPopMatrix()

        # Pierna derecha
        glPushMatrix()
        if selected:
            self.set_material_properties(self.rgb(255, 255, 255))
        else:
            self.set_material_properties(self.apagado(255, 255, 255))
        glRotatef(-pers_args.caminando, 1, 0, 0)
        glTranslatef(0.9  , -1.59, 0)
        glScalef(0.3, 0.5, 0.3)
        glutSolidCube(1.0)
        glPopMatrix()

        # Pie izquierdo
        glPushMatrix()
        if selected:
            self.set_material_properties(self.rgb(0, 0, 0))
        else:
            self.set_material_properties(self.apagado(0, 0, 0))
        glRotatef(pers_args.caminando, 1, 0, 0)
        glTranslatef(0  , -2, 0)
        glRotatef(-90, 1, 0, 0)
        glutSolidCube(0.3)
        glPopMatrix()

        # Pie derecho
        glPushMatrix()
        if selected:
            self.set_material_properties(self.rgb(0, 0, 0))
        else:
            self.set_material_properties(self.apagado(0, 0, 0))
        glRotatef(-pers_args.caminando, 1, 0, 0)
        glTranslatef(0.9, -2, 0)
        glRotatef(-90, 1, 0, 0)
        glutSolidCube(0.3)
        glPopMatrix()

    def draw(self, selected=False):
        glPushMatrix()
        glScalef(0.9, 0.9, 0.9)
        glTranslatef(-0.5, 0, 0)
        self.draw_body(selected)
        self.draw_hat(selected)
        self.draw_head(selected)
        self.draw_eyes(selected)
        self.draw_arms(selected)
        self.draw_legs(selected)
        glPopMatrix()
