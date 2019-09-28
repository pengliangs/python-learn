from django.urls import path
from .views import register,list_user_base_info,add_fixed_user

urlpatterns = [
    path('register', register),
    path('list', list_user_base_info),
    path('add/fixed', add_fixed_user),
]
