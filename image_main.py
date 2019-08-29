import os
from image_fun import *


Img_src_path="/home/jdmking/AnGang_work/GJH/gjh/src_image/image/"
Xml_src_path="/home/jdmking/AnGang_work/GJH/gjh/src_image/annotations/"

# Img_rotate_path="/media/wangxigang/DATA/new/rotate_images/"
# Xml_rotate_path="/media/wangxigang/DATA/new/rotate_anno/"
# if not os.path.exists(Img_rotate_path):
#     os.mkdir(Img_rotate_path)
# if not os.path.exists(Xml_rotate_path):
#     os.mkdir(Xml_rotate_path)

# Img_perspective_path="/media/wangxigang/DATA/new/pers_images/"
# Xml_perspective_path="/media/wangxigang/DATA/new/pers_anno/"
# if not os.path.exists(Img_perspective_path):
#     os.mkdir(Img_perspective_path)
# if not os.path.exists(Xml_perspective_path):
#     os.mkdir(Xml_perspective_path)
#
# Img_crop_path="/media/wangxigang/DATA/new/crop_images/"
# Xml_crop_path="/media/wangxigang/DATA/new/crop_anno/"
# if not os.path.exists(Img_crop_path):
#     os.mkdir(Img_crop_path)
# if not os.path.exists(Xml_crop_path):
#     os.mkdir(Xml_crop_path)

Img_color_path="/home/jdmking/AnGang_work/GJH/gjh/data_add/color_images/"
Xml_color_path="/home/jdmking/AnGang_work/GJH/gjh/data_add/color_annotations/"
if not os.path.exists(Img_color_path):
    os.mkdir(Img_color_path)
if not os.path.exists(Xml_color_path):
    os.mkdir(Xml_color_path)

Img_fuzzy_path="/home/jdmking/AnGang_work/GJH/gjh/data_add/fuzzy_images/"
Xml_fuzzy_path="/home/jdmking/AnGang_work/GJH/gjh/data_add/fuzzy_annotations/"
if not os.path.exists(Img_fuzzy_path):
    os.mkdir(Img_fuzzy_path)
if not os.path.exists(Xml_fuzzy_path):
    os.mkdir(Xml_fuzzy_path)

Img_noise_path="/home/jdmking/AnGang_work/GJH/gjh/data_add/noise_images/"
Xml_noise_path="/home/jdmking/AnGang_work/GJH/gjh/data_add/noise_annotations/"
if not os.path.exists(Img_noise_path):
    os.mkdir(Img_noise_path)
if not os.path.exists(Xml_noise_path):
    os.mkdir(Xml_noise_path)


# # rotate *9
# filename_all = os.listdir(Img_src_path)
# for Imgname in filename_all:
#     Img = imread(Img_src_path + Imgname)
#     Xmlname = Imgname[:-4]+'.xml'
#     Xml_path = Xml_src_path+Xmlname
#     th_step = 5
#     th_range = 20
#     flag = 0
#     for th in range(-th_range,th_range+1,th_step):
#         xDoc = etree.parse(Xml_path)
#         flag+=1
#         Imgname_0 = Imgname[:-4] + "_" + str(flag) + ".jpg"
#         Create_Img_Rotate(Img, xDoc, Img_rotate_path, Xml_rotate_path, Imgname_0, th)


# # Perspective *2
# filename_all0 = os.listdir(Img_rotate_path)
# for Imgname0 in filename_all0:
#     Img0 = imread(Img_rotate_path + Imgname0)
#     Xmlname0 = Imgname0[:-4] + '.xml'
#     Xml_path0 = Xml_perspective_path + Xmlname0
#     xDoc0 = etree.parse(Xml_path0)
#     Create_Img_Perspective(Img0, xDoc0, Img_perspective_path, Xml_perspective_path, Imgname0)


# # crop *5
# filename_all1 = os.listdir(Img_perspective_path)
# for Imgname1 in filename_all1:
#     Img1 = imread(Img_perspective_path + Imgname1)
#     Xmlname1 = Imgname1[:-4] + '.xml'
#     Xml_path1 = Xml_perspective_path + Xmlname1
#     xDoc1 = etree.parse(Xml_path1)
#     Create_Img_Crop(Img1, xDoc1, Img_crop_path, Xml_crop_path, Imgname1)
#

##color
count = 0
filename_all2 = os.listdir(Img_src_path)
for Imgname2 in filename_all2:
    Img2 = imread(Img_src_path + Imgname2)
    Xmlname2 = Imgname2[:-4] + '.xml'
    Xml_path2 = Xml_src_path + Xmlname2
    xDoc2 = etree.parse(Xml_path2)
    Create_Img_Color(Img2, xDoc2, Img_color_path, Xml_color_path, Imgname2)
    count += 1
    print("image color add %s" % str(count))

count = 0
#fuzzy *2
filename_all3 = os.listdir(Img_color_path)
standard_deviation=2
for Imgname3 in filename_all3:
    Img3 = imread(Img_color_path + Imgname3)
    Xmlname3 = Imgname3[:-4] + '.xml'
    Xml_path3 = Xml_color_path + Xmlname3
    xDoc3 = etree.parse(Xml_path3)
    Create_gaussian_fuzzy(Img3, xDoc3, Img_fuzzy_path, Xml_fuzzy_path, Imgname3,standard_deviation)
    count += 1
    print("image fuzzy add %s" % str(count))

count = 0
#noise *2
filename_all4 = os.listdir(Img_fuzzy_path)
percetage=0.01
for Imgname4 in filename_all4:
    Img4 = imread(Img_fuzzy_path + Imgname4)
    Xmlname4 = Imgname4[:-4] + '.xml'
    Xml_path4 = Xml_fuzzy_path + Xmlname4
    xDoc4 = etree.parse(Xml_path4)
    Create_salt_noise(Img4, xDoc4, Img_noise_path, Xml_noise_path, Imgname4,percetage)
    count += 1
    print("image noise add %s" % str(count))