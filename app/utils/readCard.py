#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @IDE          :PyCharm
# @FileName     :writeCard
# @CreatTime    :2022/4/1 22:04 
# @CreatUser    :DaneSun
# @Author       :孙智涵
import _thread
import binascii
import logging
import os
import re
import socket
from app.utils.playAudio import play

logger = logging.getLogger('log')

def kill_process():
    ret = os.popen("netstat -nao|findstr 10000")
    str_list = ret.read()
    ret_list = re.split(' ',str_list)
    try:
        process_pid = list(ret_list[0].split())[-1]
        os.popen('taskkill /pid ' + str(process_pid) + ' /F')
        logger.debug("端口已被释放")
    except:
        logger.debug("端口未被使用")

def readCard():
    try:
        kill_process()
        # 1创建套接字
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udp_socket.settimeout(10)
        # 2.绑定一个本地信息
        localaddr = ("192.168.8.100",10000) # 必须绑定自己电脑IP和port
        udp_socket.bind(localaddr)
        recv_data = udp_socket.recvfrom(1024)
        recv_msg = recv_data[0] # 信息内容
        send_addr = recv_data[1] # 信息地址
        # 识别IC卡ID
        if recv_msg[0] == 255 and recv_msg[-1] == 255:
            cardId = recv_msg[1:-2]
            cardId = binascii.b2a_hex(cardId).decode()
            _thread.start_new_thread (play,("读卡",))
            udp_socket.close()
            return 1,cardId
        udp_socket.close()
        return 0,None
        # 5.退出套接字
    except socket.timeout:
        _thread.start_new_thread (play,("超时",))
        return -2,None
    except OSError as e:
        logger.exception(e)
        _thread.start_new_thread (play,("连接失败",))
        return -1,None