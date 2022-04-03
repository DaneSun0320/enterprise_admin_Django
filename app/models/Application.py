#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @IDE          :PyCharm
# @FileName     :Application
# @CreatTime    :2022/3/21 18:37 
# @CreatUser    :DaneSun
# @Author       :孙智涵
from django.db import models


class Application(models.Model):
    id = models.AutoField(primary_key=True)
    goodId = models.IntegerField()
    amount = models.IntegerField()
    sectorId = models.IntegerField()
    applyTime = models.DateTimeField(auto_now_add=True)
    approveTime = models.DateTimeField(null=True)
    status = models.SmallIntegerField(default=0)
    class Meta:
        app_label = 'app'

class ApplicationView(models.Model):
    id = models.AutoField(primary_key=True)
    goodId = models.IntegerField()
    amount = models.IntegerField()
    goodName = models.CharField(max_length=50)
    sectorId = models.IntegerField()
    sectorName= models.CharField(max_length=50)
    applyTime = models.DateTimeField(auto_now_add=True)
    approveTime = models.DateTimeField(null=True)
    status = models.SmallIntegerField(default=0)
    class Meta(object):
        db_table = 'applicationview'
        managed = False
