#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @IDE          :PyCharm
# @FileName     :Goods
# @CreatTime    :2022/3/20 15:32 
# @CreatUser    :DaneSun
# @Author       :孙智涵

from django.db import models
class Goods(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    specification = models.CharField(max_length=20,null=True)
    amount = models.IntegerField(default=0)
    operator = models.CharField(max_length=50)
    update_time = models.DateTimeField(auto_now_add=True)
    class Meta:
        app_label = 'app'