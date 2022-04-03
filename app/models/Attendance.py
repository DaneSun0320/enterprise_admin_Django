#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @IDE          :PyCharm
# @FileName     :Attendance
# @CreatTime    :2022/2/19 16:50 
# @CreatUser    :DaneSun
# @Author       :孙智涵
from django.db import models


class Attendance(models.Model):
    id = models.AutoField(primary_key=True)
    staffId = models.IntegerField()
    tempture = models.FloatField()
    checkTempture = models.FloatField(null=True)
    operator = models.CharField(max_length=50, null=True)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True)

    class Meta:
        app_label = 'app'


class AttendanceView(models.Model):
    id = models.AutoField(primary_key=True)
    staffId = models.IntegerField()
    name = models.CharField(max_length=30)
    sector = models.CharField(max_length=30)
    uid = models.BigIntegerField()
    tempture = models.FloatField()
    checkTempture = models.FloatField(null=True)
    operator = models.CharField(max_length=50, null=True)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True)

    class Meta(object):
        db_table = 'attendanceview'
        managed = False
