from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def register(request):
    if request.method != 'POST':
        #form=RegisterForm()
        form=UserCreationForm()
    else:
        #form=RegisterForm(data=request.POST)
        form=UserCreationForm(data=request.POST) #储存注册信息并赋值变量form
        if form.is_valid():   #验证form信息有效
            new_user=form.save()   #注册用户并赋值给new_user
            LoginView.as_view(authentication_form=new_user,template_name='winter_web/index.html') #user传递给login登录
            return HttpResponseRedirect(reverse('index')) #返回主页
    context={'form':form}
    return render(request,'users/register.html',context)

