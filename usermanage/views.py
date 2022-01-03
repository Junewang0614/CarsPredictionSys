from django.http import HttpResponse
from django.shortcuts import render
from .models import User
import hashlib
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
        passward = request.POST['pward']
        vpass = request.POST['vpward']

        if passward != vpass:
            return HttpResponse('两次密码输入不相同')
        if User.objects.filter(username = username):
            return HttpResponse('用户名已注册')

        # Hash算法
        # 特点：
        # 1. 定长输出
        # 2. 不可逆
        # 3. 雪崩效应：输入改变，输出必变
        m = hashlib.md5()# 设置算法
        m.update(passward.encode())# 输入明文字节串
        passward_m = m.hexdigest()

        User.objects.create(username = username,passward=passward_m)
        return render(request,'usermanage/success.html',locals())
