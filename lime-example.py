# -*- coding: utf-8 -*-
# @Project : image-enhancement-utils
# @File    : lime-example.py
# @Author  : MQB
# @Email   : mengqingbin@aliyun.com
# @Time    : 2018-05-18 23:03


import cv2
import sys
import os

from algorithms import lime

file_path= 'D:/FPGA/python-lime-image-enhancement/images/test-img.jpg'
#file_path = sys.argv[1]

path = '/content/drive/My Drive/bddsample/'

result_path1 = '/content/drive/My Drive/night_images_results_ws1/'
result_path2 = '/content/drive/My Drive/night_images_results_ws2/'
result_path3 = '/content/drive/My Drive/night_images_results_ws3/'
result_path4 = '/content/drive/My Drive/night_images_results_ws4/'

for name in os.listdir(path):
    print(name)

    # file_name = os.path.split(file_path)[1]
    # print(file_name)

    file_name = name
    # raw_image = cv2.imread(file_path)

    raw_image = cv2.imread(path + name)
    #print(raw_image)
    img_ws1 = lime.lime(raw_image, weight_strategy=1)
    img_ws2 = lime.lime(raw_image, weight_strategy=2)
    img_ws3 = lime.lime(raw_image, weight_strategy=3)
    img_ws4 = lime.lime(raw_image, weight_strategy=4)

    cv2.imwrite(result_path1 + '%s_ws1.jpg' % file_name, img_ws1)
    cv2.imwrite(result_path2 + '%s_ws2.jpg' % file_name, img_ws2)
    cv2.imwrite(result_path3 + '%s_ws3.jpg' % file_name, img_ws3)
    cv2.imwrite(result_path4 + '%s_ws4.jpg' % file_name, img_ws4)

    # cv2.imshow('raw_image', raw_image)
    # cv2.imshow('new_image_ws1', img_ws1)
    # cv2.imshow('new_image_ws2', img_ws2)
    # cv2.imshow('new_image_ws3', img_ws3)
    # cv2.imshow('new_image_ws4', img_ws4)

