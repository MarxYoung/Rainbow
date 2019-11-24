# -*- coding:utf-8 -*-
import socket
import paramiko
import os
import tkinter as tk
from tkinter import filedialog
import json


# 客户机类
class Client():
    # 初始化
    ipadd = ''
    file_nrecv = {}
    sftp_addr = ('47.102.133.201', 22)
    socket_addr = ('47.102.133.201', 7776)

    # 发送文件
    def sendData(self,sendfile):
        #接收用户名
        while True:
            self.socket_connect.send(input("接收用户名：").encode('utf-8'))
            if self.socket_connect.recv(1024).decode() == 'YES':
                break
            else:
                print("无此用户，请重新输入！")

        # sftp创建连接
        self.sftp_connect = paramiko.Transport(self.sftp_addr)
        self.sftp_connect.connect(username='root', password='zxcvbnm,./12345')
        self.sftp = paramiko.SFTPClient.from_transport(self.sftp_connect)  # 如果连接需要密钥，则要加上一个参数，hostkey="密钥"

        filename = (str(sendfile).split('/'))[-1]  # 获取文件名
        #self.socket_connect.send(filename.encode('utf-8')) # 发送文件名
        #sendname = self.socket_connect.recv(1024).decode('utf-8') #重命名
        self.remotefile = '/root/test'
        self.remotefile = self.remotefile + filename  # 获取服务器存储路径
        try:
            self.sftp.put(sendfile, self.remotefile)  # 将本地的local文件上传至服务器的remotefile
            #self.socket_connect.send('0020'.encode('utf-8'))
        except:
            #self.socket_connect.send('0022'.encode('utf-8'))
            self.sftp_connect.close()  # 关闭连接
            return False
        self.sftp_connect.close()  # 关闭连接
        return True

    #失败重传
    def sendFailed(self,resend):
        if(resend == True):
            self.sendData()


    # 接收文件
    def recvData(self):
        self.sftp_connect = paramiko.Transport(self.sftp_addr)
        self.sftp_connect.connect(username='root', password='zxcvbnm,./12345')
        sftp = paramiko.SFTPClient.from_transport(self.sftp_connect)  # 如果连接需要密钥，则要加上一个参数，hostkey="密钥"
        while True:
            self.recv_name = input('接收的文件名：')
            try:
                self.file_detail = self.file_nrecv.get(self.recv_name)  # 获取文件详细信息
                break
            except:
                print('文件名输入错误！，请重新输入')
        self.remotefile = self.file_detail.get('path')  # 获取文件路径
        self.remotefile = self.remotefile + self.recv_name  # 获取服务器存储路径
        print('服务器路径：', self.remotefile)
        application_window = tk.Tk()  # 打开窗口
        self.recvfile = filedialog.asksaveasfilename(initialdir=os.path.abspath('.'))  # 打开文件对话框选择文件
        application_window.destroy()  # 关闭窗口
        print('本地地址：', self.recvfile)
        sftp.get(self.remotefile, self.recvfile)  # 将Linux上的/root/Linux.txt下载到本地
        #sftp.remove(self.remotefile)
        print('接收成功！')
        #self.socket_connect.send() # ***************************************************************************
        self.sftp_connect.close()  # 关闭连接

    # tcp连接验证用户信息
    def sendUData(self):
        self.socket_connect = socket.socket()  # tcp套接字
        self.socket_connect.connect(self.socket_addr)  # tcpli连接
        while True:
            self.socket_connect.send(('###' + input('Username：')).encode('utf-8'))  # 输入用户名
            self.socket_connect.send(('***' + input('Password：')).encode('utf-8'))  # 输入密码
            try:
                ans = self.socket_connect.recv(9).decode('utf-8')
                print(ans)
            except:
                print("error")
            if ans == 'Matched!!':
                print('登录成功!')
                self.file_nrecv = json.loads(self.socket_connect.recv(1024).decode('utf-8'))  # 未接收的文件列表
                print('未接受的文件：', self.file_nrecv)
                for key in self.file_nrecv:
                    print("文件名:",key)
                    for skey in self.file_nrecv[key]:
                        print(skey,':',self.file_nrecv[key][skey])
                return
            else:
                print('用户名或密码错误！请重新输入：')


if __name__ == '__main__':
    # tcp连接验证用户信息

    # 创建client类
    client = Client()
    client.sendUData()

    # 功能选择
    while True:
        select = input('选择功能，发送为1，接收为2,退出为bye：')
        if select == '1':  # 发送文件
            client.sendData()
        elif select == '2':  # 接收文件
            client.recvData()
        elif select == 'bye':  # 退出
            break
    client.socket_connect.close()