# -*- coding: utf-8 -*-
"""


@author: Luisa Domínguez López
"""
# import necessary libraries

#importing the module cv2 and numpy
import cv2
import numpy as np
import glob # Used to get retrieve files that have a specified pattern

# Path to the image that you want to undistort
#Get the file path for distorded images in the current directory
undistorted_images = glob.glob('Trapez_crop/*.jpg')

 # Go through each chessboard image, one by one
for undistorted_img_filename in undistorted_images:
    #reading the image which is to be transformed
    print(undistorted_img_filename) 
    img = cv2.imread(undistorted_img_filename)
    crop_img = img[300:600, 0:600]
    cv2.imshow("cropped", crop_img)
    
    # Create the output file name by removing the '.bmp' part
    size = len(undistorted_img_filename)
    new_filename = undistorted_img_filename[:size - 4]
    new_filename = new_filename + '_crop.jpg'
    # Save the undistorted image
    cv2.imwrite(new_filename, crop_img)

