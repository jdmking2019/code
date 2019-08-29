#对图像生成标记框和xml文件
try:
    from lxml import etree
except ImportError:
    import xml.etree.ElementTree as etree
import os
from PIL import Image
import numpy as np

src_dir = "/home/jdmking/Downloads/character_digit_Version1/Sample036"
filename = os.listdir(src_dir)
xml_dir = "/home/jdmking/Downloads/annotations/"
# src_path = [os.path.join(src_dir,filename) for filename in os.listdir(src_dir)]
# Growth_size = 15
Class = "Z"
def Write_xml(filename,x_min,y_min,x_max,y_max,width,height,Class):

    annotation = etree.Element("annotation")
    etree.SubElement(annotation, "folder").text = "pidai"
    etree.SubElement(annotation, "filename").text = filename
    source = etree.SubElement(annotation, "source")
    etree.SubElement(source, "database").text = "Unknown"
    size = etree.SubElement(annotation, "size")
    etree.SubElement(size, "width").text = str(width)
    etree.SubElement(size, "height").text = str(height)
    etree.SubElement(size, "depth").text = '1'
    etree.SubElement(annotation, "segmented").text = '0'
    key_object = etree.SubElement(annotation, "object")
    etree.SubElement(key_object, "name").text = Class
    etree.SubElement(key_object, "difficult").text = '0'
    bndbox = etree.SubElement(key_object, "bndbox")
    etree.SubElement(bndbox, "xmin").text = str(x_min)
    etree.SubElement(bndbox, "ymin").text = str(y_min)
    etree.SubElement(bndbox, "xmax").text = str(x_max)
    etree.SubElement(bndbox, "ymax").text = str(y_max)
    doc = etree.ElementTree(annotation)
    if not os.path.exists(xml_dir):
        os.mkdir(xml_dir)
    xml_path = os.path.join(xml_dir,filename[:-4] + ".xml")
    with open(xml_path, "wb+") as file:
        doc.write(file)

count = 0
for filename1 in filename:

    Img_path = os.path.join(src_dir,filename1)
    Img1 = Image.open(Img_path)
    Write_xml(filename1,x_min = 1, y_min=1, x_max=15, y_max=15,width=16, height=16,Class=Class)

    # Img = np.float32(Img1)
    # height = Img.shape[0]
    # width = Img.shape[1]
    # # x_min = np.int32(filename1.split("-")[5])
    # y_min = np.int32(filename1.split("-")[6])
    # x_max = np.int32(filename1.split("-")[7])
    # y_max = np.int32(filename1.split("-")[8][:-4])

    # if x_min >= Growth_size and y_min >= Growth_size:
    #     new_xmin = Growth_size
    #     new_ymin = Growth_size
    #     new_xmax = Growth_size + (x_max - x_min)
    #     new_ymax = Growth_size + (y_max - y_min)
    #     Write_xml(new_xmin, new_ymin, new_xmax, new_ymax, filename1, width, height)
    #
    # elif x_min >= Growth_size and y_min <= Growth_size:
    #     new_xmin = Growth_size
    #     new_ymin = 0
    #     new_xmax = Growth_size + (x_max - x_min)
    #     new_ymax = y_max - y_min
    #     Write_xml(new_xmin, new_ymin, new_xmax, new_ymax, filename1, width, height)
    #
    # elif x_min <= Growth_size and y_min >= Growth_size:
    #     new_xmin = 0
    #     new_ymin = Growth_size
    #     new_xmax = x_max - x_min
    #     new_ymax = Growth_size + (y_max - y_min)
    #     Write_xml(new_xmin, new_ymin, new_xmax, new_ymax, filename1, width, height)
    #
    # elif x_min <= Growth_size and y_min <= Growth_size:
    #     new_xmin = 0
    #     new_ymin = 0
    #     new_xmax = x_max - x_min
    #     new_ymax = y_max - y_min
    #     Write_xml(new_xmin, new_ymin, new_xmax, new_ymax, filename1, width, height)
    # else:
    #     print("-------error------")
    count = count + 1
    print("create %d xml" % count)
    print(filename1)
