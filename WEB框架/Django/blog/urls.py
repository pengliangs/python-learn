"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
# 返回一个模板
def tmpl_index(request):
    return render(request,"index.html",{"content":"hello","numbers":[1,2,5,6,3]})

def index(request):
    return HttpResponse("hello django.")

def json_return(request):
    return JsonResponse({"hello":"hello django."})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index),
    path('json/', json_return),
    path('tmpl/', tmpl_index),
    path('user/', include("user.urls")),
]
