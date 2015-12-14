#!/usr/bin/env python
#coding:utf-8

import MySQLdb
import re





class MysqlHelper(object):

    def __init__(self):
        try:
            dbConfFile = open('conf',mode='r')
            host = None
            user = None
            passwd = None
            port = None
            db = None
            for option in dbConfFile.readlines():

                if ''.join(re.findall('^host=(.*)',option)):
                    host = ''.join(re.findall('^host=(.*)',option))


                if ''.join(re.findall('^user=(.*)',option)):
                    user = ''.join(re.findall('^user=(.*)',option))


                if ''.join(re.findall('^passwd=(.*)',option)):
                    passwd = ''.join(re.findall('^passwd=(.*)',option))


                if ''.join(re.findall('^port=(.*)',option)):
                    port = ''.join(re.findall('^port=(.*)',option))


                if ''.join(re.findall('^db=(.*)',option)):
                    db = ''.join(re.findall('^db=(.*)',option))


            dbConfFile.close()

            if host and user and passwd and db and port:
                connectionString=dict(host=host,user=user,passwd=passwd,port=int(port),db=db)
            else:
                raise Exception('配置文件有误')

        except Exception as e:
            exit(e)

        self.__myConnectionString = connectionString

    def getDict(self,sql,params):

        myConnection = MySQLdb.connect(**self.__myConnectionString)
        cur=myConnection.cursor(cursorclass=MySQLdb.cursors.DictCursor)

        reCount = cur.execute(sql,params)
        data = cur.fetchall()

        cur.close()
        myConnection.close()

        return data

    def getOne(self,sql,params):
        myConnection = MySQLdb.connect(**self.__myConnectionString)
        cur = myConnection.cursor(cursorclass=MySQLdb.cursors.DictCursor)

        reCount = cur.execute(sql,params)
        data = cur.fetchone()

        cur.close()
        myConnection.close()

        return data