#!/usr/bin/env python
#coding:utf-8


import SocketServer
from loginCheck.myLoginCheck import Admin
from myFTP.myFTP import MyFTP
import time


class MyRequestHandler(SocketServer.BaseRequestHandler):

    def setup(self):
        pass
    def handle(self):
        print time.strftime('%Y-%m-%d %H:%M:%S') + ' %s' %str(self.request)
        print time.strftime('%Y-%m-%d %H:%M:%S') + ' %s' %str(self.client_address)
        print time.strftime('%Y-%m-%d %H:%M:%S') + ' %s' %str(self.server)


        conn = self.request
        try:
            if self.loginCheck():
                conn.send('Login success!')
                flag = True
            else:
                conn.send('Login failed!')
                flag = False
                conn.close()

            while flag:
                data = conn.recv(1024)
                if data == 'ACK':
                    print time.strftime('%Y-%m-%d %H:%M:%S') + ' 客户端断开连接 ... '
                    break
                print time.strftime('%Y-%m-%d %H:%M:%S') + ' 传过来的命令 %s'%data
                result = MyFTP().ls(str(data))
                retries = 1
                while True:
                    readFile = result[0].read()
                    if not readFile and retries == 1:
                        conn.sendall(result[1].read())
                        print time.strftime('%Y-%m-%d %H:%M:%S') + ' 读取完毕'
                        break
                    time.sleep(0.01)
                    conn.sendall(readFile)
                    retries += 1
                    if not readFile:
                        print time.strftime('%Y-%m-%d %H:%M:%S') + ' 读取完毕'
                        break
                time.sleep(0.4)
                conn.send('FIN')
            conn.close()

        except Exception as e:
            print e

    def loginCheck(self):
        conn = self.request
        conn.send('请输入用户名:')
        username = conn.recv(1024)
        conn.send('请输入密码:')
        password = conn.recv(1024)

        login = None
        if username and password:
            try:
                login = Admin().loginVerity(username,password)

            except SystemExit as e:
                print e
                conn.close()

        if not login:
            return False
        else:
            return True