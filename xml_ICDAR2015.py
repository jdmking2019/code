#将xml文件转成为ICDAR2015数据集格式

import os
from lxml import etree
import numpy as np

src_xml = "/home/jdmking/AnGang_work/GJH/gjh/src_image/ANN"
txt_dir = "/home/jdmking/AnGang_work/GJH/gjh/src_image/gt/"

xml_listdir = os.listdir(src_xml)

xml_listpath = [os.path.join(src_xml,xml_listdir1) for xml_listdir1 in xml_listdir]

def xml_out(xml_path):
    gt_lines = []
    ET = etree.parse(xml_path)
    objs = ET.findall("object")
    for ix,obj in enumerate(objs):
        name = obj.find("name").text
        robox = obj.find("robndbox")
        cx = int(float(robox.find("cx").text))
        cy = int(float(robox.find("cy").text))
        w = int(float(robox.find("w").text))
        h = int(float(robox.find("h").text))
        angle = float(robox.find("angle").text)

        wx1 = cx - int(0.5 * w)
        wy1 = cy - int(0.5 * h)

        wx2 = cx + int(0.5 * w)
        wy2 = cy - int(0.5 * h)

        wx3 = cx - int(0.5 * w)
        wy3 = cy + int(0.5 * h)

        wx4 = cx + int(0.5 * w)
        wy4 = cy + int(0.5 * h)

        x1 = int((wx1 - cx) * np.cos(angle) - (wy1 - cy) * np.sin(angle) + cx)
        y1 = int((wx1 - cx) * np.sin(angle) - (wy1 - cy) * np.cos(angle) + cy)

        x2 = int((wx2 - cx) * np.cos(angle) - (wy2 - cy) * np.sin(angle) + cx)
        y2 = int((wx2 - cx) * np.sin(angle) - (wy2 - cy) * np.cos(angle) + cy)

        x3 = int((wx3 - cx) * np.cos(angle) - (wy3 - cy) * np.sin(angle) + cx)
        y3 = int((wx3 - cx) * np.sin(angle) - (wy3 - cy) * np.cos(angle) + cy)

        x4 = int((wx4 - cx) * np.cos(angle) - (wy4 - cy) * np.sin(angle) + cx)
        y4 = int((wx4 - cx) * np.sin(angle) - (wy4 - cy) * np.cos(angle) + cy)

        lines = str(x1)+","+str(y1)+","+str(x2)+","+str(y2)+","+\
                str(x3)+","+str(y3)+","+str(x4)+","+str(y4)+","+str(name)+"\n"
        gt_lines.append(lines)
        return gt_lines

def main():
    count = 0
    for xml_dir in xml_listdir:
        gt_lines = xml_out(os.path.join(src_xml,xml_dir))
        txt_path = "gt_" + xml_dir[:-4] + ".txt"
        with open(os.path.join(txt_dir,txt_path),"a+") as fd:
            fd.writelines(gt_lines)
        count +=1
        print("Write file %s" % str(count))

if __name__ == "__main__":
    main()







