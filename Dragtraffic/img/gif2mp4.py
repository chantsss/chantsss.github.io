# -*- coding: utf-8 -*-
import os
from moviepy.editor import *

# 定义输入和输出文件夹路径
input_folder = '/home/sheng/chantsss.github.io/Dragtraffic/img'
output_folder = '/home/sheng/chantsss.github.io/Dragtraffic/videos'

# 遍历输入文件夹中的所有文件
for file_name in os.listdir(input_folder):
    if file_name.endswith('.GIF'):
        # 构造输入和输出文件路径
        input_path = os.path.join(input_folder, file_name)
        output_path = os.path.join(output_folder, file_name.replace('.GIF', '.mp4'))

        # 使用moviepy库将gif转换为mp4
        clip = VideoFileClip(input_path)
        clip.write_videofile(output_path)