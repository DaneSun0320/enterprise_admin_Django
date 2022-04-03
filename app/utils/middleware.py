
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin


USER_CHECK_PATH = [

]

ADMIN_CHECK_PATH = [

]

class OptionsCheckInterceptor(MiddlewareMixin):
    def process_request(self,request):
        if request.method == "OPTIONS":
            return None
        else:
            pass

class LoginHandlerInterceptor(MiddlewareMixin):
    def process_request(self,request):
        if request.method == "OPTIONS":
            return None
        else:
          pass