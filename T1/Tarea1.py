# coding=utf-8
"""Dibujo de rectangulos que representan cielo y pasto"""

import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy as np
import easy_shaders as es
import basic_shapes as bs
from gpu_shape import GPUShape, SIZE_IN_BYTES

__author__ = "Daniel Calderon"
__license__ = "MIT"


# We will use 32 bits data, so floats and integers have 4 bytes
# 1 byte = 8 bits
SIZE_IN_BYTES = 4


# A class to store the application control
class Controller:
    fillPolygon = True


# we will use the global controller as communication with the callback function
controller = Controller()


def on_key(window, key, scancode, action, mods):

    if action != glfw.PRESS:
        return
    
    global controller

    if key == glfw.KEY_SPACE:
        controller.fillPolygon = not controller.fillPolygon

    elif key == glfw.KEY_ESCAPE:
        glfw.set_window_should_close(window, True)

    else:
        print('Unknown key')



#Método para crear los cuadrados del tablero declarando sus posiciones y colores en una matriz numpy, utilizando un ebo para ir leyendo las posiciones.

def createQuad():

    # Aquí se definen los indices y colores respectivos.
    vertexData = np.array([
    #   positions        colors
        #1er fila

        -0.1,  0.0, 0.0,  0.0, 0.0, 0.0,
         0.0,  0.0, 0.0,  0.0, 0.0, 0.0,
         0.0,  0.1, 0.0,  0.0, 0.0, 0.0,
        -0.1,  0.1, 0.0,  0.0, 0.0, 0.0,

         0.0,  0.0, 0.0,  1.0, 1.0, 1.0,
         0.1,  0.0, 0.0,  1.0, 1.0, 1.0,
         0.1,  0.1, 0.0,  1.0, 1.0, 1.0,
         0.0,  0.1, 0.0,  1.0, 1.0, 1.0,

         0.1,  0.0, 0.0,  0.0, 0.0, 0.0,
         0.2,  0.0, 0.0,  0.0, 0.0, 0.0,
         0.2,  0.1, 0.0,  0.0, 0.0, 0.0,
         0.1,  0.1, 0.0,  0.0, 0.0, 0.0,

         
         0.2,  0.0, 0.0,  1.0, 1.0, 1.0,
         0.3,  0.0, 0.0,  1.0, 1.0, 1.0,
         0.3,  0.1, 0.0,  1.0, 1.0, 1.0,
         0.2,  0.1, 0.0,  1.0, 1.0, 1.0,

         0.3,  0.0, 0.0,  0.0, 0.0, 0.0,
         0.4,  0.0, 0.0,  0.0, 0.0, 0.0,
         0.4,  0.1, 0.0,  0.0, 0.0, 0.0,
         0.3,  0.1, 0.0,  0.0, 0.0, 0.0,

         0.4,  0.0, 0.0,  1.0, 1.0, 1.0,
         0.5,  0.0, 0.0,  1.0, 1.0, 1.0,
         0.5,  0.1, 0.0,  1.0, 1.0, 1.0,
         0.4,  0.1, 0.0,  1.0, 1.0, 1.0,

         0.5,  0.0, 0.0,  0.0, 0.0, 0.0,
         0.6,  0.0, 0.0,  0.0, 0.0, 0.0,
         0.6,  0.1, 0.0,  0.0, 0.0, 0.0,
         0.5,  0.1, 0.0,  0.0, 0.0, 0.0,

         
         0.6,  0.0, 0.0,  1.0, 1.0, 1.0,
         0.7,  0.0, 0.0,  1.0, 1.0, 1.0,
         0.7,  0.1, 0.0,  1.0, 1.0, 1.0,
         0.6,  0.1, 0.0,  1.0, 1.0, 1.0,


        #2da fila

        -0.1, -0.1, 0.0,  1.0, 1.0, 1.0,
         0.0, -0.1, 0.0,  1.0, 1.0, 1.0,
         0.0,  0.0, 0.0,  1.0, 1.0, 1.0,
        -0.1,  0.0, 0.0,  1.0, 1.0, 1.0,

         0.0, -0.1, 0.0,  0.0, 0.0, 0.0,
         0.1, -0.1, 0.0,  0.0, 0.0, 0.0,
         0.1,  0.0, 0.0,  0.0, 0.0, 0.0,
         0.0,  0.0, 0.0,  0.0, 0.0, 0.0,

         0.1, -0.1, 0.0,  1.0, 1.0, 1.0,
         0.2, -0.1, 0.0,  1.0, 1.0, 1.0,
         0.2,  0.0, 0.0,  1.0, 1.0, 1.0,
         0.1,  0.0, 0.0,  1.0, 1.0, 1.0,

         0.2, -0.1, 0.0,  0.0, 0.0, 0.0,
         0.3, -0.1, 0.0,  0.0, 0.0, 0.0,
         0.3,  0.0, 0.0,  0.0, 0.0, 0.0,
         0.2,  0.0, 0.0,  0.0, 0.0, 0.0,

        
         0.3, -0.1, 0.0,  1.0, 1.0, 1.0,
         0.4, -0.1, 0.0,  1.0, 1.0, 1.0,
         0.4,  0.0, 0.0,  1.0, 1.0, 1.0,
         0.3,  0.0, 0.0,  1.0, 1.0, 1.0,

         0.4, -0.1, 0.0,  0.0, 0.0, 0.0,
         0.5, -0.1, 0.0,  0.0, 0.0, 0.0,
         0.5,  0.0, 0.0,  0.0, 0.0, 0.0,
         0.4,  0.0, 0.0,  0.0, 0.0, 0.0,

         0.5, -0.1, 0.0,  1.0, 1.0, 1.0,
         0.6, -0.1, 0.0,  1.0, 1.0, 1.0,
         0.6,  0.0, 0.0,  1.0, 1.0, 1.0,
         0.5,  0.0, 0.0,  1.0, 1.0, 1.0,

         0.6, -0.1, 0.0,  0.0, 0.0, 0.0,
         0.7, -0.1, 0.0,  0.0, 0.0, 0.0,
         0.7,  0.0, 0.0,  0.0, 0.0, 0.0,
         0.6,  0.0, 0.0,  0.0, 0.0, 0.0,
    
        #3era fila

        
        -0.1, -0.2, 0.0,  0.0, 0.0, 0.0,
         0.0, -0.2, 0.0,  0.0, 0.0, 0.0,
         0.0, -0.1, 0.0,  0.0, 0.0, 0.0,
        -0.1, -0.1, 0.0,  0.0, 0.0, 0.0,

         0.0, -0.2, 0.0,  1.0, 1.0, 1.0,
         0.1, -0.2, 0.0,  1.0, 1.0, 1.0,
         0.1, -0.1, 0.0,  1.0, 1.0, 1.0,
         0.0, -0.1, 0.0,  1.0, 1.0, 1.0,

         0.1, -0.2, 0.0,  0.0, 0.0, 0.0,
         0.2, -0.2, 0.0,  0.0, 0.0, 0.0,
         0.2, -0.1, 0.0,  0.0, 0.0, 0.0,
         0.1, -0.1, 0.0,  0.0, 0.0, 0.0,

         
         0.2, -0.2, 0.0,  1.0, 1.0, 1.0,
         0.3, -0.2, 0.0,  1.0, 1.0, 1.0,
         0.3, -0.1, 0.0,  1.0, 1.0, 1.0,
         0.2, -0.1, 0.0,  1.0, 1.0, 1.0,

         0.3, -0.2, 0.0,  0.0, 0.0, 0.0,
         0.4, -0.2, 0.0,  0.0, 0.0, 0.0,
         0.4, -0.1, 0.0,  0.0, 0.0, 0.0,
         0.3, -0.1, 0.0,  0.0, 0.0, 0.0,

         0.4, -0.2, 0.0,  1.0, 1.0, 1.0,
         0.5, -0.2, 0.0,  1.0, 1.0, 1.0,
         0.5, -0.1, 0.0,  1.0, 1.0, 1.0,
         0.4, -0.1, 0.0,  1.0, 1.0, 1.0,

         0.5, -0.2, 0.0,  0.0, 0.0, 0.0,
         0.6, -0.2, 0.0,  0.0, 0.0, 0.0,
         0.6, -0.1, 0.0,  0.0, 0.0, 0.0,
         0.5, -0.1, 0.0,  0.0, 0.0, 0.0,

         
         0.6, -0.2, 0.0,  1.0, 1.0, 1.0,
         0.7, -0.2, 0.0,  1.0, 1.0, 1.0,
         0.7, -0.1, 0.0,  1.0, 1.0, 1.0,
         0.6, -0.1, 0.0,  1.0, 1.0, 1.0,


        #4ta fila

        -0.1, -0.3, 0.0,  1.0, 1.0, 1.0,
         0.0, -0.3, 0.0,  1.0, 1.0, 1.0,
         0.0, -0.2, 0.0,  1.0, 1.0, 1.0,
        -0.1, -0.2, 0.0,  1.0, 1.0, 1.0,

         0.0, -0.3, 0.0,  0.0, 0.0, 0.0,
         0.1, -0.3, 0.0,  0.0, 0.0, 0.0,
         0.1, -0.2, 0.0,  0.0, 0.0, 0.0,
         0.0, -0.2, 0.0,  0.0, 0.0, 0.0,

         0.1, -0.3, 0.0,  1.0, 1.0, 1.0,
         0.2, -0.3, 0.0,  1.0, 1.0, 1.0,
         0.2, -0.2, 0.0,  1.0, 1.0, 1.0,
         0.1, -0.2, 0.0,  1.0, 1.0, 1.0,

         0.2, -0.3, 0.0,  0.0, 0.0, 0.0,
         0.3, -0.3, 0.0,  0.0, 0.0, 0.0,
         0.3, -0.2, 0.0,  0.0, 0.0, 0.0,
         0.2, -0.2, 0.0,  0.0, 0.0, 0.0,

        
         0.3, -0.3, 0.0,  1.0, 1.0, 1.0,
         0.4, -0.3, 0.0,  1.0, 1.0, 1.0,
         0.4, -0.2, 0.0,  1.0, 1.0, 1.0,
         0.3, -0.2, 0.0,  1.0, 1.0, 1.0,

         0.4, -0.3, 0.0,  0.0, 0.0, 0.0,
         0.5, -0.3, 0.0,  0.0, 0.0, 0.0,
         0.5, -0.2, 0.0,  0.0, 0.0, 0.0,
         0.4, -0.2, 0.0,  0.0, 0.0, 0.0,

         0.5, -0.3, 0.0,  1.0, 1.0, 1.0,
         0.6, -0.3, 0.0,  1.0, 1.0, 1.0,
         0.6, -0.2, 0.0,  1.0, 1.0, 1.0,
         0.5, -0.2, 0.0,  1.0, 1.0, 1.0,

         0.6, -0.3, 0.0,  0.0, 0.0, 0.0,
         0.7, -0.3, 0.0,  0.0, 0.0, 0.0,
         0.7, -0.2, 0.0,  0.0, 0.0, 0.0,
         0.6, -0.2, 0.0,  0.0, 0.0, 0.0,


        #5ta fila

          
        -0.1, -0.4, 0.0,  0.0, 0.0, 0.0,
         0.0, -0.4, 0.0,  0.0, 0.0, 0.0,
         0.0, -0.3, 0.0,  0.0, 0.0, 0.0,
        -0.1, -0.3, 0.0,  0.0, 0.0, 0.0,

         0.0, -0.4, 0.0,  1.0, 1.0, 1.0,
         0.1, -0.4, 0.0,  1.0, 1.0, 1.0,
         0.1, -0.3, 0.0,  1.0, 1.0, 1.0,
         0.0, -0.3, 0.0,  1.0, 1.0, 1.0,

         0.1, -0.4, 0.0,  0.0, 0.0, 0.0,
         0.2, -0.4, 0.0,  0.0, 0.0, 0.0,
         0.2, -0.3, 0.0,  0.0, 0.0, 0.0,
         0.1, -0.3, 0.0,  0.0, 0.0, 0.0,

         
         0.2, -0.4, 0.0,  1.0, 1.0, 1.0,
         0.3, -0.4, 0.0,  1.0, 1.0, 1.0,
         0.3, -0.3, 0.0,  1.0, 1.0, 1.0,
         0.2, -0.3, 0.0,  1.0, 1.0, 1.0,

         0.3, -0.4, 0.0,  0.0, 0.0, 0.0,
         0.4, -0.4, 0.0,  0.0, 0.0, 0.0,
         0.4, -0.3, 0.0,  0.0, 0.0, 0.0,
         0.3, -0.3, 0.0,  0.0, 0.0, 0.0,

         0.4, -0.4, 0.0,  1.0, 1.0, 1.0,
         0.5, -0.4, 0.0,  1.0, 1.0, 1.0,
         0.5, -0.3, 0.0,  1.0, 1.0, 1.0,
         0.4, -0.3, 0.0,  1.0, 1.0, 1.0,

         0.5, -0.4, 0.0,  0.0, 0.0, 0.0,
         0.6, -0.4, 0.0,  0.0, 0.0, 0.0,
         0.6, -0.3, 0.0,  0.0, 0.0, 0.0,
         0.5, -0.3, 0.0,  0.0, 0.0, 0.0,

         
         0.6, -0.4, 0.0,  1.0, 1.0, 1.0,
         0.7, -0.4, 0.0,  1.0, 1.0, 1.0,
         0.7, -0.3, 0.0,  1.0, 1.0, 1.0,
         0.6, -0.3, 0.0,  1.0, 1.0, 1.0,


        #6xta fila

        -0.1, -0.5, 0.0,  1.0, 1.0, 1.0,
         0.0, -0.5, 0.0,  1.0, 1.0, 1.0,
         0.0, -0.4, 0.0,  1.0, 1.0, 1.0,
        -0.1, -0.4, 0.0,  1.0, 1.0, 1.0,

         0.0, -0.5, 0.0,  0.0, 0.0, 0.0,
         0.1, -0.5, 0.0,  0.0, 0.0, 0.0,
         0.1, -0.4, 0.0,  0.0, 0.0, 0.0,
         0.0, -0.4, 0.0,  0.0, 0.0, 0.0,

         0.1, -0.5, 0.0,  1.0, 1.0, 1.0,
         0.2, -0.5, 0.0,  1.0, 1.0, 1.0,
         0.2, -0.4, 0.0,  1.0, 1.0, 1.0,
         0.1, -0.4, 0.0,  1.0, 1.0, 1.0,

         0.2, -0.5, 0.0,  0.0, 0.0, 0.0,
         0.3, -0.5, 0.0,  0.0, 0.0, 0.0,
         0.3, -0.4, 0.0,  0.0, 0.0, 0.0,
         0.2, -0.4, 0.0,  0.0, 0.0, 0.0,

        
         0.3, -0.5, 0.0,  1.0, 1.0, 1.0,
         0.4, -0.5, 0.0,  1.0, 1.0, 1.0,
         0.4, -0.4, 0.0,  1.0, 1.0, 1.0,
         0.3, -0.4, 0.0,  1.0, 1.0, 1.0,

         0.4, -0.5, 0.0,  0.0, 0.0, 0.0,
         0.5, -0.5, 0.0,  0.0, 0.0, 0.0,
         0.5, -0.4, 0.0,  0.0, 0.0, 0.0,
         0.4, -0.4, 0.0,  0.0, 0.0, 0.0,

         0.5, -0.5, 0.0,  1.0, 1.0, 1.0,
         0.6, -0.5, 0.0,  1.0, 1.0, 1.0,
         0.6, -0.4, 0.0,  1.0, 1.0, 1.0,
         0.5, -0.4, 0.0,  1.0, 1.0, 1.0,

         0.6, -0.5, 0.0,  0.0, 0.0, 0.0,
         0.7, -0.5, 0.0,  0.0, 0.0, 0.0,
         0.7, -0.4, 0.0,  0.0, 0.0, 0.0,
         0.6, -0.4, 0.0,  0.0, 0.0, 0.0,



        #7ptima fila

        -0.1, -0.6, 0.0,  0.0, 0.0, 0.0,
         0.0, -0.6, 0.0,  0.0, 0.0, 0.0,
         0.0, -0.5, 0.0,  0.0, 0.0, 0.0,
        -0.1, -0.5, 0.0,  0.0, 0.0, 0.0,

         0.0, -0.6, 0.0,  1.0, 1.0, 1.0,
         0.1, -0.6, 0.0,  1.0, 1.0, 1.0,
         0.1, -0.5, 0.0,  1.0, 1.0, 1.0,
         0.0, -0.5, 0.0,  1.0, 1.0, 1.0,

         0.1, -0.6, 0.0,  0.0, 0.0, 0.0,
         0.2, -0.6, 0.0,  0.0, 0.0, 0.0,
         0.2, -0.5, 0.0,  0.0, 0.0, 0.0,
         0.1, -0.5, 0.0,  0.0, 0.0, 0.0,

         
         0.2, -0.6, 0.0,  1.0, 1.0, 1.0,
         0.3, -0.6, 0.0,  1.0, 1.0, 1.0,
         0.3, -0.5, 0.0,  1.0, 1.0, 1.0,
         0.2, -0.5, 0.0,  1.0, 1.0, 1.0,

         0.3, -0.6, 0.0,  0.0, 0.0, 0.0,
         0.4, -0.6, 0.0,  0.0, 0.0, 0.0,
         0.4, -0.5, 0.0,  0.0, 0.0, 0.0,
         0.3, -0.5, 0.0,  0.0, 0.0, 0.0,

         0.4, -0.6, 0.0,  1.0, 1.0, 1.0,
         0.5, -0.6, 0.0,  1.0, 1.0, 1.0,
         0.5, -0.5, 0.0,  1.0, 1.0, 1.0,
         0.4, -0.5, 0.0,  1.0, 1.0, 1.0,

         0.5, -0.6, 0.0,  0.0, 0.0, 0.0,
         0.6, -0.6, 0.0,  0.0, 0.0, 0.0,
         0.6, -0.5, 0.0,  0.0, 0.0, 0.0,
         0.5, -0.5, 0.0,  0.0, 0.0, 0.0,

         
         0.6, -0.6, 0.0,  1.0, 1.0, 1.0,
         0.7, -0.6, 0.0,  1.0, 1.0, 1.0,
         0.7, -0.5, 0.0,  1.0, 1.0, 1.0,
         0.6, -0.5, 0.0,  1.0, 1.0, 1.0,


        #8tava fila

        -0.1, -0.7, 0.0,  1.0, 1.0, 1.0,
         0.0, -0.7, 0.0,  1.0, 1.0, 1.0,
         0.0, -0.6, 0.0,  1.0, 1.0, 1.0,
        -0.1, -0.6, 0.0,  1.0, 1.0, 1.0,

         0.0, -0.7, 0.0,  0.0, 0.0, 0.0,
         0.1, -0.7, 0.0,  0.0, 0.0, 0.0,
         0.1, -0.6, 0.0,  0.0, 0.0, 0.0,
         0.0, -0.6, 0.0,  0.0, 0.0, 0.0,

         0.1, -0.7, 0.0,  1.0, 1.0, 1.0,
         0.2, -0.7, 0.0,  1.0, 1.0, 1.0,
         0.2, -0.6, 0.0,  1.0, 1.0, 1.0,
         0.1, -0.6, 0.0,  1.0, 1.0, 1.0,

         0.2, -0.7, 0.0,  0.0, 0.0, 0.0,
         0.3, -0.7, 0.0,  0.0, 0.0, 0.0,
         0.3, -0.6, 0.0,  0.0, 0.0, 0.0,
         0.2, -0.6, 0.0,  0.0, 0.0, 0.0,

        
         0.3, -0.7, 0.0,  1.0, 1.0, 1.0,
         0.4, -0.7, 0.0,  1.0, 1.0, 1.0,
         0.4, -0.6, 0.0,  1.0, 1.0, 1.0,
         0.3, -0.6, 0.0,  1.0, 1.0, 1.0,

         0.4, -0.7, 0.0,  0.0, 0.0, 0.0,
         0.5, -0.7, 0.0,  0.0, 0.0, 0.0,
         0.5, -0.6, 0.0,  0.0, 0.0, 0.0,
         0.4, -0.6, 0.0,  0.0, 0.0, 0.0,

         0.5, -0.7, 0.0,  1.0, 1.0, 1.0,
         0.6, -0.7, 0.0,  1.0, 1.0, 1.0,
         0.6, -0.6, 0.0,  1.0, 1.0, 1.0,
         0.5, -0.6, 0.0,  1.0, 1.0, 1.0,

         0.6, -0.7, 0.0,  0.0, 0.0, 0.0,
         0.7, -0.7, 0.0,  0.0, 0.0, 0.0,
         0.7, -0.6, 0.0,  0.0, 0.0, 0.0,
         0.6, -0.6, 0.0,  0.0, 0.0, 0.0,
    # Se especifica la necesidad que sea float para captar decimales.
        ], dtype = np.float32)

    # Se definen las conexiones entre vertices, creando dos triangulos para cada cuadrado, necesitando en total 6 por cada uno.
    indices = np.array(
        [0, 1, 2, 2, 3, 0,
         4, 5, 6, 6, 7, 4,
         8, 9, 10, 10, 11, 8,
         12, 13, 14, 14, 15, 12,
         16, 17, 18, 18, 19, 16,
         20, 21, 22, 22, 23, 20,
         24, 25, 26, 26, 27, 24,
         28, 29, 30, 30, 31, 28,
         32, 33, 34, 34, 35, 32,
         36, 37, 38, 38, 39, 36,
         40, 41, 42, 42, 43, 40,
         44, 45, 46, 46, 47, 44,
         48, 49, 50, 50, 51, 48,
         52, 53, 54, 54, 55, 52,
         56, 57, 58, 58, 59, 56,
         60, 61, 62, 62, 63, 60,
         64, 65, 66, 66, 67, 64,
         68, 69, 70, 70, 71, 68,
         72, 73, 74, 74, 75, 72,
         76, 77, 78, 78, 79, 76,
         80, 81, 82, 82, 83, 80,
         84, 85, 86, 86, 87, 84,
         88, 89, 90, 90, 91, 88,
         92, 93, 94, 94, 95, 92,
         96,  97,  98,  98,  99,  96,
         100, 101, 102, 102, 103, 100,
         104, 105, 106, 106, 107, 104,
         108, 109, 110, 110, 111, 108,
         112, 113, 114, 114, 115, 112,
         116, 117, 118, 118, 119, 116,
         120, 121, 122, 122, 123, 120,
         124, 125, 126, 126, 127, 124,
         128, 129, 130, 130, 131, 128,
         132, 133, 134, 134, 135, 132,
         136, 137, 138, 138, 139, 136,
         140, 141, 142, 142, 143, 140,
         144, 145, 146, 146, 147, 144,
         148, 149, 150, 150, 151, 148,
         152, 153, 154, 154, 155, 152,
         156, 157, 158, 158, 159, 156,
         160, 161, 162, 162, 163, 160,
         164, 165, 166, 166, 167, 164,
         168, 169, 170, 170, 171, 168,
         172, 173, 174, 174, 175, 172,
         176, 177, 178, 178, 179, 176,
         180, 181, 182, 182, 183, 180,
         184, 185, 186, 186, 187, 184,
         188, 189, 190, 190, 191, 188,
         192, 193, 194, 194, 195, 192,
         196, 197, 198, 198, 199, 196,
         200, 201, 202, 202, 203, 200,
         204, 205, 206, 206, 207, 204,
         208, 209, 210, 210, 211, 208,
         212, 213, 214, 214, 215, 212,
         216, 217, 218, 218, 219, 216,
         220, 221, 222, 222, 223, 220,
         224, 225, 226, 226, 227, 224,
         228, 229, 230, 230, 231, 228,
         232, 233, 234, 234, 235, 232,
         236, 237, 238, 238, 239, 236,
         240, 241, 242, 242, 243, 240,
         244, 245, 246, 246, 247, 244,
         248, 249, 250, 250, 251, 248,
         252, 253, 254, 254, 255, 252,
         ], dtype= np.uint32)



    size = len(indices)
    #Se retorna aquí el objeto tipo Shape que contiene la información de los indices y el arreglo
    return bs.Shape(vertexData, indices)



def crear_dama(x,y,r,g,b,radius):
    
    circle = []
    for angle in range(0,360,10):
        circle.extend([x, y, 0.0, r, g, b])
        circle.extend([x+np.cos(np.radians(angle))*radius, 
                       y+np.sin(np.radians(angle))*radius, 
                       0.0, r, g, b])
        circle.extend([x+np.cos(np.radians(angle+10))*radius, 
                       y+np.sin(np.radians(angle+10))*radius, 
                       0.0, r, g, b])
    
    return bs.Shape(circle, range(len(circle)))





if __name__ == "__main__":

    # Initialize glfw
    if not glfw.init():
        glfw.set_window_should_close(window, True)

    width = 600
    height = 600

    window = glfw.create_window(width, height, "Tablero de damas", None, None)

    if not window:
        glfw.terminate()
        glfw.set_window_should_close(window, True)

    glfw.make_context_current(window)

    # Connecting the callback function 'on_key' to handle keyboard events
    glfw.set_key_callback(window, on_key)
    
    # Creating our shader program and telling OpenGL to use it
    pipeline = es.SimpleShaderProgram()

    # Creating shapes on GPU memory


    # Se van instanciando objetos tipo Shape de nuestra clase auxiliar basic_shapes, para cada una de las damas que van a ser apropiadamente coloreadas y posicionadas en el tablero.
    dama1 = crear_dama(-0.05,0.05, 1.0, 0.0, 0.0, 0.04)
    dama2 = crear_dama(0.15, 0.05, 1.0, 0.0, 0.0, 0.04)
    dama3 = crear_dama(0.35, 0.05, 1.0, 0.0, 0.0, 0.04)
    dama4 = crear_dama(0.55, 0.05, 1.0, 0.0, 0.0, 0.04)

    dama5 = crear_dama(0.05,-0.05, 1.0, 0.0, 0.0, 0.04)
    dama6 = crear_dama(0.25,-0.05, 1.0, 0.0, 0.0, 0.04)
    dama7 = crear_dama(0.45,-0.05, 1.0, 0.0, 0.0, 0.04)
    dama8 = crear_dama(0.65,-0.05, 1.0, 0.0, 0.0, 0.04)

    dama9 = crear_dama(-0.05,-0.15, 1.0, 0.0, 0.0, 0.04)
    dama10 = crear_dama(0.15,-0.15, 1.0, 0.0, 0.0, 0.04)
    dama11 = crear_dama(0.35,-0.15, 1.0, 0.0, 0.0, 0.04)
    dama12 = crear_dama(0.55,-0.15, 1.0, 0.0, 0.0, 0.04)


    dama13 = crear_dama(0.05,-0.45, 0.0, 0.0, 1.0, 0.04)
    dama14 = crear_dama(0.25,-0.45, 0.0, 0.0, 1.0, 0.04)
    dama15 = crear_dama(0.45,-0.45, 0.0, 0.0, 1.0, 0.04)
    dama16 = crear_dama(0.65,-0.45, 0.0, 0.0, 1.0, 0.04)

    
    dama17 = crear_dama(-0.05,-0.55, 0.0, 0.0, 1.0, 0.04)
    dama18 = crear_dama(0.15,-0.55, 0.0, 0.0, 1.0, 0.04)
    dama19 = crear_dama(0.35,-0.55, 0.0, 0.0, 1.0, 0.04)
    dama20 = crear_dama(0.55,-0.55, 0.0, 0.0, 1.0, 0.04)


    dama21 = crear_dama(0.05,-0.65, 0.0, 0.0, 1.0, 0.04)
    dama22 = crear_dama(0.25,-0.65, 0.0, 0.0, 1.0, 0.04)
    dama23 = crear_dama(0.45,-0.65, 0.0, 0.0, 1.0, 0.04)
    dama24 = crear_dama(0.65,-0.65, 0.0, 0.0, 1.0, 0.04)

    # Desde la clase auxiliar gpu_shape, se nombran los buffers con initBuffers() para los vao, vbo, ebo respectivos que usaremos para cada dama.
    # Desde la clase auxiliar easy_shaders, se hace el binding del los objetos con setupVAO, glBindVertexArray para el vao, glBindBuffer para el vbo y ebo. 
    # Se especifican los colores y posiciones para el shader.

    gpuDama1 = GPUShape().initBuffers()
    pipeline.setupVAO(gpuDama1)

    gpuDama2 = GPUShape().initBuffers()
    pipeline.setupVAO(gpuDama2)

    gpuDama3 = GPUShape().initBuffers()
    pipeline.setupVAO(gpuDama3)

    gpuDama4 = GPUShape().initBuffers()
    pipeline.setupVAO(gpuDama4)

    gpuDama5 = GPUShape().initBuffers()
    pipeline.setupVAO(gpuDama5)

    gpuDama6 = GPUShape().initBuffers()
    pipeline.setupVAO(gpuDama6)

    gpuDama7 = GPUShape().initBuffers()
    pipeline.setupVAO(gpuDama7)

    gpuDama8 = GPUShape().initBuffers()
    pipeline.setupVAO(gpuDama8)

    gpuDama9 = GPUShape().initBuffers()
    pipeline.setupVAO(gpuDama9)

    gpuDama10 = GPUShape().initBuffers()
    pipeline.setupVAO(gpuDama10)

    gpuDama11 = GPUShape().initBuffers()
    pipeline.setupVAO(gpuDama11)

    gpuDama12 = GPUShape().initBuffers()
    pipeline.setupVAO(gpuDama12)

    gpuDama13 = GPUShape().initBuffers()
    pipeline.setupVAO(gpuDama13)

    gpuDama14 = GPUShape().initBuffers()
    pipeline.setupVAO(gpuDama14)

    gpuDama15 = GPUShape().initBuffers()
    pipeline.setupVAO(gpuDama15)

    gpuDama16 = GPUShape().initBuffers()
    pipeline.setupVAO(gpuDama16)

    gpuDama17 = GPUShape().initBuffers()
    pipeline.setupVAO(gpuDama17)

    gpuDama18 = GPUShape().initBuffers()
    pipeline.setupVAO(gpuDama18)

    gpuDama19 = GPUShape().initBuffers()
    pipeline.setupVAO(gpuDama19)

    gpuDama20 = GPUShape().initBuffers()
    pipeline.setupVAO(gpuDama20)

    gpuDama21 = GPUShape().initBuffers()
    pipeline.setupVAO(gpuDama21)

    gpuDama22 = GPUShape().initBuffers()
    pipeline.setupVAO(gpuDama22)

    gpuDama23 = GPUShape().initBuffers()
    pipeline.setupVAO(gpuDama23)

    gpuDama24 = GPUShape().initBuffers()
    pipeline.setupVAO(gpuDama24)


    # Nuevamente con métodos de gpu_shape, se utiliza fillBuffers que hacen un segundo binding e inicializan los buffers previamente nombrados gracias a los indices y vertexData

    gpuDama1.fillBuffers(dama1.vertices, dama1.indices, GL_STATIC_DRAW)
    gpuDama2.fillBuffers(dama2.vertices, dama2.indices, GL_STATIC_DRAW)
    gpuDama3.fillBuffers(dama3.vertices, dama3.indices, GL_STATIC_DRAW)
    gpuDama4.fillBuffers(dama4.vertices, dama4.indices, GL_STATIC_DRAW)
    
    gpuDama5.fillBuffers(dama5.vertices, dama5.indices, GL_STATIC_DRAW)
    gpuDama6.fillBuffers(dama6.vertices, dama6.indices, GL_STATIC_DRAW)
    gpuDama7.fillBuffers(dama7.vertices, dama7.indices, GL_STATIC_DRAW)
    gpuDama8.fillBuffers(dama8.vertices, dama8.indices, GL_STATIC_DRAW)
  
    gpuDama9.fillBuffers(dama9.vertices, dama9.indices, GL_STATIC_DRAW)
    gpuDama10.fillBuffers(dama10.vertices, dama10.indices, GL_STATIC_DRAW)
    gpuDama11.fillBuffers(dama11.vertices, dama11.indices, GL_STATIC_DRAW)
    gpuDama12.fillBuffers(dama12.vertices, dama12.indices, GL_STATIC_DRAW)
  
    gpuDama13.fillBuffers(dama13.vertices, dama13.indices, GL_STATIC_DRAW)
    gpuDama14.fillBuffers(dama14.vertices, dama14.indices, GL_STATIC_DRAW)
    gpuDama15.fillBuffers(dama15.vertices, dama15.indices, GL_STATIC_DRAW)
    gpuDama16.fillBuffers(dama16.vertices, dama16.indices, GL_STATIC_DRAW)

    gpuDama17.fillBuffers(dama17.vertices, dama17.indices, GL_STATIC_DRAW)
    gpuDama18.fillBuffers(dama18.vertices, dama18.indices, GL_STATIC_DRAW)
    gpuDama19.fillBuffers(dama19.vertices, dama19.indices, GL_STATIC_DRAW)
    gpuDama20.fillBuffers(dama20.vertices, dama20.indices, GL_STATIC_DRAW)

    gpuDama21.fillBuffers(dama21.vertices, dama21.indices, GL_STATIC_DRAW)
    gpuDama22.fillBuffers(dama22.vertices, dama22.indices, GL_STATIC_DRAW)
    gpuDama23.fillBuffers(dama23.vertices, dama23.indices, GL_STATIC_DRAW)
    gpuDama24.fillBuffers(dama24.vertices, dama24.indices, GL_STATIC_DRAW)
    

    # Se repite el mismo proceso anterior, pero ahora para el (unico) tablero
    tableroShape = createQuad() 
    gpuTablero = GPUShape().initBuffers()
    pipeline.setupVAO(gpuTablero)
    gpuTablero.fillBuffers(tableroShape.vertices, tableroShape.indices, GL_STATIC_DRAW )
 



    # Setting up the clear screen color
    glClearColor(0.15, 0.15, 0.15, 1.0)

    while not glfw.window_should_close(window):
        # Using GLFW to check for input events
        glfw.poll_events()

        # Filling or not the shapes depending on the controller state
        if (controller.fillPolygon):
            glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
        else:
            glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)

        # Clearing the screen in both, color and depth
        glClear(GL_COLOR_BUFFER_BIT)

        # Se le dice a OpenGL que use el shaderProgram simple
        glUseProgram(pipeline.shaderProgram)

        # Se usa una última vez un método de la clase easy_shaders, que hará la labor de unir el vao, dibujar la figura y separarlo sucesivamente, harta terminar la última figura.
        pipeline.drawCall(gpuTablero)
        pipeline.drawCall(gpuDama1)
        pipeline.drawCall(gpuDama2)
        pipeline.drawCall(gpuDama3)
        pipeline.drawCall(gpuDama4)
        pipeline.drawCall(gpuDama5)
        pipeline.drawCall(gpuDama6)
        pipeline.drawCall(gpuDama7)
        pipeline.drawCall(gpuDama8)
        pipeline.drawCall(gpuDama9)
        pipeline.drawCall(gpuDama10)
        pipeline.drawCall(gpuDama11)
        pipeline.drawCall(gpuDama12)
        pipeline.drawCall(gpuDama13)
        pipeline.drawCall(gpuDama14)
        pipeline.drawCall(gpuDama15)
        pipeline.drawCall(gpuDama16)
        pipeline.drawCall(gpuDama17)
        pipeline.drawCall(gpuDama18)
        pipeline.drawCall(gpuDama19)
        pipeline.drawCall(gpuDama20)
        pipeline.drawCall(gpuDama21)
        pipeline.drawCall(gpuDama22)
        pipeline.drawCall(gpuDama23)
        pipeline.drawCall(gpuDama24)




        # Once the render is done, buffers are swapped, showing only the complete scene.
        glfw.swap_buffers(window)

    # freeing GPU memory
    
    
    #gpuSky.clear()

    glfw.terminate()
