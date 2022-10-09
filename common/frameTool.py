# @Time : 2022/10/9 16:42
# @Author : eatingYan
# @module : 根据输入的video和audio进行自动裁剪/匹配
'''

'''
import argparse
import subprocess


def crop_videoandaudio(video_duration,audio_duration,path):#裁剪使音频时长对应 一般裁剪音频来适应视频
    if video_duration < audio_duration:
        command = 'ffmpeg -i {} -ss 0 -t {} {}'.format(path,video_duration, 'temp/temp1.wav')  # 暂时存储
        subprocess.call(command, shell=True)  # Python3 subprocess模块，执行命令行
        new_audio_path = 'temp/temp1.wav'
        return new_audio_path



