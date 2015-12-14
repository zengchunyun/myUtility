#!/usr/bin/env python
#coding:utf-8

# def zcyReadlines():
#     seek=0
#     while True:
#         with open('account','r+b') as f:
#             f.seek(seek)
#             data = f.readline()
#             if data:
#                 seek = f.tell()
#                 yield data
#             else:
#                 return
#     f.close()
#
# while True:
#     f=open('account','wb')
#     wr=raw_input('input: ')
#     f.write('%s\n'%wr)
#     f.flush()
#     if wr == 'exit':
#         break
#
#
#     for item in zcyReadlines():
#         print item

def realread(account):
    seek=0
    while True:
        f=open(str(account),'rb')
        f.seek(seek)
        readData = f.readline()
        if readData:
            seek=f.tell()
            yield readData
        else:
            return
    f.close()



for i in realread('account'):
    print i.rstrip()


def foo():
    yield 2

a=foo()
print a
for i in a:
    print i