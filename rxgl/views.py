from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.decorators import login_required
import xlrd
from rxgl import models
from taxi import handle
from bus import bus_handle
import pandas as pd


@login_required
def czcsc(request):
    if request.method == "GET":
        return render(request, 'shangchuan/czcsc.html')
    else:
        title = request.POST.get("title")
        try:
            f = request.FILES['my_xzfile']
            type_excel = f.name.split('.')[1]
            if 'xls' == type_excel:
                # 开始解析上传的excel表格
                wb = xlrd.open_workbook(filename=None, file_contents=f.read())  # 关键点在于这里
                table = wb.sheets()[0]
                df = pd.DataFrame([list(table.row_values(i)) for i in range(1, table.nrows)])
                # print(type(df))
                df.columns = table.row_values(0)
                df.drop_duplicates('工单编号', inplace=True)
                # nrows = table.nrows  # 行数
                for i in range(len(df)):
                    rowValues = df.iloc[i,:]  # 一行的数据
                    models.czc.objects.create(gdbh=rowValues[0],
                                             slsj=rowValues[1],
                                             sllx=rowValues[2],
                                             slnr=rowValues[3],
                                             gdsx=rowValues[4],
                                             slr=rowValues[5],
                                             ly=rowValues[6],
                                             zbdw=rowValues[7],
                                             gdzt=rowValues[8],
                                             zjzt=rowValues[9],
                                             cbdw=rowValues[10],
                                             cbyj=rowValues[11],
                                             czlx=title,)
                    # print(title)
                    # models.czc.objects.create(czlx=title)
        except:
            return render(request,"nomal.html",{'msg':'出错请核查'})
        return render(request,"nomal.html",{'msg':'上传成功'})


@login_required
def gjcsc(request):
    if request.method == "GET":
        return render(request, 'shangchuan/gjcsc.html')
    else:
        try:
            f = request.FILES['my_xzfile']
            print(1)
            type_excel = f.name.split('.')[1]
            print(2)
            if 'xls' == type_excel:
                print(3)
                # 开始解析上传的excel表格
                wb = xlrd.open_workbook(filename=None, file_contents=f.read())  # 关键点在于这里
                table = wb.sheets()[0]
                df = pd.DataFrame([list(table.row_values(i)) for i in range(1, table.nrows)])
                df.columns = table.row_values(0)
                df.drop_duplicates('工单编号', inplace=True)
                # nrows = table.nrows  # 行数
                for i in range(len(df)):
                    rowValues = df.iloc[i,:]  # 一行的数据
                    print(rowValues[0])
                    models.gjc.objects.create(gdbh=rowValues[0],
                                             slsj=rowValues[1],
                                             sllx=rowValues[2],
                                             slnr=rowValues[3],
                                             gdsx=rowValues[4],
                                             slr=rowValues[5],
                                             ly=rowValues[6],
                                             zbdw=rowValues[7],
                                             gdzt=rowValues[8],
                                             zjzt=rowValues[9],
                                             cbdw=rowValues[10],
                                             cbyj=rowValues[11],
                                                     )
        except:
            return render(request, "nomal.html", {'msg': '出错请核查'})
        return render(request, "nomal.html", {'msg': '上传成功'})


@login_required
def index(request):
    return render(request,"shangchuan/dashboard.html")


@login_required
def czccl(request):
    if request.method =="GET":
        return render(request,'chuli/czccl.html')
    else:
        try:
            start = request.POST.get("start")
            end = request.POST.get("end")
            print(start,end)
            handle(start,end)
            print(1)
            # return render(request,"shangchuan/dashboard.html")
            return render(request,"nomal.html", {'msg': '处理成功'})
        except:
            return render(request,"nomal.html", {'msg': '出错请核查'})


@login_required
def gjccl(request):
    if request.method =="GET":
        return render(request,'chuli/gjccl.html')
    else:
        try:
            start = request.POST.get("start")
            end = request.POST.get("end")
            bus_handle(start,end)
            # return render(request,"shangchuan/dashboard.html")
            return render(request, "nomal.html", {'msg':  '处理成功'})
        except:
            return render(request, "nomal.html", {'msg': '出错请核查'})


