#!/usr/bin/python
# -*- coding:utf8 -*-

"""定义users的urls.py"""
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView  # 引入默认登录视图函数
from . import views


urlpatterns = [
    # 用户登录页面
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='winter_web/index.html'), name='logout'),
    path('register/', views.register, name='register'),

    ]
