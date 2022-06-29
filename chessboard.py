# -*- coding: utf-8 -*-
"""


@author: Luisa Domínguez López
"""

#
import numpy as np
import cv2
from matplotlib import pyplot as plt
 
 
 # Generación de tablero de ajedrez
def generate_checkerboard(rows_num, columns_num, block_size, base_color):
 
    block_size = block_size * 4
    image_width = block_size * columns_num
    image_height = block_size * rows_num
    inv_color = tuple(255 - val for val in base_color),
 
    checker_board = np.zeros((image_height, image_width, 3), np.uint8)
    color_row = 0
    color_column = 0
 
    for i in range(0, image_height, block_size):
            color_row = not color_row
            color_column = color_row
 
            for j in range(0, image_width, block_size):
                checker_board[i:i+block_size, j:j +
                            block_size] = base_color if color_column else inv_color
                color_column = not color_column
 
    return checker_board
#
b1 = generate_checkerboard(6,9, 20, (255,255,255)) #columna, fila, tamaño de visualización
cv2.imshow('checkerboard', b1)

 
# b2 = generate_checkerboard(3,9, 20, (255,255,255))
# cv2.imshow('checkerboard2', b2)
#
cv2.waitKey(0)
cv2.destroyAllWindows()
 
cv2.imwrite('chessboard.png', b1)