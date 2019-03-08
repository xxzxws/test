from django.shortcuts import render,redirect
# from yuqing import models
# import pymysql
import spy1
# from django.contrib.auth.decorators import login_required

import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "untitled2.settings")# project_name 项目名称
django.setup()
from yuqing import models


def yu_list(request):
    # db = pymysql.connect(host="localhost", user="root", password="1234", db="rxgl", port=3306, charset="utf8")
    # cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
    # cursor.execute("select id,publish_time,title,hf,ck,url,ly,gjc from yuqing_yqout")
    # new_list = cursor.fetchall()
    new_list = models.yqout.objects.all()
    # cursor.execute("select gjc from yuqing_yqgjc")
    # gjc_list = []
    # list = cursor.fetchall()
    # for i in list:
    #     gjc_list.append(i["gjc"])
    # cursor.close()
    # db.close()
    return render(request,"yuqing/yu_list.html", { 'new_list':new_list })


def gjc_list(request):
    if request.method=="GET":
        return render(request, 'yuqing/gjc_search.html')
    else:
        key = request.POST.get("key")
        print(key)
        if key:
            spy1.pp(key)
            # db = pymysql.connect(host="localhost", user="root", password="1234", db="rxgl", port=3306, charset="utf8")
            # cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
            # cursor.execute("select id,publish_time,title,hf,ck,url,ly,gjc from yuqing_yqout1")
            # new_list = cursor.fetchall()
            new_list =models.yqout1.objects.all()
            # cursor.close()
            # db.close()
            return render(request,"yuqing/gjc_list.html", {'new_list':new_list})



def gjc(request):
    if request.method == "GET":
        # db = pymysql.connect(host="10.9.96.217", user="root", password="1234", db="zh", port=3306, charset="utf8")
        # cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
        # cursor.execute("select id,gjc from yq_gjc")
        gjc_list = models.gjc.objects.all()
        return render(request,"yuqing/gjc_gl.html", {'new_list':gjc_list})
    else:
        key2 = request.GET.get("key2")
        if key2:
            models.gjc.objects.create(title=key2)
            # db = pymysql.connect(host="10.9.96.217", user="root", password="1234", db="zh", port=3306,
            #                      charset="utf8")
            # cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
            # sql = "INSERT INTO yq_gjc(gjc) VALUES(%s)"
            # cursor.execute(sql, (key2))
            # db.commit()
            # cursor.execute("select id,gjc from yq_gjc")
            # db.commit()
            # new_list = cursor.fetchall()
            # cursor.close()
            # db.close()
            return redirect("/yuqing/gjc/")
            # return render(request,"yuqing/gjc_gl.html", {'new_list':new_list})
        else:
            return redirect("/yuqing/gjc/")


def sc(request):
    nid =request.GET.get("nid")
    models.gjc.objects.filter(id = nid).delete()
    return redirect('/yuqing/gjc/')

def zj(request):
    gjc = request.POST.get("key2")
    models.gjc.objects.create(title = gjc)
    return redirect('/yuqing/gjc/')