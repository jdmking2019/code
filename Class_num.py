from lxml import etree
import os
#查看数据集中类别的数量，分析是否数据平衡
xml_src = "/home/jdmking/GJH/gjh/data_add/noise_annotations"
xml_filename = os.listdir(xml_src)
XML_PATH = [os.path.join(xml_src,xml_filename1) for xml_filename1 in xml_filename]
Class_list = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","G","H","I","J",
              "K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
MAP_list = []

def XML_Input(xml_path,MAP_list):
    doc = etree.parse(xml_path)
    root = doc.getroot()
    for i in range(6,len(root)):
        if root[i][0].text in Class_list:
            MAP_list.append(root[i][0].text)
            # print(root[i][0].text)
def List_num(MAP_list):
    res = {}
    for i in MAP_list:
        res[i] = res.get(i, 0) + 1
        # print(res[i])
    print([k for k in res.keys()])
    print([v for v in res.values()])
for xml_path in XML_PATH:
    XML_Input(xml_path,MAP_list)

List_num(MAP_list)


