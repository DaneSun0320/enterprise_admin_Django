#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @IDE          :PyCharm
# @FileName     :User
# @CreatTime    :2022/4/5 22:50 
# @CreatUser    :DaneSun
# @Author       :孙智涵
from django.db import models

class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    password = models.CharField(max_length=128)
