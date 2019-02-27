from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,login,logout



def acc_login(request):
    if request.method=="GET":
        return render(request,"log/login.html")
    else:
        error_msg = ''
        username = request.POST.get("username")
        password = request.POST.get("password")
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect(request.GET.get("next",'index'))
        else:
            error_msg = 'Wrong username or password'
            return render(request,"log/login.html",{'error_msg':error_msg})



def acc_logout(request):
    logout(request)
    return redirect("login")

