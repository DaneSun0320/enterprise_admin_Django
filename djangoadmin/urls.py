
from django.urls import path
from app.views import GoodsController, AttendanceController, SectorController, OutsideInfoController, StaffController

# 共 29 个路由
urlpatterns = [
    path('login/', StaffController.login),
    path('updatepassword/', StaffController.updatePassword),
    # 库存api
    path('goods/', GoodsController.getGoods),
    path('addgoods/',GoodsController.addGoods),
    path('deletegoods/',GoodsController.deleteGoods),
    path('application/',GoodsController.getApplication),
    path('applygoods/',GoodsController.applyGoods),
    path('approvegoods/',GoodsController.approveGoods),
    # 出勤api
    path('todayattendance/',AttendanceController.getTodayAttendance),
    path('allattendance/',AttendanceController.getAllAttendance),
    path('todayexcept/',AttendanceController.getTodayExceptAttendance),
    path('allexcept/',AttendanceController.getAllExceptAttendance),
    path('checktempture/',AttendanceController.checkTempture),
    # 部门
    path('sectorlist/',SectorController.getSector),
    path('addsectorlist/',SectorController.addSector),
    path('deletesectorlist/',SectorController.deleteSector),
    # 外出
    path('outsideinfo/',OutsideInfoController.getOutside),
    path('outsidenumber/',OutsideInfoController.getNumber),
    path('outsideapprove/',OutsideInfoController.approveOutside),
    path('updateriskLevel/',OutsideInfoController.updateRiskLevel),
    # 风险地区
    path('riskregion/',OutsideInfoController.getRiskRegion),
    path('addriskregion/',OutsideInfoController.addRiskRegion),
    path('updateriskregion/',OutsideInfoController.updateRiskLevel),
    path('deleteriskregion/',OutsideInfoController.deleteRiskRegion),
    # 职工
    path('stafflist/',StaffController.getStaff),
    path('writecard/',StaffController.writeCard),
    path('addstaff/',StaffController.addStaff),
    path('updatelevel/',StaffController.updateLevel),
    path('deletestaff/',StaffController.deleteStaff),
    path('updatestaff/',StaffController.updateStaff)
]
