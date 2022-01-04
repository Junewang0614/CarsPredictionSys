import json

from django.http import HttpResponse
from django.shortcuts import render
from .models import User,Factory
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
        fname = request.POST['factory']

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
        password_m = m.hexdigest()

        # 1. 看看厂商在不在，不在要新建厂商
        fset = Factory.objects.filter(fname=fname)
        fid = 0
        if fset:
            fset = fset[0]
        else:
            fset = Factory(fname = fname)
            fset.save()
        User.objects.create(username = username,password=password_m,factory=fset)
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
        if not user.exists():
            messages.error(request, "用户名不存在")
            return render(request,'usermanage/logon.html',locals())

        m = hashlib.md5()  # 设置算法
        m.update(password.encode())  # 输入明文字节串
        password_m = m.hexdigest()

        # 验证失败
        if password_m != user[0].password:
            messages.error(request,"用户名或密码错误")
            return render(request, 'usermanage/logon.html',locals())
        else: # 成功登录，保存seesion
            request.session['user'] = {}
            request.session['user']['id'] = user[0].id
            request.session['user']['name'] = user[0].username

            # 保存factory
            fname = user[0].factory.fname
            flogo = user[0].factory.flogo

            request.session['factory'] = {}
            request.session['factory']['id'] = user[0].factory.id
            request.session['factory']['name'] = fname

            return render(request, 'usermanage/index.html', locals())

def success_rest_view(request):
    username = request.session['user']['name']
    names = ["王一丹","刘慧琳","夏志文","任思怡","罗晟"]
    return render(request,'usermanage/index2.html',locals())
