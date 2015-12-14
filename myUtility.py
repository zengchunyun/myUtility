#!/usr/bin/env python
#coding:utf-8


import SocketServer
import socket
from main.myServer import MyRequestHandler


def main():
    ip_port = ('0.0.0.0',9999)
    server = SocketServer.ThreadingTCPServer(ip_port,MyRequestHandler)
    server.serve_forever(poll_interval=0.2)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt as e:
        print '服务正在退出 ...'
    except socket.error as e:
        print '地址被占用'
    except TypeError as e:
        print '数据类型错误'
