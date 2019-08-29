#视频转换为图像，按帧截取

#! -*- coding:utf-8 -*-
import cv2
import numpy as np
from PIL import Image
import os

videos_src_path ="/home/jdmking/Desktop/error_videos/jt3"
videos_save_path ="/home/jdmking/Desktop/error_videos/jt3/images"
videos = os.listdir(videos_src_path)
videos = filter(lambda x: x.endswith('mp4'), videos)
frame_count = 0
for each_video in videos:
    each_video_name, _ = each_video.split('.')
    if not os.path.exists(videos_save_path):
        os.mkdir(videos_save_path)
    each_video_save_full_path = videos_save_path + '/'
    # get the full path of each video, which will open the video tp extract frames
    each_video_full_path = os.path.join(videos_src_path, each_video)
    cap = cv2.VideoCapture(each_video_full_path)
    success = True
    while(success):
        success, frame = cap.read()

        if frame_count % 5 != 0:
        frame_count = frame_count + 1
        continue

        print('Read a new frame: ', success, frame_count)

        if not success:
            continue
        # frame = np.transpose(frame)
        # try:
        #     frame = np.array(Image.fromarray(frame).rotate(270, expand=True))
        # except AttributeError:
        #     print(frame)
        params = []
        params.append(cv2.IMWRITE_JPEG_CHROMA_QUALITY)
        params.append(1)
        cv2.imwrite(os.path.join(each_video_save_full_path, each_video_name) + "_%d.jpg" % frame_count, frame, params)
        frame_count = frame_count + 1
    cap.release()








