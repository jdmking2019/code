#数据转换为txt格式， “dataname”
import os
src_path = "/home/jdmking/AnGang_work/GJH/gjh/data_add/noise_annotations"
img_path = os.listdir(src_path)
save_path = "/home/jdmking/AnGang_work/GJH/gjh/data_add/train.txt"

for img_path1 in img_path:
    if img_path1[-4:] == ".xml":
        img_path_txt = img_path1[:-4]
        with open(save_path,"a+") as f:
            f.write(img_path_txt + "\n")
