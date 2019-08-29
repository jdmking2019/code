per_path = "/home/jdmking/caffe/examples/imagenet/image/train_p.txt"
bg_path = "/home/jdmking/caffe/examples/imagenet/image/train_b.txt"
combine_path = "/home/jdmking/caffe/examples/imagenet/image/train_c.txt"
shuffer_path = "/home/jdmking/caffe/examples/imagenet/image/train_s.txt"
count = 0
count1 = 0
with open(per_path,"rb+") as pf:
    data_p = pf.readlines()
    with open(bg_path,"rb+") as bf:
        data_b = bf.readlines()

with open(combine_path,"wb") as cf:
    for data in data_b:
        cf.write(data)
    for data1 in data_p:
        cf.write(data1)
    cf.close()

with open(combine_path, "rb+") as cf:
    with open(shuffer_path,"wb") as sf:
        data_c = cf.readlines()
        data_set = set(data_c)
        for data in data_set:
            sf.write(data)
            count1 += 1
            print("shuffer_write %s data" % str(count1))


