# 将数据写成txt格式， “path” “类别”
import os
src_path = "/home/jdmking/AnGang_work/chaoyang/noise_annotations"
train_txt = "/home/jdmking/AnGang_work/chaoyang/train.txt"
filename = os.listdir(src_path)
label = "0"
def create_txt(Img_dir,label):
    file_dir = Img_dir.split("/")[-2]
    file_dir1 = Img_dir.split("/")[-1]
    listfile = os.listdir(Img_dir)
    for line in listfile:
        filepath = os.path.join(file_dir,file_dir1,line)
        with open(train_txt,"a+") as f:
            f.write(filepath + " " + label+"\n")
create_txt(src_path,label)
