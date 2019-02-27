# --*-- coding:utf-8 --*--
import re
import time
from requests.exceptions import RequestException
import requests
from lxml import etree
import datetime
from bs4 import BeautifulSoup

import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "untitled2.settings")# project_name 项目名称
django.setup()
from yuqing import models
list_key = ['常州']

def get_page(url):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}
    res = requests.get(url, headers=header)
    res.encoding = "uft-8"
    res_t = res.text
    soup = BeautifulSoup(res_t, "lxml")
    items = soup.select(".title")
    htmls = []
    titles = []
    cks = []
    hfs = []
    times = []
    for item in items:
        html = item.select("a")[0]['href'].strip()
        htmls.append(html)
        res = requests.get(html, headers=header)
        res.encoding = "gbk"
        res_t = res.text
        soup = BeautifulSoup(res_t, "lxml")
        if soup.select(".title_name h2 a"):
            title = soup.select(".title_name h2 a")[0].text.strip()
            # print(title)
            ck = int(soup.select(".data li span")[0].text)
            hf = int(soup.select(".data li span")[1].text)
            time = soup.select(".cont_hd p")[0]['title'].strip()
            time = datetime.datetime.strptime(time, '%Y-%m-%d %H:%M')
            titles.append(title)
            cks.append(ck)
            hfs.append(hf)
            times.append(time)
    return titles, cks, hfs, times, htmls


def load_data(titles, cks, hfs, times, htmls, key):
    for i in range(len(titles)):
        v1 = times[i]
        v2 = titles[i]
        v3 = hfs[i]
        v4 = cks[i]
        v5 = htmls[i]
        v6 ='化龙巷'
        v7 = key
        models.yqin1.objects.create(publish_time=v1,title=v2,hf=v3,ck=v4,url=v5,ly=v6,gjc=v7)

def main_hlx(key):
    url = "http://so.hualongxiang.com/?keyword="+key+"&page="+"1"+'&time=w&fid=103'
    titles, cks, hfs, times, htmls = get_page(url)
    load_data(titles, cks, hfs, times, htmls, key)
# #
# ##############################################
def get_pagecontent(url, key):
    header ={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
    s = requests.Session()
    r = s.get(url,headers=header)
    soup = BeautifulSoup(r.text,"lxml")
    formhash = soup.select('.searchform input')[0]['value']
    data = {'srchtxt': key, 'searchsubmit': 'yes', 'formhash': formhash}
    r = s.post(url,headers=header,data=data)
    try:
        if r.status_code == 200:
            return r.text
        else:
            return None
    except RequestException:
        print('请求索引页错误')
        return None

def get_txt(html,key):
    pat = re.compile('<h3.*?href=(.*? ).*?>(.*?)<.*?color.*?>(.*?)<.*?strong>(.*?)<.*?class.*?>(.*?)</p>.*?<span>(.*?)</span>', re.S)
    res = re.findall(pat, html)
    for item in res:
        readers=item[4].partition("-")
        now_time = time.time()-604800
        data = item[5]
        date = datetime.datetime.strptime(data,"%Y-%m-%d %H:%M")
        b = time.mktime(date.timetuple())
        if b>now_time:
            v1 = item[5]
            v2 = item[1]+item[2]+item[3]
            v3 = (readers[0]).replace("个回复", "")
            v4 = (readers[2]).replace("次查看", "")
            v5=eval(item[0].replace("&amp;", "&"))
            v6="中吴网"
            v7=key
            models.yqin1.objects.create(publish_time=v1,title=v2,hf=v3,ck=v4,url=v5,ly=v6,gjc=v7)
        else:
            break

def main_zww(key):  #关键词操作
    url ='http://www.zhong5.cn/search.php?mod=forum'
    html = get_pagecontent(url,key)
    get_txt(html,key)

"""复制数据"""
def copy_data():
    models.yqin1.objects.values('title').distinct()
    yq_list=models.yqin1.objects.all()
    models.yqout1.objects.all().delete()
    i=[]
    for list in yq_list:
        if list.title not in i:
            models.yqout1.objects.create(publish_time=list.publish_time, title=list.title, hf=list.hf, ck=list.ck, url=list.url, ly=list.ly, gjc=list.gjc)
        i.append(list.title)

"""程序主控制器"""
def pp(key):
    models.yqin1.objects.all().delete()
    main_hlx(key)
    main_zww(key)
    # main_weibo(key.title)
    copy_data()
    print(time.asctime( time.localtime(time.time()) ))

"""循环控件"""






    

