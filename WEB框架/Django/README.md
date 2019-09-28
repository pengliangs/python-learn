[文档](https://docs.djangoproject.com/zh-hans/2.1/)
# 安装 Django

```
pip install django
```

# 查看django命令

```
django-admin
```

# 初始化一个 Django 项目

```
# blog是项目名称，后边的 "点" 代表当前目录，不然会创建一个嵌套目录
django-admin startproject blog .
```

# 目录结构
```lua
blog 项目名称
 ├── __init__.py
 ├── settings.py -- 全局配置信息
 ├── urls.py -- 做路由用的
 ├── wsgi.py -- wsgi接口信息
manage.py -- 项目命令行管理工具
```

# 数据库配置

```lua
DATABASES = {
    'default': {
         # 数据库引擎，需要安装 mysql 驱动支持，mysqlclient
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'test', # 数据库名称
        'USER': 'root', 
        'PASSWORD': 'root',  
        'HOST': '127.0.0.1', 
        'PORT': '3306',
    }
}
```

# 创建应用

```lua
$ python manage.py startapp user
```

# 注册应用

添加一个 user 应用。目的是为了后台管理 admin 使用，或迁移manage.py

```lua
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'user'
]
```

# 定义模型

https://docs.djangoproject.com/zh-hans/2.2/topics/db/models/#field-types

user/models.py

```python
from django.db import models

# Create your models here.
class UserBaseInfo(models.Model):
    # 使用内部 Meta类 来给模型赋予元数据，就像：
    class Meta:
        # 数据库表名
        db_table  = "user_base_info"
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100,null=False)
    age = models.IntegerField(null=False)
    
    def __repr__(self):
        return "".format(self.id,self.username,self.age)
        
    __str__ = __repr__

```

# 迁移Migration
从模型定义生成数据表

```lua
# 生成迁移文件，必须注册应用 INSTALLED_APPS
$ python manage.py makemigrations
# 执行迁移生成对应的表结构
$ python manage.py migrate
```


# 查看后台管理，创建管理用户

```lua
# createsuperuser
$ python manage.py
[auth]
    changepassword
    createsuperuser

$ python manage.py createsuperuser
```

# 设置语言和时区

```
LANGUAGE_CODE = 'zh-Hans'#'en-us'

TIME_ZONE = 'Asia/Shanghai'#'UTC'
```

# 启动服务

```
$ python manage.py runserver
```

# 启动成功

http://127.0.0.1:8000/admin


# 将自定义的UserBaseInfo注册到Django

admin.py
```
from django.contrib import admin
from .models import UserBaseInfo
# Register your models here.
admin.site.register(UserBaseInfo)
```

# 创建一个路由

urls.py
```python
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse,JsonResponse

def index(request):
    return HttpResponse("hello django.")

def json_return(request):
    return JsonResponse({"hello":"hello django."})
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index),
    path('json/', json_return),
]
```