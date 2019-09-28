import json
from django.core import serializers
from django.http import JsonResponse, HttpRequest, HttpResponseBadRequest
from  .models import UserBaseInfo
# Create your views here.

def register(request: HttpRequest):
    print(request)
    print(request.method)
    print(request.GET)
    print(request.POST)
    print(type(request))
    try:
        param = json.loads(request.body.decode())
        print("name=",param.get("name"))
        print("age=",param.get("age"))
        return JsonResponse({})
    except Exception as ex:
        print(ex)
        return HttpResponseBadRequest()

def add_fixed_user(request: HttpRequest):
    user_base_info = UserBaseInfo(username="张三",age="18")
    user_base_info.save()
    return JsonResponse({"data":"success"})

def list_user_base_info(request: HttpRequest):
    user_list = list(UserBaseInfo.objects.values())
    print(user_list)
    return JsonResponse({"data":user_list})