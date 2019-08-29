from PIL import Image
from scipy.misc import imread,imshow,imresize,imsave
from scipy import ndimage
from numpy import *
import numpy as np
from scipy.ndimage import filters
import cv2
try:
    from lxml import etree
except ImportError:
    import xml.etree.ElementTree as etree
import math

#add G_noise
# def Create_B_noise(image,percetage):
#     G_Noiseimg=image
#     G_NoiseNum=int(percetage * image.shape[0]*image.shape[1])
#     for i in range(G_NoiseNum):
#         temp_x=np.random.randint(10,100)
#         temp_y=np.random.randint(10,100)
#         G_Noiseimg[temp_x][temp_y]=255
#
#     return G_Noiseimg

#add salt and Pepper noise
def Create_salt_noise(image, xml_doc, image_path, xml_path, image_name,percetage):
    Create_filesave(image, xml_doc, image_path, xml_path, image_name)
    SP_Noiseimg = image
    SP_NoiseNum = int(percetage * image.shape[0] * image.shape[1])
    for i in range(SP_NoiseNum):
        # temp_x=random.random_integers(0,image.shape[0]-1)
        # temp_y=random.random_integers(0,image.shape[1]-1)
        temp_x = np.random.randint(0,image.shape[0]-1)
        temp_y = np.random.randint(0,image.shape[1]-1)
        if random.random_integers(0,1) == 0:
            SP_Noiseimg[temp_x,temp_y] = 0
        else:
            SP_Noiseimg[temp_x,temp_y] = 255
    noise_img = SP_Noiseimg
    name_new = image_name[:-4]+"_"+str(1)+".jpg"
    Create_filesave(noise_img, xml_doc, image_path, xml_path, name_new)


#add Gaussian blur
def Create_gaussian_fuzzy(image, xml_doc, image_path, xml_path, image_name,standard_deviation):

    Create_filesave(image, xml_doc, image_path, xml_path, image_name)

    fuzzy_image=np.zeros(image.shape, "int")
    for i in range(3):
        fuzzy_image[:, :, i] = filters.gaussian_filter(image[:, :, i], standard_deviation)

    name_new=image_name[:-4]+"_"+str(1)+".jpg"
    Create_filesave(fuzzy_image, xml_doc, image_path, xml_path, name_new)



#add image rotate
def Create_Img_Rotate(image,xml_doc,image_path,xml_path,image_name,afla):
    #image_expand= cv2.copyMakeBorder(image,top,down,left,right,cv2.BORDER_REPLICATE, value=0)
    hight,weight = image.shape[:2]
    M = cv2.getRotationMatrix2D(( weight / 2, hight / 2), afla, 1)
    rotate_image = cv2.warpAffine(image, M, (weight, hight))
    # xml_doc = etree.parse(xml_path)
    root = xml_doc.getroot()

    bndbox=root[6][4]
    xmin,ymin,xmax,ymax=bndbox[0],bndbox[1],bndbox[2],bndbox[3]
    x_min=int(xmin.text)
    y_min=int(ymin.text)
    x_max=int(xmax.text)
    y_max=int(ymax.text)
    xo= weight / 2
    yo= hight / 2
    xo_r=rotate_image.shape[1] / 2
    yo_r=rotate_image.shape[0] / 2
    theta = (360 - afla) / 180 * math.pi
    x_1 = (x_min - xo) * math.cos(theta) - (y_min - yo) * math.sin(theta) + xo_r
    y_1 = (x_min - xo) * math.sin(theta) + (y_min - yo) * math.cos(theta) + yo_r

    x_2 = (x_max - xo) * math.cos(theta) - (y_min - yo) * math.sin(theta) + xo_r
    y_2 = (x_max - xo) * math.sin(theta) + (y_min - yo) * math.cos(theta) + yo_r

    x_3 = (x_min - xo) * math.cos(theta) - (y_max - yo) * math.sin(theta) + xo_r
    y_3 = (x_min - xo) * math.sin(theta) + (y_max - yo) * math.cos(theta) + yo_r

    x_4 = (x_max - xo) * math.cos(theta) - (y_max - yo) * math.sin(theta) + xo_r
    y_4 = (x_max - xo) * math.sin(theta) + (y_max - yo) * math.cos(theta) + yo_r

    xmin.text= str(round(min(min(x_1, x_2), min(x_3, x_4))))
    xmax.text= str(round(max(max(x_1, x_2), max(x_3, x_4))))
    ymin.text= str(round(min(min(y_1, y_2), min(y_3, y_4))))
    ymax.text= str(round(max(max(y_1, y_2), max(y_3, y_4))))


    Create_filesave(rotate_image, xml_doc, image_path, xml_path, image_name)


#add image tailor
def Create_Img_Crop(image, xml_doc, image_path, xml_path, imagename):
    root = xml_doc.getroot()
    bndbox = root[6][4]
    xmin, ymin, xmax, ymax = bndbox[0], bndbox[1], bndbox[2], bndbox[3]
    x_min = int(xmin.text)
    y_min = int(ymin.text)
    x_max = int(xmax.text)
    y_max = int(ymax.text)
    image_size=500

    # 左上平移
    start_x=int(x_min-(image_size-(x_max-x_min)))
    end_x=int(x_min-(image_size-(x_max-x_min)) / 2)
    start_y=int(y_min-(image_size-(y_max-y_min)))
    end_y=int(y_min-(image_size-(y_max-y_min)) / 2)
    start_randint_x= np.random.randint(start_x,end_x)
    start_randint_y= np.random.randint(start_y,end_y)
    left_top_image=image[start_randint_y:start_randint_y+image_size,start_randint_x:start_randint_x+image_size]

    xmin.text = str(ｘ_min - start_randint_x)
    xmax.text = str(x_max - start_randint_x)
    ymin.text = str(y_min - start_randint_y)
    ymax.text = str(y_max - start_randint_y)

    name_new = imagename[:-4] + '_' + str(1) + ".jpg"
    Create_filesave(left_top_image, xml_doc, image_path, xml_path, name_new)


    #左下平移
    start_randint_y1=np.random.randint(end_y,y_min)
    start_randint_x = np.random.randint(start_x, end_x)
    left_down_image= image[start_randint_y1:start_randint_y1+image_size,start_randint_x:start_randint_x+image_size]

    xmin.text = str(ｘ_min - start_randint_x)
    xmax.text = str(x_max - start_randint_x)
    ymin.text = str(y_min - start_randint_y1)
    ymax.text = str(y_max - start_randint_y1)

    name_new = imagename[:-4] + '_' + str(2) + ".jpg"
    Create_filesave(left_down_image, xml_doc, image_path, xml_path, name_new)

    #右上平移
    start_randint_x1 = np.random.randint(end_x, x_min)
    start_randint_y = np.random.randint(start_y, end_y)
    right_top_image = image[start_randint_y:start_randint_y + image_size,
                      start_randint_x1:start_randint_x1 + image_size]

    xmin.text = str(x_min - start_randint_x1)
    xmax.text = str(x_max - start_randint_x1)
    ymin.text = str(y_min - start_randint_y)
    ymax.text = str(y_max - start_randint_y)

    name_new = imagename[:-4] + '_' + str(3) + ".jpg"
    Create_filesave(right_top_image, xml_doc, image_path, xml_path, name_new)

    #右下平移

    start_randint_y2 = np.random.randint(end_y, y_min)
    start_randint_x2= np.random.randint(end_x, x_min)
    right_down_image = image[start_randint_y2:start_randint_y2 + image_size,
                       start_randint_x2:start_randint_x2 + image_size]
    xmin.text = str(x_min - start_randint_x2)
    xmax.text = str(x_max - start_randint_x2)
    ymin.text = str(y_min - start_randint_y2)
    ymax.text = str(y_max - start_randint_y2)

    name_new = imagename[:-4] + '_' + str(4) + ".jpg"
    Create_filesave(right_down_image, xml_doc, image_path, xml_path, name_new)

#add image tranform
def Create_Img_Color(image, xml_doc, image_path, xml_path, image_name):

    Create_filesave(image, xml_doc, image_path, xml_path, image_name)

    h,w,k=image.shape
    R = image[:,:,0]
    G = image[:,:,1]
    B = image[:,:,2]

    image_out= np.zeros([h,w,k],"int")
    image_out[:,:,0]=np.rint(np.where(R* 1.5>255, 255, R* 1.5))
    image_out[:,:,1]=np.rint(np.where(G* 1.5>255, 255, G* 1.5))
    image_out[:,:,2]=np.rint(np.where(B* 1.5>255, 255, B* 1.5))
    name_new = image_name[:-4] + "_" + "01.jpg"
    Create_filesave(image_out,xml_doc,image_path,xml_path,name_new)

    image_out1 = np.zeros([h, w, k],"int")
    image_out1[:,:,0] = np.rint(R * 0.5)
    image_out1[:,:,1] = np.rint(G * 0.5)
    image_out1[:,:,2] = np.rint(B * 0.5)
    name_new = image_name[:-4] + "_" + "02.jpg"
    Create_filesave(image_out1, xml_doc, image_path, xml_path, name_new)

    image_out2 = np.zeros([h, w, k])
    image_out2[:, :, 0] = R
    image_out2[:, :, 1] = G
    image_out2[:, :, 2] = G
    name_new = image_name[:-4] + "_" + "03.jpg"
    # imshow(image_out2)
    Create_filesave(image_out2, xml_doc, image_path, xml_path, name_new)

    # image_out3 = np.zeros([h, w, k])
    # image_out3[:, :, 0] = np.rint(np.where(R > 255, 255, R))
    # image_out3[:, :, 1] = np.rint(np.where(G + 50 > 255, 255, G + 20))
    # image_out3[:, :, 2] = np.rint(np.where(B + 50 > 255, 255, B + 20))
    # name_new = image_name[:-4] + "_" + "04.jpg"
    # imshow(image_out3)
    # Create_filesave(image_out3, xml_doc, image_path, xml_path, name_new)

    image_out4 = np.zeros([h, w, k])
    image_out4[:, :, 0] = R
    image_out4[:, :, 1] = G
    image_out4[:, :, 2] = Ｒ
    name_new = image_name[:-4] + "_" + "05.jpg"
    # imshow(image_out4)
    Create_filesave(image_out4, xml_doc, image_path, xml_path, name_new)

    image_out5 = np.zeros([h, w, k])
    image_out5[:, :, 0] = R
    image_out5[:, :, 1] = R
    image_out5[:, :, 2] = G
    name_new = image_name[:-4] + "_" + "06.jpg"
    # imshow(image_out5)
    Create_filesave(image_out5, xml_doc, image_path, xml_path, name_new)


def Create_Img_Perspective(image, xml_doc,image_path,xml_path,imagename):


    Create_filesave(image, xml_doc, image_path, xml_path, imagename)

    # R, G, B = cv2.split(image)
    M, N, K = image.shape
    H = np.array(
        [[1.0, 0.1, 0.0],
         [0.1, 1.0, 0.0],
         [0, 0, 1]]
    )

    y_1, x_1 = np.dot([1, 1, 1],H)[0:2]
    y_2, x_2 = np.dot([1, N, 1],H)[0:2]
    y_3, x_3 = np.dot([M, 1, 1], H)[0:2]
    y_4, x_4 = np.dot([M, N, 1], H)[0:2]

    xmin = min(min(x_1, x_2), min(x_3, x_3))
    xmax = max(max(x_1, x_3), max(x_3, x_4))
    ymin = min(min(y_1, y_2), min(y_3, y_4))
    ymax = max(max(y_1, y_2), max(y_3, y_4))
    height = int(ymax - ymin + 0.5)
    width = int(xmax - xmin + 0.5)

    dx = width - N
    dy = height - M

    img_n = ndimage.affine_transform(image, H)
    Per_image = Image.fromarray(img_n)

    root = xml_doc.getroot()
    bndbox = root[6][4]
    xmin, ymin, xmax, ymax = bndbox[0], bndbox[1], bndbox[2], bndbox[3]
    x_min = int(xmin.text)
    y_min = int(ymin.text)
    x_max = int(xmax.text)
    y_max = int(ymax.text)

    y_0, x_0 = np.dot([y_min, x_min, 1],H)[0:2]
    y_1, x_1 = np.dot([y_min, x_max, 1],H)[0:2]
    y_2, x_2 = np.dot([y_max, x_min, 1],H)[0:2]
    y_3, x_3 = np.dot([y_max, x_max, 1],H)[0:2]

    xmin.text = str(int(round(min(min(x_0, x_1), min(x_2, x_3))) +0.5)-dx)
    xmax.text = str(int(round(max(max(x_0, x_1), max(x_2, x_3))) +0.5)-dx)
    ymin.text = str(int(round(min(min(y_0, y_1), min(y_2, y_3))) +0.5)-dy)
    ymax.text = str(int(round(max(max(y_0, y_1), max(y_2, y_3))) +0.5)-dy)
    # #
    name_new = imagename[:-4] + "_" + "01.jpg"
    Create_filesave(Per_image, xml_doc, image_path, xml_path, name_new)
    # return (img_new, xml_doc, per_filename)

# save the files
def Create_filesave(image, xml_doc, image_path, xml_path, image_name):
    root = xml_doc.getroot()
    filename = root[1]
    path = root[2]
    filename.text=image_name
    path.text = image_path + image_name
    imsave(image_path + image_name, image)
    xml_doc.write(xml_path + image_name[:-4] + ".xml")

