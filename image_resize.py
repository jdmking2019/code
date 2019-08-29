#改变图像大小，同时更改xml

import os
from PIL import Image
from lxml import etree

src_path = "/home/jdmking/Desktop/images/"
src_xml_path = "/home/jdmking/Desktop/ann/"

save_img_path = "/home/jdmking/AnGang_work/chaoyang/images1/"
save_xml_path = "/home/jdmking/AnGang_work/chaoyang/annotations1/"

def Img_resize(img_path,xml_path,save_img_path,save_xml_path):
    # save_filename = src_path.split("/")[-1]
    print(os.path.join(src_path,img_path))
    Img = Image.open(os.path.join(src_path,img_path))
    xml_root = etree.parse(xml_path)
    annotation = xml_root.getroot()
    path = annotation[2]
    size = annotation[4]
    width = float(size[0].text)
    height = float(size[1].text)

    ratio_width = 500 / width
    ratio_height = 500 / height

    New_img = Img.resize((500, 500), Image.ANTIALIAS)

    All_bndbox = [obj[4] for obj in annotation[6:]]
    for bndbox in All_bndbox:
        bndbox[0].text = str(int(int(bndbox[0].text) * ratio_width))
        bndbox[1].text = str(int(int(bndbox[1].text) * ratio_height))
        bndbox[2].text = str(int(int(bndbox[2].text) * ratio_width))
        bndbox[3].text = str(int(int(bndbox[3].text) * ratio_height))

    size[0].text = str(500)
    size[1].text = str(500)
    path.text = os.path.join(save_img_path,img_path)

    New_img.save(save_img_path + img_path)
    xml_root.write(save_xml_path + img_path[:-4] + ".xml")

img_filename = os.listdir(src_path)
count = 0
for img_path in img_filename:
    xml_path = os.path.join(src_xml_path, img_path[:-4] + ".xml")
    # img_path = os.path.join(src_path,img_path1)
    Img_resize(img_path,xml_path,save_img_path,save_xml_path)
    count += 1
    print("save %f image" % count)



