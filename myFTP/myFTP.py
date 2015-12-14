#!/usr/bin/env python
#coding:utf-8

import os
import time
import subprocess


class MyFTP(object):
    def __init__(self):
        pass

    def put(self,destination):
        print 'put'


    def readFile(self,filename,chunkSize):
        self.fileName = filename
        self.chunkSize = chunkSize

        fileObject = open(self.fileName,'rb')
        while True:
            chunk = fileObject.read(chunkSize)
            print chunk
            if not chunk:
                break
            yield chunk
        fileObject.close()


    def get(self,*source):
        self.files = source


        fileName = self.files
        result=os.popen('ls %s'%fileName)

        for file in result:
            # file=file.split('\n')[0]
            file=file.rstrip()
            print file
            time.sleep(0.4)
            # baseName = os.popen('basename %s'%file).read().split('\n')[0]
            baseName = os.popen('basename %s'%file).read().rstrip()

            fileTemp = open('/tmp/%s'%baseName,'a+b')
            tempOpen=open('%s'%file,'rb')

            getLines = tempOpen.read()
            print getLines
            fileTemp.writelines(getLines)

            fileTemp.close()
            tempOpen.close()



    def record(self):
        print 'log'

    def ls(self,*command):
        self.command = command
        PIPE = subprocess.PIPE
        p = subprocess.Popen(self.command, shell=True,
                                stdin=PIPE, stdout=PIPE,
                                stderr=PIPE,close_fds=True)
        return p.stdout,p.stderr

    def ll(self,*command):
        self.command = command
        PIPE = subprocess.PIPE
        p = subprocess.Popen(self.command, shell=True,
                                 bufsize=1, stdin=PIPE, stdout=PIPE,
                                 stderr=PIPE,close_fds=True)
        print p.stdin
        print p.stdout
        print p.stderr.read()

if __name__ == '__main__':
    ftp = MyFTP()
    result = ftp.ls(str('las -l'))
    print result[0].read()
    print result[1].read()