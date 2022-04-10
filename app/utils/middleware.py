import logging

from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin

from app.models.Staff import Staff
from app.utils.JWTUtil import verify
logger = logging.getLogger('log')
# 免验证路径
NOVERIFY_CHECK_PATH = [
    '/login/',
]
# 超级管理员验证路径
SUPER_CHECK_PATH = [
    '/addsectorlist/',
    '/deletesectorlist/',
    '/updatelevel/',
    '/approvegoods/',
]
class LoginHandlerInterceptor(MiddlewareMixin):
    def process_request(self,request):
        if request.method == "OPTIONS":
            return None
        else:
            if request.path not in NOVERIFY_CHECK_PATH:
                # 校验非登录路径
                try:
                    # 校验token有效性
                    token = request.headers['Authorization']
                    status,userid = verify(token)
                    logger.debug("访问token=>{},访问用户=>{}".format(token,userid))
                    if request.path in SUPER_CHECK_PATH:
                        # 校验超级管理员权限
                        super_admin = Staff.objects.filter(id=userid,level=2).values()
                        logger.debug("访问超级管理员=>{}".format(super_admin))
                        if len(super_admin) == 0:
                            return HttpResponse(status=406, content="您没有权限访问该路径")
                except Exception:
                    return HttpResponse(status=401)
                if(status == 1): return None
                else: return HttpResponse(status=401)
            else: return None