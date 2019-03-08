# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 15:51:33 2019

@author: Administrator
"""

import re
import pandas as pd
import datetime
import pymysql


def bus_handle(start,end):
    start_time=start+' 00:00:00'
    end_time = end+' 23:59:59'
    db= pymysql.connect(host="localhost",user="root",password="1234",db="perferctcrm",port=3306,charset="utf8")
    try:
        with db.cursor() as cursor:
            sql="SELECT * FROM rxgl_gjc where slsj between '{}' and '{}'".format(start_time,end_time)
            cursor.execute(sql)
            result=cursor.fetchall()
    finally:
        db.close()
    df_bus = pd.DataFrame([list(i) for i in result])
    df_bus2 = pd.DataFrame(df_bus.iloc[:,4])
    df_bus2.columns=['受理内容']
    df_bus2['工单编号'] =df_bus.iloc[:,1]
    df_bus2['投诉日期']= df_bus.iloc[:,2]
    df_bus2['投诉日期']=pd.to_datetime(df_bus2['投诉日期'], format='%Y%m%d')
    df_bus2['投诉日期']=df_bus2['投诉日期'].dt.strftime('%Y-%m-%d')
    df_bus2['路别']='无'
    df_bus2['车牌号']='无'
    df_bus2['自编号']='无'
    df_bus2['诉求类别']='其他'
    df_bus2['事发日期']='无'
    df_bus2['等车时间']='无'
    df_bus2['上车时间']='无'
    df_bus2['下车时间']='无'
    df_bus2['上车地点']='无'
    df_bus2['下车地点']='无'

    df_bus2 = df_bus2.loc[:,['工单编号','投诉日期','路别','车牌号', '自编号','事发日期','等车时间','上车时间','上车地点','下车时间', '下车地点','诉求类别', '受理内容']]
    i=0
    for content in df_bus2['受理内容']:
        bus_line = re.findall(r"([A-Za-z]*\d+[A-Za-z]*路)",content)
        bus_num = re.findall("自编号为(\d+)",content)
        bus_cph = re.findall("(苏D[A-Za-z]*\d+[A-Za-z]*)",content)
        if len(bus_num)==0:
             bus_num = re.findall("自编号(\d+)",content)
        if len(bus_num)>0:
            df_bus2.loc[i,'自编号'] = bus_num[0]
        if len(bus_line)>0:
            df_bus2.loc[i,'路别'] = bus_line[0]
        if len(bus_cph)>0:
            df_bus2.loc[i,'车牌号'] = bus_cph[0]
        i+=1

    ###诉求类别
    buslx_list =['站点设置不合理','线路规划/调整','未按站点停靠/到站不停靠/二次停站','车辆车况','运行时间问题（晚点)',
                 '服务质量','消极驾驶','一卡通问题','不安全（文明）行车','不照顾赶来的乘客','公交站台、设施问题',
                 '事故纠纷','不文明行为','不开空调','拒载', '开车车速慢']
    i=0
    for content in df_bus2['受理内容']:
        for buslx in buslx_list:
            if buslx in content:
                df_bus2.loc[i,'诉求类别'] = buslx
            if df_bus2.loc[i,'诉求类别']=='其他' and '不按线路行驶'in content:
                df_bus2.loc[i,'诉求类别'] = "线路规划/调整"
            if df_bus2.loc[i,'诉求类别']=='其他' and '设备'in content or '路别问题'in content or '语音播报'in content or '刷卡机'in content:
                df_bus2.loc[i,'诉求类别'] = "车辆车况"
            if df_bus2.loc[i,'诉求类别']=='其他' and '不安全行车'in content or '不文明行车'in content or\
            '不文明驾驶'in content or '不安全驾驶'in content or '危险驾驶'in content or '野蛮驾驶'in content or '不文明行驶'in content:
                df_bus2.loc[i,'诉求类别'] = "不安全（文明）行车"
            if df_bus2.loc[i,'诉求类别']=='其他' and '赶来的乘客'in content or '赶车乘客'in content  or '赶来乘客'in content  or '赶车的乘客'in content:
                df_bus2.loc[i,'诉求类别'] = "不照顾赶来的乘客"
            if df_bus2.loc[i,'诉求类别']=='其他' and '事故' in content or '受伤' in content:
                df_bus2.loc[i,'诉求类别'] = "事故纠纷"
            if df_bus2.loc[i,'诉求类别']=='其他' and '停车'in content or '停靠'in content or '不停'in content or '未停'in content:
                df_bus2.loc[i,'诉求类别'] = "未按站点停靠/到站不停靠/二次停站"
            if df_bus2.loc[i,'诉求类别']=='其他' and '晚点' in content or '时间' in content:
                df_bus2.loc[i,'诉求类别'] = "运行时间问题（晚点)"
            if df_bus2.loc[i,'诉求类别']=='其他' and '服务差' in content or '态度' in content:
                df_bus2.loc[i,'诉求类别'] = "服务质量"
            if df_bus2.loc[i,'诉求类别']=='其他' and '空调' in content or '暖气' in content:
                df_bus2.loc[i,'诉求类别'] = "不开空调"
        i+=1

    ###事发日期
    i=0
    for content,gd_date in zip(df_bus2['受理内容'],df_bus2['投诉日期']):
        date = re.search(r"(\d{1,2}月\d{1,2}日)",content)
        if date is not None:
            month= re.findall("(\d{1,2})月",date.group(0))
            if '%02d'%int(month[0])!=gd_date[5:7] and '%02d'%int(month[0])=='12' :
                df_bus2.loc[i,'事发日期'] = datetime.datetime.strptime(str(int(gd_date[0:4])-1)+'年'+date.group(0), '%Y年%m月%d日').strftime('%Y-%m-%d')
            else:
                df_bus2.loc[i,'事发日期'] = datetime.datetime.strptime(gd_date[0:4]+'年'+date.group(0), '%Y年%m月%d日').strftime('%Y-%m-%d')
        i+=1

    ###上下车时间
    i=-1
    for content, sf_date in zip(df_bus2['受理内容'],df_bus2['事发日期']):
        i+=1
        time = re.findall("(\d{1,2}时\d{1,2}分).*?等车",content)
        if len(time)>0:
             try:
                 df_bus2.loc[i,'等车时间'] = datetime.datetime.strptime(sf_date+' '+time[0], '%Y-%m-%d %H时%M分').strftime('%H:%M')
             except:
                pass
             try:
                 df_bus2.loc[i,'等车时间'] = datetime.datetime.strptime(sf_date+' '+time[0], '%Y-%m-%d %H时').strftime('%H:%M')
             except:
                 pass
        if df_bus2.loc[i,'等车时间']!='无':
            time = re.findall("到.*?(\d{1,2}时\d{1,2}分)",content)
            if len(time)>0:
                try:
                    df_bus2.loc[i,'上车时间'] = datetime.datetime.strptime(sf_date+' '+time[0], '%Y-%m-%d %H时%M分').strftime('%H:%M')
                except:
                    pass

        time = re.findall("等车，.*?未.*?上车",content)
        if len(time)>0:
            continue
        time = re.findall("等车，.*?没.*?上车",content)
        if len(time)>0:
            continue
        time = re.findall("等车，.*?不.*?上车",content)
        if len(time)>0:
            continue
        time = re.findall("(\d{1,2}时\d{1,2}分).*?上车",content)
        if len(time)==0:
            time = re.findall("(\d{1,2}时\d{1,2}分).*?乘车",content)
        if len(time)==0:
            time = re.findall("(\d{1,2}时\d{1,2}分).*?乘坐",content)
        if len(time)>0:
            try:
                df_bus2.loc[i,'上车时间'] = datetime.datetime.strptime(sf_date+' '+time[0], '%Y-%m-%d %H时%M分').strftime('%H:%M')
            except:
                pass

        time = re.findall(r"上车，(\d{1,2}时\d{1,2}分).*?下车",content)
        if len(time)==0:
            time = re.findall("上车，.*?(\d{1,2}时\d{1,2}分).*?下车",content)
        if len(time)==0:
            para = re.findall(r"(\d{1,2}时\d{1,2}分.*?下车)",content)
            if len(para)>0 and ('，'not in para[0] and '。' not in para[0]):
                time = re.findall(r"(\d{1,2}时\d{1,2}分).*?下车",content)
        if len(time)>0:
            try:
                df_bus2.loc[i,'下车时间'] = datetime.datetime.strptime(sf_date+' '+time[0], '%Y-%m-%d %H时%M分').strftime('%H:%M')
            except:
                pass


    i=0
    for content in df_bus2['受理内容']:
        seton_add = re.findall("在(.*?站点)等车",content)
        if len(seton_add) == 0:
            seton_add = re.findall("在(.*?站点)上车",content)
        if len(seton_add) == 0:
            seton_add = re.findall("在(.*?站点)想要上车",content)
        if len(seton_add) == 0:
            seton_add = re.findall("在(.*?站点)",content)
        if len(seton_add) > 0:
            df_bus2.loc[i,'上车地点'] = seton_add[0]
        setoff_add = re.findall("在.*?上车，在(.*?站点)下车",content)
        if len(setoff_add) == 0:
            setoff_add = re.findall("在.*?上车，.*?在(.*?站点)下车",content)
        if len(setoff_add) == 0:
            setoff_add = re.findall("，在(.*?站点)下车",content)
        if len(setoff_add) == 0:
            setoff_add = re.findall("，.*?在(.*?站点)下车",content)
        if len(setoff_add) == 0:
            setoff_add = re.findall("在(.*?站点)下车",content)
        if len(setoff_add) == 0:
            setoff_add = re.findall("，在(.*?站点).*?下车",content)
        if len(setoff_add) > 0:
            df_bus2.loc[i,'下车地点'] = setoff_add[0]
        i+=1

    db= pymysql.connect(host="localhost",user="root",password="1234",db="perferctcrm",port=3306,charset="utf8")
    with db:
        cur=db.cursor()
        sql = "INSERT INTO rxgl_bus(gdbh,tsrq,lb,bus_number,bus_zbh,sfrq,wait_time,geton_time,geton_address,getoff_time,getoff_address,sqlb,slnr) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        for i in range(len(df_bus2)):
            v1 = df_bus2.loc[i,'工单编号']
            v2 = df_bus2.loc[i,'投诉日期']
            v3 = df_bus2.loc[i,'路别']
            v4 = df_bus2.loc[i,'车牌号']
            v5 = df_bus2.loc[i,'自编号']
            v6 = df_bus2.loc[i,'事发日期']
            v7 = df_bus2.loc[i,'等车时间']
            v8 = df_bus2.loc[i,'上车时间']
            v9 = df_bus2.loc[i,'上车地点']
            v10 = df_bus2.loc[i,'下车时间']
            v11 = df_bus2.loc[i,'下车地点']
            v12 = df_bus2.loc[i,'诉求类别']
            v13 = df_bus2.loc[i,'受理内容']
            cur.execute(sql,(v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13))
    db.close()