#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @IDE          :PyCharm
# @FileName     :GoodApply
# @CreatTime    :2022/3/20 18:09 
# @CreatUser    :DaneSun
# @Author       :孙智涵
from django.db import models


class GoodApply(models.Model):
    id = models.AutoField(primary_key=True)
    goodId = models.IntegerField()
    amount = models.IntegerField()
    staffId = models.IntegerField()
    isPass = models.BooleanField()
    isRead = models.BooleanField()
    update_time = models.DateTimeField(auto_now_add=True)
    class Meta:
        app_label = 'app'