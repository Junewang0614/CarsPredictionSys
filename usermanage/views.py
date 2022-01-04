from django.http import HttpResponse
from django.shortcuts import render
from .models import User
import hashlib
from django.contrib import messages
# Create your views here.

def register_view(request):

    if request.method == "GET":
        return render(request,'usermanage/register.html')
    elif request.method == 'POST':
        # 1.两个密码比对
        # 2.用户名是否可用
        # 3.明文处理密码
        # 4.插入新用户

        username = request.POST['uname']
        password = request.POST['pward']
        vpass = request.POST['vpward']

        if password != vpass:
            messages.error(request, '两次密码输入不一致')
            return render(request,'usermanage/register.html',locals())
        if User.objects.filter(username = username):
            messages.error(request,'用户名已注册')
            return render(request,'usermanage/register.html',locals())

        # Hash算法
        # 特点：
        # 1. 定长输出
        # 2. 不可逆
        # 3. 雪崩效应：输入改变，输出必变
        m = hashlib.md5()# 设置算法
        m.update(password.encode())# 输入明文字节串
        passward_m = m.hexdigest()

        User.objects.create(username = username,passward=passward_m)
        # 成功返回登录界面
        messages.success(request,"注册信息提交成功，在1-3个工作日内会返回审核结果")
        return render(request, 'usermanage/logon.html', locals())

def logon_view(request):
    if request.method == 'GET':
        return render(request,'usermanage/logon.html')
    if request.method == 'POST':
        username = request.POST['uname']
        password = request.POST['pword']

        user = User.objects.filter(username=username,is_active=True)
        # 先看用户在不在
        print(len(user))

        if not user.exists():

            return HttpResponse('用户不存在')

        m = hashlib.md5()  # 设置算法
        m.update(password.encode())  # 输入明文字节串
        passward_m = m.hexdigest()

        # 验证失败
        if passward_m != user[0].passward:
            return HttpResponse('密码错误！')
        else:
            return render(request, 'usermanage/index.html', locals())
