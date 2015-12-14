#!/usr/bin/env python
#coding:utf-8

from mySQLHelper.mySQLHelper import MysqlHelper

class Admin(object):
    def __init__(self):
        self.__helper = MysqlHelper()
    def getOne(self,id):
        sql = "select * from USER where id = %s"
        params = (id,)

        return self.__helper.getOne()

    def loginVerity(self,username,password):

        sql = "select * from USER WHERE username=%s and password=%s"
        params = (username,password)

        return self.__helper.getOne(sql,params)