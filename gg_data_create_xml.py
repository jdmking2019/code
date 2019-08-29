#将公共数据集加入训练集中，生成xml
from lxml import etree
from PIL import Image
import os

# src_xml = "/home/jdmking/GJH/GG_DATA/annotations"
src_img = "/home/jdmking/GJH/GG_DATA/image2"
save_img = "/home/jdmking/GJH/GG_DATA/image1"
# xml_dir = "/home/jdmking/GJH/GG_DATA/annotations1"
img_path = os.listdir(src_img)
count = 0
for img_path1 in img_path:
    if img_path1[-4:] == ".png":
        img_path2 = img_path1[:-4] + ".jpg"
        img = Image.open(os.path.join(src_img,img_path1))
        img = img.convert("RGB")
        img.save(os.path.join(save_img,img_path2))
        count +=1
        print(count)

# xml_path = os.listdir(src_xml)
# i = 0
# for xml_path1 in xml_path:
#     xml_doc = etree.parse(os.path.join(src_xml,xml_path1))
#     annotation = xml_doc.getroot()
#     key_object = annotation[5]
#     etree.SubElement(key_object, "pose").text = "Unspecified"
#     etree.SubElement(key_object, "truncated").text = "0"
#     filename = annotation[1]
#     filename.text = xml_path1[:-4] + ".jpg"
#     etree.SubElement(annotation, "path").text = "/home/jdmking/GJH/GG_DATA/image/" + xml_path1[:-4] + ".jpg"
#     if not os.path.exists(xml_dir):
#         os.mkdir(xml_dir)
#     xml_path = os.path.join(xml_dir,xml_path1)
#     doc = etree.ElementTree(annotation)
#     with open(xml_path, "wb+") as file:
#         doc.write(file)
#     i +=1
#     print(i)

