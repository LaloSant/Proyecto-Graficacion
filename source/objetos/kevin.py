# source/objetos/kevin.py
from OpenGL.GL import *        # type: ignore
from OpenGL.GLUT import *      # type: ignore
from OpenGL.GLU import *       # type: ignore
from source.objetos.objeto import Objeto    # type: ignore
import utils.estado as est
import source.objetos.pers_args as pers_args

class Kevin(Objeto):

    def apagado(self, r, g, b):
        gris = (r + g + b) // 90
        r2 = int(r * 0.4 + gris * 0.6)
        g2 = int(g * 0.4 + gris * 0.6)
        b2 = int(b * 0.4 + gris * 0.6)
        return self.rgb(r2, g2, b2)

    def draw_head(self, selected=False):
        glPushMatrix()
        color = self.rgb(198, 136, 99) if selected else self.apagado(198, 136, 99)
        self.set_material_properties(color)
        glTranslatef(0, 1.4, 0)
        glScalef(1, 1, 0.8)
        glutSolidCube(1.0)
        glPopMatrix()

    def draw_horns(self):
        for dx in [-0.5, 0.5]:
            glPushMatrix()
            # Cuernos siempre negros
            self.set_material_properties(self.rgb(0, 0, 0))
            glTranslatef(dx, 1.8, 0)
            glScalef(0.25, 0.9, 0.25)
            glutSolidCube(0.5)
            glPopMatrix()

    def draw_eyes(self, selected):
        # Derecha
        glPushMatrix()
        glTranslatef(-0.3, 1.6, 0.41)
        color = self.rgb(255, 0, 0) if selected else self.apagado(255, 0, 0)
        self.set_material_properties(color)
        glutSolidCube(0.1)
        glPopMatrix()

        # Izquierda
        glPushMatrix()
        glTranslatef(0.3, 1.6, 0.41)
        color = self.rgb(255, 0, 0) if selected else self.apagado(255, 0, 0)
        self.set_material_properties(color)
        glutSolidCube(0.1)
        glPopMatrix()

    def draw_mouth(self, selected):
        glPushMatrix()
        glTranslatef(0, 1.2, 0.41)
        color = self.rgb(51, 51, 51) if selected else self.apagado(51, 51, 51)
        self.set_material_properties(color)
        glScalef(0.6, 0.25, 0.1)
        glutSolidCube(1.0)
        glPopMatrix()

    def draw_body(self):
        glPushMatrix()
        self.set_material_properties(self.rgb(0, 0, 0))
        glTranslatef(0, 0, 0)
        glScalef(1.6, 1.8, .6)
        glutSolidCube(1.0)
        glPopMatrix()

    def draw_arms(self, selected):
        arm_color = self.rgb(198, 136, 99) if selected else self.apagado(198, 136, 99)

        # Brazo derecho
        glPushMatrix()
        self.set_material_properties(arm_color)
        if pers_args.brazos_arriba:
            glRotatef(180, 0, 0, 1)
            glTranslatef(1.0, -0.8, 0)
        else:
            glTranslatef(-1.0, 0.9, 0)
            glRotatef(-pers_args.caminando, 1, 0, 0)
        glTranslatef(0, -0.6, 0)
        glScalef(.4, 1.2, .3)
        glutSolidCube(1.0)
        glPopMatrix()

        # Brazo izquierdo
        glPushMatrix()
        self.set_material_properties(arm_color)
        if pers_args.brazos_arriba:
            glRotatef(180, 0, 0, 1)
            glTranslatef(-1.0, -0.8, 0)
        else:
            glTranslatef(1.0, 0.9, 0)
            glRotatef(pers_args.caminando, 1, 0, 0)
        glTranslatef(0, -0.6, 0)
        glScalef(.4, 1.2, .3)
        glutSolidCube(1.0)
        glPopMatrix()

    def draw_legs(self, selected):
        leg_color = self.rgb(127, 127, 127) if selected else self.apagado(127, 127, 127)

        # Izquierda
        glPushMatrix()
        self.set_material_properties(leg_color)
        glRotatef(pers_args.caminando, 1, 0, 0)
        glTranslatef(-.5, -1.4, 0)
        glScalef(.5, 1.5, .5)
        glutSolidCube(1.0)
        glPopMatrix()

        # Derecha
        glPushMatrix()
        self.set_material_properties(leg_color)
        glRotatef(-pers_args.caminando, 1, 0, 0)
        glTranslatef(.5, -1.4, 0)
        glScalef(.5, 1.5, .5)
        glutSolidCube(1.0)
        glPopMatrix()
        
    def draw(self, selected=False):
        glPushMatrix()
        glScalef(0.8, 0.8, 0.8)
        self.draw_body()
        self.draw_head(selected)
        self.draw_horns()
        self.draw_eyes(selected)
        self.draw_mouth(selected)
        self.draw_arms(selected)
        self.draw_legs(selected)
        glPopMatrix()
