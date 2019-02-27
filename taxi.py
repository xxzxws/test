import pymysql
import re
import pandas as pd
import datetime


def handle(start,end):
    start_time=str(start)+' 00:00:00'
    end_time = str(end)+' 23:59:59'
    db= pymysql.connect(host="localhost",user="root",password="1234",db="rxgl",port=3306,charset="utf8")
    try:
        with db.cursor() as cursor:
            sql="select * from rxgl_czc where slsj between '{}' and '{}'".format(start_time,end_time)
            cursor.execute(sql)
            result=cursor.fetchall()
    finally:
        db.close();
    df_taxi = pd.DataFrame([list(i) for i in result])
    df_taxi2 = pd.DataFrame(df_taxi.iloc[:,4])
    df_taxi2.columns=['受理内容']
    df_taxi2['工单编号'] =df_taxi.iloc[:,1]
    df_taxi2['出租车类型'] = df_taxi.iloc[:, 13]
    df_taxi2['投诉日期'] = df_taxi.iloc[:, 2]
    df_taxi2['投诉日期'] = pd.to_datetime(df_taxi2['投诉日期'], format='%Y%m%d')
    df_taxi2['投诉日期'] = df_taxi2['投诉日期'].dt.strftime('%Y-%m-%d')
    df_taxi2['所属公司']='无'
    df_taxi2['车牌号']='无'
    df_taxi2['事发日期']='无'
    df_taxi2['上车时间']='无'
    df_taxi2['下车时间']='无'
    df_taxi2['上车地点']='无'
    df_taxi2['下车地点']='无'
    df_taxi2['诉求类别']='其他'
    df_taxi2 = df_taxi2.loc[:,['工单编号','投诉日期','所属公司', '车牌号','事发日期', '上车时间', '上车地点','下车时间','下车地点','诉求类别','受理内容','出租车类型']]
    company_list = ['巴士出租', '外汽出租', '交服出租', '东方出租', '武进顺发', '联创出租','常运出租', '吉达出租', '苏南交运','新联龙城', '捷达出租', '捷安出租', '凯凯商务','八达旅游', '华泰出租', '武进汽运', '东吴出租', '众联出租', '新能源车' ]
    ###所属公司
    i=0
    for content in df_taxi2['受理内容']:
        company_names = set()
        for company_name in company_list:
            if company_name in content:
                company_names.add(company_name)
        if len(company_names)>0:
            company_names = ' '.join(company_names)
            df_taxi2.loc[i,'所属公司'] = company_names.strip()
        i+=1

    ###车牌号
    i=0
    for content in df_taxi2['受理内容']:
        taxi_num = re.findall("(苏D[A-Z]*\d+[A-Z]*)",content)
        if len(taxi_num)>0:
            taxi_num = list(set(taxi_num))
            taxi_num = ' '.join(taxi_num)
            df_taxi2.loc[i,'车牌号'] = taxi_num.strip()
        i+=1

    ###事发日期
    i=0
    for content,gd_date in zip(df_taxi2['受理内容'],df_taxi2['投诉日期']):
        date = re.search(r"(\d{1,2}月\d{1,2}日)",content)
        if date is not None:
            month= re.findall("(\d{1,2})月",date.group(0))
            if '%02d'%int(month[0])!=gd_date[5:7] and '%02d'%int(month[0])=='12' :
                df_taxi2.loc[i,'事发日期'] = datetime.datetime.strptime(str(int(gd_date[0:4])-1)+'年'+date.group(0), '%Y年%m月%d日').strftime('%Y-%m-%d')
            else:
                df_taxi2.loc[i,'事发日期'] = datetime.datetime.strptime(gd_date[0:4]+'年'+date.group(0), '%Y年%m月%d日').strftime('%Y-%m-%d')
        i+=1

    ###上下车时间
    i=0
    for content, sf_date in zip(df_taxi2['受理内容'],df_taxi2['事发日期']):
        time = re.findall(r"(\d{1,2}时\d{1,2}分).*?上车，",content)
        if len(time)==0:
            time = re.findall(r"(\d{1,2}时\d{1,2}分).*?叫车，",content)
        if len(time)==0:
            time = re.findall(r"(\d{1,2}时\d{1,2}分).*?打车，",content)
        if len(time)==0:
            time = re.findall(r"(\d{1,2}时\d{1,2}分).*?等车，",content)
        if len(time)>0  and (sf_date!='无'):
            try:
                df_taxi2.loc[i,'上车时间'] = datetime.datetime.strptime(sf_date+' '+time[0], '%Y-%m-%d %H时%M分').strftime('%H:%M').replace(':','时')+'分'
            except:
                pass
        time2 = re.findall(r"上车，(\d{1,2}时\d{1,2}分).*?下车",content)
        if len(time2)==0:
            time2 = re.findall(r"上车，.*?(\d{1,2}时\d{1,2}分).*?下车",content)
        if len(time2)>0 and (sf_date!='无'):
            try:
                df_taxi2.loc[i,'下车时间'] = datetime.datetime.strptime(sf_date+' '+time2[0], '%Y-%m-%d %H时%M分').strftime('%H:%M').replace(':','时')+'分'
            except:
                pass
        i+=1
    sqlx_list =['拒载','不使用计价器','不提供票据','异地经营','公司经营纠纷','不文明驾驶','乱收费','多收费','甩客','爽约','擅自拼车','绕路','服务质量','服务差','拒载']
    i=0
    for content in df_taxi2['受理内容']:
        for sqlx in sqlx_list:
            if sqlx in content:
                df_taxi2.loc[i,'诉求类别'] = sqlx
            if '绕远路' in content:
                df_taxi2.loc[i, '诉求类别'] = "绕路"
            if '乱收费'in content:
                df_taxi2.loc[i,'诉求类别'] = "多收费"
            if df_taxi2.loc[i,'诉求类别']=='其他' and '拼车'in content:
                df_taxi2.loc[i,'诉求类别'] = "擅自拼车"
            if df_taxi2.loc[i,'诉求类别']=='其他' and '态度'in content or '服务差' in content:
                df_taxi2.loc[i,'诉求类别'] = "服务质量"
            if df_taxi2.loc[i, '诉求类别'] == '其他' and '计价器' in content:
                df_taxi2.loc[i, '诉求类别'] = "计价器问题"
        i+=1


    i=0
    for content in df_taxi2['受理内容']:
        seton_add = re.findall("在(.*?)想要上车",content)
        if len(seton_add) == 0:
            seton_add = re.findall("在(.*?)准备上车",content)
        if len(seton_add) == 0:
            seton_add = re.findall("在(.*?)排队等车",content)
        if len(seton_add) == 0:
            seton_add = re.findall("在(.*?)招车",content)
        if len(seton_add) == 0:
            seton_add = re.findall("在(.*?)等车",content)
        if len(seton_add) == 0:
            seton_add = re.findall("在(.*?)上车",content)
        if len(seton_add) == 0:
            seton_add = re.findall("在(.*?)打车",content)
        if len(seton_add) == 0:
            seton_add = re.findall("在(.*?)叫车",content)
        if len(seton_add) > 0:
            if '恐龙园' in seton_add[0]:
                df_taxi2.loc[i,'上车地点'] = '恐龙园迪诺水镇'
            elif '奔牛机场'in seton_add[0]:
                df_taxi2.loc[i,'上车地点'] = '常州机场'
            elif '火车站北广场'in seton_add[0] or '常州北广场'in seton_add[0] or seton_add[0]=='北广场':
                df_taxi2.loc[i,'上车地点'] = '常州站北广场'
            elif '火车站南广场'in seton_add[0] or '常州南广场'in seton_add[0] or seton_add[0]=='南广场':
                df_taxi2.loc[i,'上车地点'] = '常州站南广场'
            else:
                df_taxi2.loc[i,'上车地点'] = seton_add[0]

        setoff_add = re.findall("在.*?上车，在(.*?)下车",content)
        if len(setoff_add) > 0 and (('，'in setoff_add[0] or '。' in setoff_add[0]) or len(setoff_add[0])>12):
            setoff_add = re.findall("目的地(.*?)，",content)
        if len(setoff_add) > 0 and (('，'in setoff_add[0] or '。' in setoff_add[0]) or len(setoff_add[0])>12):
            setoff_add =re.findall("目的地(.*?)。",content)
        if len(setoff_add) == 0:
            setoff_add = re.findall("在.*?上车，.*?在(.*?)下车",content)
        if len(setoff_add) > 0 and (('，'in setoff_add[0] or '。' in setoff_add[0]) or len(setoff_add[0])>12):
            setoff_add = re.findall("目的地(.*?)，",content)
        if len(setoff_add) > 0 and (('，'in setoff_add[0] or '。' in setoff_add[0]) or len(setoff_add[0])>12):
            setoff_add =re.findall("目的地(.*?)。",content)
        if len(setoff_add) == 0:
            setoff_add = re.findall("目的地(.*?)，",content)
        if len(setoff_add) > 0 and (('，'in setoff_add[0] or '。' in setoff_add[0]) or len(setoff_add[0])>12):
            setoff_add = re.findall("目的地(.*?)。",content)
        if len(setoff_add) == 0:
            setoff_add = re.findall("目的地(.*?)。",content)
        if len(setoff_add) > 0:
            if '恐龙园' in setoff_add[0]:
                df_taxi2.loc[i,'下车地点'] = '恐龙园迪诺水镇'
            elif '奔牛机场'in setoff_add[0]:
                df_taxi2.loc[i,'下车地点'] = '常州机场'
            elif '火车站北广场'in setoff_add[0] or '常州北广场'in setoff_add[0] or setoff_add[0]=='北广场':
                df_taxi2.loc[i,'上车地点'] = '常州站北广场'
            elif '火车站南广场'in setoff_add[0] or '常州南广场'in setoff_add[0] or setoff_add[0]=='南广场':
                df_taxi2.loc[i,'上车地点'] = '常州站南广场'
            else:
                df_taxi2.loc[i,'下车地点'] = setoff_add[0]
        i+=1


    db= pymysql.connect(host="localhost",user="root",password="1234",db="rxgl",port=3306,charset="utf8")
    with db:
        cur=db.cursor()
        sql = "INSERT INTO rxgl_taxi(gdbh,tsrq,company,taxi_number,sfrq,geton_time,geton_address,getoff_time,getoff_address,sqlb,slnr,czlx) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        for i in range(len(df_taxi2)):
            v1 = df_taxi2.loc[i,'工单编号']
            v2 = df_taxi2.loc[i,'投诉日期']
            v3 = df_taxi2.loc[i,'所属公司']
            v4 = df_taxi2.loc[i,'车牌号']
            v5 = df_taxi2.loc[i,'事发日期']
            v6 = df_taxi2.loc[i,'上车时间']
            v7 = df_taxi2.loc[i,'上车地点']
            v8 = df_taxi2.loc[i,'下车时间']
            v9 = df_taxi2.loc[i,'下车地点']
            v10 = df_taxi2.loc[i,'诉求类别']
            v11 = df_taxi2.loc[i,'受理内容']
            v12 = df_taxi2.loc[i, '出租车类型']
            cur.execute(sql,(v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12))
    db.close()


