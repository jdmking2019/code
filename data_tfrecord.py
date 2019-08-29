#将数据集以文件夹为类别，转换成tfrecord

import sys
# sys.path.insert(0, '../models/slim/')  models-master research
sys.path.insert(0, '/home/jdmking/models/research/slim/')  # 把后面的路径插入到系统路径中 idx=0
from datasets import dataset_utils
import math
import os
import tensorflow as tf
#  根据list路径  把数据转化为TFRecord
# def convert_dataset(list_path, data_dir, output_dir, _NUM_SHARDS=5):
def convert_dataset(list_path, data_dir, output_dir, _NUM_SHARDS=3):
    fd = open(list_path)
    lines = [line.split() for line in fd]
    fd.close()
    num_per_shard = int(math.ceil(len(lines) / float(_NUM_SHARDS)))
    with tf.Graph().as_default():
        decode_jpeg_data = tf.placeholder(dtype=tf.string)
        decode_jpeg = tf.image.decode_jpeg(decode_jpeg_data, channels=3)
        with tf.Session('') as sess:
            for shard_id in range(_NUM_SHARDS):
                output_path = os.path.join(output_dir,
# 'data_{:05}-of-{:05}.tfrecord'.format(shard_id, _NUM_SHARDS))
                                           'data_{:03}-of-{:03}.tfrecord'.format(shard_id, _NUM_SHARDS))
                tfrecord_writer = tf.python_io.TFRecordWriter(output_path)
                start_ndx = shard_id * num_per_shard
                end_ndx = min((shard_id + 1) * num_per_shard, len(lines))
                for i in range(start_ndx, end_ndx):
                    sys.stdout.write('\r>> Converting image {}/{} shard {}'.format(
                        i + 1, len(lines), shard_id))
                    sys.stdout.flush()
                    image_data = tf.gfile.FastGFile(os.path.join(data_dir, lines[i][0]), 'rb').read()
                    image = sess.run(decode_jpeg, feed_dict={decode_jpeg_data: image_data})
                    height, width = image.shape[0], image.shape[1]
                    example = dataset_utils.image_to_tfexample(
                        image_data, b'jpg', height, width, int(lines[i][1]))
                    tfrecord_writer.write(example.SerializeToString())
                tfrecord_writer.close()
    sys.stdout.write('\n')
    sys.stdout.flush()
train = "/home/jdmking/Desktop/gjh/train/"
val = "/home/jdmking/Desktop/gjh/val"

List_train = "/home/jdmking/Desktop/gjh/list_train.txt"
List_val = "/home/jdmking/Desktop/gjh/list_val.txt"

Data_dir = "/home/jdmking/Desktop/gjh/Train_data"
os.system("mkdir -p {}".format(train))
convert_dataset(List_train, Data_dir, train)
os.system("mkdir -p {}".format(val))
convert_dataset(List_val, Data_dir, val)
