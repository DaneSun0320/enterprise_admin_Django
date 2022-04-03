#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @IDE          :PyCharm
# @FileName     :__init__.py
# @CreatTime    :2022/2/19 16:36 
# @CreatUser    :DaneSun
# @Author       :孙智涵
import binascii
import socket

from app.utils.playAudio import play


def main():
    try:
        # 1创建套接字
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # 2.绑定一个本地信息
        localaddr = ("192.168.8.100",10000) # 必须绑定自己电脑IP和port
        udp_socket.bind(localaddr)
        play("启动成功")
        # 3.接收数据
        while True:
            recv_data = udp_socket.recvfrom(1024)
            recv_msg = recv_data[0] # 信息内容
            send_addr = recv_data[1] # 信息地址
            # 识别IC卡ID
            if recv_msg[0] == 255 and recv_msg[-1] == 255:
                cardId = recv_msg[1:-2]
                print(binascii.b2a_hex(cardId).decode())
                play("打卡完成")
            elif recv_msg[0] == 0 and recv_msg[-1] == 0:
                tempture = recv_msg[1:-1]
                tempture =int.from_bytes(bytes(tempture), byteorder='big', signed=False)
                if tempture < 37:
                    play("体温正常")
                else:
                    play("体温异常")
        # 5.退出套接字
        udp_socket.close()
    except OSError:
        play("连接失败")
if __name__ == "__main__":
    main()