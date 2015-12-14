#!/usr/bin/env python
#coding:utf-8

import socket
import time
import os

ip_port = ('127.0.0.1',9999)
sock = socket.socket()
try:
    sock.connect(ip_port)
except Exception as e:
    print '服务器连接错误 ...'
    exit(1)

#设置存储当前缓冲区文件名字,取当前时间戳为标记
recvfile = time.time()
flag = True
session = 0
seek=0

def Readlines(file):
    global seek
    # seek=0
    while True:
        f = open(file,'rb')
        f.seek(seek)
        readData = f.readline()
        if readData:
            seek = f.tell()
            yield readData
        else:
            return
    f.close()



try:
    while flag:
        if flag:
            data = sock.recv(1024)
            print data

        if 'Login failed' in data:
            print 'Good Bye ...'
            break

        elif 'Login success' in data:
            command = False
            while flag:
                if command:
                    recv = 20
                    recvData = open(str(recvfile),'a+b')
                    while recv:
                        data = sock.recv(4096)
                        time.sleep(0.1)
                        if 'FIN' in data:
                            # print '接收完成'
                            recv = -1
                            break
                        else:
                            recv -= 1
                            recvData.write(str(data))
                        recvData.flush()
                    recvData.close()
                    for i in Readlines('%s'%recvfile):
                        print i.rstrip()

                command = raw_input('[localhost: ~] ')
                if command:
                    sock.send(command)
                    if command == 'exit':
                        flag = False
                        sock.send('ACK')
                        print 'Good Bye ...'
                        sock.close()
                        break

        else:
            if not session:
                session = raw_input('用户名:')
            if len(session) < 1:
                flag = False
                loginRetry = 1
                while not flag and loginRetry < 3:

                    print '用户名不能为空!!!'
                    session = raw_input('用户名: ')

                    if len(session) > 1:
                        flag = True

                    loginRetry += 1

                if len(session):
                    flag = True
                else:
                    sock.close()
                    flag = False

            if len(session) > 1:
                sock.send(session)
                data = sock.recv(1096)
                print data
                session = raw_input('密码:')
                if len(session) < 1:
                    flag = False
                    loginRetry = 1
                    while not flag and loginRetry < 3:
                        print '密码不能为空!!!'
                        session = raw_input('密码: ')
                        if len(session) >1:
                            sock.send(session)
                            flag = True
                            break

                        loginRetry += 1
                else:
                    sock.send(session)
                    flag = True
except KeyboardInterrupt as e:
    print '\n感谢您的使用!'
except TypeError as e:
    print '数据类型错误'
except Exception as e:
    print '服务器正在维护 ,请稍后再试 ...' + e

finally:
    sock.close()
    if os.path.isfile(str(recvfile)):
        os.remove(str(recvfile))