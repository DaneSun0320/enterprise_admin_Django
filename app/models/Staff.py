#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @IDE          :PyCharm
# @FileName     :Staff
# @CreatTime    :2022/2/19 16:37 
# @CreatUser    :DaneSun
# @Author       :孙智涵
from django.db import models

class Staff(models.Model):
    id = models.BigAutoField(primary_key=True)
    uid = models.CharField(max_length=80,null=True)
    name = models.CharField(max_length=30)
    sex = models.BooleanField()
    age = models.SmallIntegerField()
    phone = models.CharField(max_length=11)
    email = models.EmailField()
    sector = models.IntegerField()
    position = models.CharField(max_length=20)
    level = models.IntegerField()
    class Meta:
        app_label = 'app'

class StaffView(models.Model):
    id = models.BigAutoField(primary_key=True)
    uid = models.CharField(max_length=80)
    name = models.CharField(max_length=30)
    sex = models.BooleanField()
    age = models.SmallIntegerField()
    phone = models.CharField(max_length=11)
    email = models.EmailField()
    sector = models.IntegerField()
    sectorName = models.CharField(max_length=30)
    position = models.CharField(max_length=20)
    level = models.IntegerField()
    class Meta(object):
        db_table = 'staffview'
        managed = False