#!/usr/bin/python
# -*- coding:utf8 -*-

"""定义winter_web的url模式"""
from django.urls import path  
from . import views         # 从当前目录导入模块views(视图)


urlpatterns = [
    # 主页
    path(r'', views.index, name='index'),  # 给url模式取名为index
    # 数据展示区
    path('datas/', views.datas, name='datas'),
    # themes页面
    path('themes/', views.themes, name='themes'),
    # theme页面
    path('themes/<theme_id>/', views.theme, name='theme'),
    # 创建新theme
    path('new_theme/', views.new_theme, name='new_theme'),
    # topic下的entry页面,topic_id为从上一层链接topics.html获得的值
    path('topics/<topic_id>/', views.topic, name='topic'),
    # 创建新topic的页面
    path('new_topic/<theme_id>/', views.new_topic, name='new_topic'),
    # 创建新entry的页面,topic_id为从上一层链接topic.html获得的值
    path('new_entry/<topic_id>/', views.new_entry, name='new_entry'),
    # 创建编辑entry的页面,需要获取entry.id
    path('edit_entry/<entry_id>/', views.edit_entry, name='edit_entry'),
    # btc数据仪表盘
    path('datas/lagou/', views.lagou, name='lagou'),
    # test页面
    path('test/', views.text, name='test')
]
