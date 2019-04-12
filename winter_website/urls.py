#!/usr/bin/python
# -*- coding:utf8 -*-

"""winter_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include

from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from winter_web.models import Theme, Topic

from django.views import static
from django.conf import settings
from django.conf.urls import url

# Serializers(串行器)定义api呈现
"""class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')  """


class TopicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Topic
        fields = ('date_added', 'id', 'text',)  # 调用api接口会展现这些内容,指定返回的数据集的字段


# ViewSets 定义视图行为
"""class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer"""


class TopicViewSet(viewsets.ModelViewSet):  # 指定返回的数据集
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


# router 提供了一个简单的方法去自动设置url配置
router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)
router.register('topic', TopicViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('winter_web.urls')),  # 添加winter_web的url
    path('users/', include('users.urls')),
    path('comments/', include('django_comments.urls')),
    # api接口
    path('api/', include(router.urls)),
    # debug=false 解决static显示错误的问题
    url('static/', static.serve, {'document_root': settings.STATIC_ROOT}, name='static'),

]
