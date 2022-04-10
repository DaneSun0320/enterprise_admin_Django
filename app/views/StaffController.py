#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @IDE          :PyCharm
# @FileName     :StaffController
# @CreatTime    :2022/3/30 18:56 
# @CreatUser    :DaneSun
# @Author       :孙智涵
import json
import logging

from django.http import HttpResponse

from app.service.StaffService import getStaffList, writeCardService, loginService, updateLevelService, \
    deleteStaffService, updateStaffService, updatePasswordService, addStaffService
from app.utils.DateEncoder import DateEncoder
from app.utils.JWTUtil import create_token
from app.utils.readCard import readCard

logger = logging.getLogger('log')


def getStaff(request):
    if request.method == "GET":
        status, staffList = getStaffList()
        res = {
            "status": status,
            "data": staffList
        }
        return HttpResponse(json.dumps(res, ensure_ascii="utf-8", cls=DateEncoder), content_type="application/json")


def writeCard(request):
    if request.method == "POST":
        postBody = json.loads(request.body)
        id = postBody["id"]
        status, cardId = readCard()
        if status == 1:
            writeCardService(id, cardId)
        res = {
            "status": status
        }
    return HttpResponse(json.dumps(res, ensure_ascii="utf-8", cls=DateEncoder), content_type="application/json")


def updateLevel(request):
    if request.method == "POST":
        postBody = json.loads(request.body)
        logger.debug(postBody)
        id = postBody["id"]
        isAdmin = postBody["isAdmin"]
        status = updateLevelService(id, isAdmin)
        res = {
            "status": status
        }
        return HttpResponse(json.dumps(res, ensure_ascii="utf-8", cls=DateEncoder), content_type="application/json")

def addStaff(request):
    if request.method == "POST":
        postBody = json.loads(request.body)
        name = postBody["name"]
        sector = postBody["sector"]
        age = postBody["age"]
        sex = postBody["sex"]
        phone = postBody["phone"]
        email = postBody["email"]
        position = postBody["position"]
        status = addStaffService(name = name,sex = sex, phone = phone, age = age, email = email,sector = sector, position = position)
        res = {
            "status":status
        }
        return HttpResponse(json.dumps(res, ensure_ascii="utf-8", cls=DateEncoder), content_type="application/json")

def deleteStaff(request):
    if request.method == "POST":
        postBody = json.loads(request.body)
        id = postBody["id"]
        status = deleteStaffService(id)
        res = {
            "status": status
        }
        return HttpResponse(json.dumps(res, ensure_ascii="utf-8", cls=DateEncoder), content_type="application/json")


def updateStaff(request):
    if request.method == "POST":
        postBody = json.loads(request.body)
        id = postBody["id"]
        name = postBody["name"]
        sector = postBody["sector"]
        sex = postBody["sex"]
        age = postBody["age"]
        phone = postBody["phone"]
        email = postBody["email"]
        position = postBody["position"]
        status = updateStaffService(id=id,
                                    name=name,
                                    sex=sex,
                                    age=age,
                                    phone=phone,
                                    email=email,
                                    sector=sector,
                                    position=position)
        res = {
            "status": status
        }
        return HttpResponse(json.dumps(res, ensure_ascii="utf-8", cls=DateEncoder), content_type="application/json")

def login(request):
    if request.method == "POST":
        postBody = json.loads(request.body)
        id = postBody["id"]
        password = postBody["password"]
        status, staff = loginService(id, password)
        if status == 1:
            res = {
                "status": status,
                "token": create_token(staff["id"]),
                "id": staff["id"],
                "name": staff["name"],
                "sector": staff["sector"],
                "level": staff["level"],
                "token": create_token(staff["id"])
            }
        else:
            res = {
                "status": status
            }
        return HttpResponse(json.dumps(res, ensure_ascii="utf-8", cls=DateEncoder), content_type="application/json")
def verify (request):
    if request.method == "POST":
        postBody = json.loads(request.body)
        id = postBody["id"]
        status, staff = loginService(id, "")
        if status == 1:
            res = {
                "status": status,
                "token": create_token(staff["id"]),
                "id": staff["id"],
                "name": staff["name"],
                "sector": staff["sector"],
                "level": staff["level"],
                "token": create_token(staff["id"])
            }
        else:
            res = {
                "status": status
            }
        return HttpResponse(json.dumps(res, ensure_ascii="utf-8", cls=DateEncoder), content_type="application/json")
def updatePassword(request):
    if request.method == "POST":
        postBody = json.loads(request.body)
        id = postBody["id"]
        oldPassword = postBody["oldPassword"]
        newPassword = postBody["newPassword"]
        status = updatePasswordService(id, oldPassword, newPassword)
        res = {
            "status": status
        }
        return HttpResponse(json.dumps(res, ensure_ascii="utf-8", cls=DateEncoder), content_type="application/json")

def verifyToken(request):
    if request.method == "GET":
        header = request.META.get("Authorization")
        logger.debug("用户请求头为：{}".format(header))
        if header is None:
            res = {
                "status": 0
            }
            return HttpResponse(json.dumps(res, ensure_ascii="utf-8", cls=DateEncoder), content_type="application/json")
        token = header.split(" ")[1]
        status, id = verify(token)
        if status == 1:
            res = {
                "status": status,
                "id": id
            }
        else:
            res = {
                "status": status
            }
        return HttpResponse(json.dumps(res, ensure_ascii="utf-8", cls=DateEncoder), content_type="application/json")