#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @IDE          :PyCharm
# @FileName     :OutsideInfo
# @CreatTime    :2022/3/29 19:40 
# @CreatUser    :DaneSun
# @Author       :孙智涵
import datetime

from django.db import models
class OutsideInfo(models.Model):
    id = models.AutoField(primary_key=True)
    staffId = models.IntegerField()
    province = models.CharField(max_length=10)
    city = models.CharField(max_length=20)
    district = models.CharField(max_length=10)
    applyDate = models.DateTimeField(auto_now_add=True)
    startDate = models.DateField()
    endDate = models.DateField()
    approveStatus = models.SmallIntegerField(default=0)
    status = models.IntegerField(default=0)

class OutsideInfoView(models.Model):
    id = models.AutoField(primary_key=True)
    staffId = models.IntegerField()
    name  = models.CharField(max_length=30)
    sectorName = models.CharField(max_length=30)
    province = models.CharField(max_length=10)
    city = models.CharField(max_length=20)
    district = models.CharField(max_length=10)
    applyDate = models.DateTimeField(auto_now_add=True)
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()
    approveStatus = models.SmallIntegerField(default=0)
    status = models.IntegerField(default=0)
    class Meta(object):
        db_table = 'outsideinfoview'
        managed = False