#!/usr/bin/python
# -*- coding:utf8 -*-

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse   # 2.0之前的reverse是core.urlresolvers现为urls
from django.contrib.auth.decorators import login_required

from .models import Theme, Topic, Entry
from .forms import ThemeForm, TopicForm, EntryForm

# Create your views here.


def index(request):
    """winter_web的主页"""
    return render(request, 'winter_web/index.html')


def text(request):
    return render(request, 'winter_web/test.html')


def lagou(request):
    """拉勾网数据仪表盘"""
    return render(request, 'winter_web/lagou.html')


def datas(request):
    """数据展示区"""
    return render(request,'winter_web/datas.html')


def themes(request):
    """定义winter_web的版块页面"""
    themes = Theme.objects.order_by('date_added')
    context = {'themes': themes}
    return render(request, 'winter_web/themes.html', context)


@login_required
def theme(request, theme_id):
    """定义theme-topic页面"""
    theme = Theme.objects.get(id=theme_id)
    topics = theme.topic_set.order_by('date_added')
    context = {'theme': theme, 'topics': topics}
    return render(request, 'winter_web/theme.html', context)


@login_required   # 登录用户方可调用该函数
def new_theme(request):   # 当不需要新建板块时,将html中到此的href删除
    if request.user.id == 1:
        if request.method != 'POST':
            form=ThemeForm()
        else:
            form=ThemeForm(request.POST)
            if form.is_valid():
                new_theme = form.save(commit=False)
                new_theme.owner = request.user   # 为theme指定一个owner
                new_theme.save()
                return HttpResponseRedirect(reverse('themes'))
        context={'form':form}
        return render(request,'winter_web/new_theme.html',context)
    else:
        return render(request,'winter_web/default.html')


@login_required
def topic(request, topic_id):
    """定义topic-entry页面"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'winter_web/topic.html', context)


@login_required  # 登录用户方可调用该函数
def new_topic(request, theme_id):
    theme = Theme.objects.get(id=theme_id)
    if request.method != 'POST':
        # 未提交数据:创建一个新表单
        form=TopicForm()
    else:
        # POST提交的数据,对数据进行处理
        form=TopicForm(data=request.POST)  # 用户输入数据会储存在request.POST中
        if form.is_valid():   # 检测有效性:表单是否已填写必要字段,数据是否合法
            new_topic = form.save(commit=False)   # 将表单数据写入数据库
            new_topic.owner = request.user
            new_topic.theme = theme
            new_topic.save()
            return HttpResponseRedirect(reverse('theme', args=[theme_id]))  # 提交完毕,去板块页面
    context = {'form': form, 'theme': theme}
    return render(request, 'winter_web/new_topic.html', context)


@login_required   # 登录用户方可调用该函数
def new_entry(request, topic_id):  # topic_id储存从url获得的值
    """在特定topic下添加新的entry"""
    topic = Topic.objects.get(id=topic_id)  # 获得entry所属的topic实例
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.owner = request.user
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('topic', args=[topic_id]))
    context = {'topic': topic, 'form': form}
    return render(request, 'winter_web/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):  # 获取entry.id的值,储存在entry_id中
    entry = Entry.objects.get(id=entry_id)  # 根据id获取entry的实例
    if request.user == entry.owner:
        topic = entry.topic           # 根据entry实例获取topic实例
        if request.method != 'POST':         # 初次请求
            form = EntryForm(instance=entry)  # 生成表单,自动填充entry实例
        else:
            form = EntryForm(instance=entry,data=request.POST)
            # 处理post数据,传输原entry和新提交的数据
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('topic', args=[topic.id]))
            # 通过验证储存表单后传递topic.id的值跳转到topic页面
        context = {'entry': entry, 'topic': topic, 'form': form}
        return render(request, 'winter_web/edit_entry.html', context)
    # 未传输数据继续停留在当前页面
    else:
        return render(request, 'winter_web/default.html')

