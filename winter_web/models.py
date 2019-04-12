#!/usr/bin/python
# -*- coding:utf8 -*-

from django.db import models
from django.contrib.auth.models import User  # 引入user模块绑定用户

# Create your models here.


class Theme(models.Model):      # 创建一个与topic类似的模型,作为版块
    """theme代表板块名称"""
    text = models.CharField(max_length=50)  # 版块名称限制长度50
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text


class Topic(models.Model):      # 先创建一个models.Model的子类Topic
    """topic代表板块名称"""
    text = models.CharField(max_length=200)  # 把CharField的实例作为类topic的属性text
    date_added = models.DateTimeField(auto_now_add=True)  # 又创建了一个类的实例作为属性
    owner = models.ForeignKey(User,on_delete=models.DO_NOTHING)  # 关联到用户
    theme = models.ForeignKey(Theme,on_delete=models.DO_NOTHING)  # 关联到板块

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text          # 所以其实返回的是实例topic的属性text,而属性text实际上是charfield的实例


class Entry(models.Model):
    """entry,版块下的条目"""
    topic = models.ForeignKey(Topic, on_delete=models.DO_NOTHING)  # 创建外键实例,关联一个topic作为外键
    text = models.TextField()        # 创建一个文本域实例
    date_added = models.DateTimeField(auto_now_add=True)  # 创建时间戳
    owner = models.ForeignKey(User,on_delete=models.DO_NOTHING)   # 关联到用户
    class Meta:
        verbose_name_plural = 'entries'  # 定义复数字符串

    def __str__(self):
        """返回模型的字符串表示"""
        if len(self.text) > 20:      # 默认只显示entry的前20个字符
            return self.text[:20]+'...'      # 拼接个省略号会好看点
        else:
            return self.text

