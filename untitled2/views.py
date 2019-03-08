from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,login,logout


from django.shortcuts import render, redirect
from rbac import models
from rbac.service.init_permission import init_permission


def acc_login(request):
    if request.method == 'GET':
        return render(request, 'log/login.html')
    user = request.POST.get('username')
    pwd = request.POST.get('password')
    user_object = models.UserInfo.objects.filter(name=user, password=pwd).first()
    if not user_object:
        return render(request, 'log/login.html', {'error': '用户名或密码错误'})
    init_permission(user_object, request)
    return redirect('/index/')

# def acc_login(request):
#     if request.method=="GET":
#         return render(request,"log/login.html")
#     else:
#         error_msg = ''
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#         user=authenticate(username=username,password=password)
#         if user:
#             login(request,user)
#             return redirect(request.GET.get("next",'index'))
#         else:
#             error_msg = 'Wrong username or password'
#             return render(request,"log/login.html",{'error_msg':error_msg})



def acc_logout(request):
    logout(request)
    return redirect("login")

def acc_index(request):
    return render(request, 'layout.html')