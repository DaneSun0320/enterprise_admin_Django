#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @IDE          :PyCharm
# @FileName     :Sector
# @CreatTime    :2022/3/20 20:06 
# @CreatUser    :DaneSun
# @Author       :孙智涵
from django.db import models


class Sector(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
