#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @IDE          :PyCharm
# @FileName     :play
# @CreatTime    :2022/4/2 14:34 
# @CreatUser    :DaneSun
# @Author       :孙智涵
import pyaudio
import wave
import os

def play(name):
    chunk = 1024
    path= os.path.abspath(os.path.dirname(__file__))
    wf = wave.open(path +'/{}.wav'.format(name), 'rb')
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    data = wf.readframes(chunk)
    while len(data) > 0:
        stream.write(data)
        data = wf.readframes(chunk)
    stream.stop_stream()
    stream.close()
    p.terminate()