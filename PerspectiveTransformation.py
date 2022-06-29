# -*- coding: utf-8 -*-
"""

@author:  Luisa Domínguez López
"""
# import necessary libraries

#importing the module cv2 and numpy
import cv2
import numpy as np
import glob
import os

# Path to the image that you want to undistort
path_directory = 'undistorted03'
path_search = path_directory + '/*_undistorted.jpg'

undistorted_img = glob.glob(path_search)

new_path = 'transformed03'
os.mkdir(new_path)


for undistorted_img_filename in undistorted_img:
           
    
    #reading the image which is to be transformed
    imagergb = cv2.imread(undistorted_img_filename)
    
    #specifying the points in the source image which is to be transformed to the corresponding points in the destination image
    srcpts = np.float32([[449, 500], [1309, 510], [72, 960], [1687, 966]])
    destpts = np.float32([[0, 0], [600, 0], [0, 600], [600, 600]])
    
    #applying PerspectiveTransform() function to transform the perspective of the given source image to the corresponding points in the destination image
    resmatrix = cv2.getPerspectiveTransform(srcpts, destpts)
    
    #applying warpPerspective() function to display the transformed image
    resultimage = cv2.warpPerspective(imagergb, resmatrix, (600, 600))
    
    #displaying the original image and the transformed image as the output on the screen
    # cv2.imshow('frame', imagergb)
    # cv2.imshow('frame1', resultimage)
       
    # Create the output file name by removing the '.bmp' part
    size = len(undistorted_img_filename)
    
    new_filename = undistorted_img_filename.replace(path_directory,"")
    new_filename = new_filename.replace(new_filename[:1], "")
    print(new_filename[:2])

    new_filename = new_path + '/' +  new_filename[:2] + '.jpg'   
         
    # Save the undistorted image
    cv2.imwrite(new_filename, resultimage)
    
   
        
    
    
    


