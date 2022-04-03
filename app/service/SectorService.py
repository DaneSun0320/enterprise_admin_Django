#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @IDE          :PyCharm
# @FileName     :SectorService
# @CreatTime    :2022/3/22 19:55 
# @CreatUser    :DaneSun
# @Author       :孙智涵
from django.db import transaction

from app.models.Sector import Sector
import logging

from app.models.Staff import Staff

logger = logging.getLogger('log')

def getSectorList():
    try:
        with transaction.atomic():
            sector = Sector.objects.filter(id__gt=0).all().values()
            return 1,list(sector)
    except Exception as e:
        logger.exception(e)
        return 0,None

def addSectorService(name):
    try:
        with transaction.atomic():
            sectorList = Sector.objects.all()
            lastId = 0
            if len(sectorList) != 0:
                lastId =  sectorList[::-1][0].id
            Sector.objects.create(id=lastId+1,name=name).save()
            return 1
    except Exception as e:
        logger.exception(e)
        return 0

def deleteSectorService(id):
    try:
        with transaction.atomic():
            # 将待删除部门的全部员工部门修改为待分配状态
            staffInDeleteSector = Staff.objects.filter(sector=id)
            for staff in staffInDeleteSector:
                staff.objects.update(sector = 0)
            Sector.objects.filter(id = id).delete()
        return 1
    except Exception as e:
        logger.exception(e)
        return 0