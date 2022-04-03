#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @IDE          :PyCharm
# @FileName     :RiskRegion
# @CreatTime    :2022/4/2 22:04 
# @CreatUser    :DaneSun
# @Author       :孙智涵

# 创建一个model，用于描述风险区域
from django.db import models
class RiskRegion(models.Model):
    id = models.AutoField(primary_key=True)
    province = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    district = models.CharField(max_length=20)
    riskLevel = models.IntegerField()
    class Meta:
        app_label = 'app'
