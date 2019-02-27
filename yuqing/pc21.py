# --*-- coding:utf-8 --*--
import re
import pymysql
import time
from requests.exceptions import RequestException
import requests
from lxml import etree
import datetime
# from datetime import datetime
from bs4 import BeautifulSoup

import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "untitled2.settings")# project_name 项目名称
django.setup()
from yuqing import models
# list_key = ['常州']
# n ="1"
# def get_page(url):
#     header = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}
#     res = requests.get(url, headers=header)
#     res.encoding = "uft-8"
#     res_t = res.text
#     soup = BeautifulSoup(res_t, "lxml")
#     items = soup.select(".title")
#     htmls = []
#     titles = []
#     cks = []
#     hfs = []
#     times = []
#     for item in items:
#         html = item.select("a")[0]['href'].strip()
#         htmls.append(html)
#         title, ck, hf, time = get_other(html)
#         titles.append(title)
#         cks.append(ck)
#         hfs.append(hf)
#         times.append(time)
#     return titles, cks, hfs, times, htmls
#
# def get_other(url):
#     header = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}
#     res = requests.get(url, headers=header)
#     res.encoding = "gbk"
#     res_t = res.text
#     soup = BeautifulSoup(res_t, "lxml")
#     title = soup.select(".title_name h2 a")[0].text.strip()
#     ck = int(soup.select(".data li span")[0].text)
#     hf = int(soup.select(".data li span")[1].text)
#     time = soup.select(".cont_hd p")[0]['title'].strip()
#     time = datetime.datetime.strptime(time, '%Y-%m-%d %H:%M')
#     return title, ck, hf, time
#
#
# def load_data(titles, cks, hfs, times, htmls, key):
#     db= pymysql.connect(host="localhost",user="root",password="1234",db="rxgl",port=3306,charset="utf8")
#     #db= pymysql.connect(host="localhost",user="root",password="187490",db="2.1",port=3306)
#     # 使用cursor()方法获取操作游标
#     # SQL 插入语句
#     for i in range(len(titles)):
#         cur=db.cursor()
#         sql = "INSERT INTO yuqing_yqin(publish_time,title,hf,ck,url,ly,gjc) VALUES(%s,%s,%s,%s,%s,%s,%s)"
#         v1 = times[i]
#         v2 = titles[i]
#         v3 = hfs[i]
#         v4 = cks[i]
#         v5 = htmls[i]
#         v6 ='化龙巷'
#         v7 = key
#         cur.execute(sql,(v1,v2,v3,v4,v5,v6,v7))
#     db.commit()
#     db.close()
#
# def main_hlx(key):
#     url = "http://so.hualongxiang.com/?keyword="+key+"&page="+str(n)+'&time=w'
#     titles, cks, hfs, times, htmls = get_page(url)
#     load_data(titles, cks, hfs, times, htmls, key)
#
# ##############################################
# def get_pagecontent(url, key):
#     header ={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
#     s = requests.Session()
#     r = s.get(url,headers=header)
#     soup = BeautifulSoup(r.text,"lxml")
#     formhash = soup.select('.searchform input')[0]['value']
#     data = {'srchtxt': key, 'searchsubmit': 'yes', 'formhash': formhash}
#     r = s.post(url,headers=header,data=data)
#     try:
#         if r.status_code == 200:
#             return r.text
#
#         else:
#             return None
#     except RequestException:
#         print('请求索引页错误')
#         return None
#
# def get_txt(html,key):
#     pat = re.compile('<h3.*?href=(.*? ).*?>(.*?)<.*?color.*?>(.*?)<.*?strong>(.*?)<.*?class.*?>(.*?)</p>.*?<span>(.*?)</span>', re.S)
#     res = re.findall(pat, html)
#     for item in res:
#         readers=item[4].partition("-")
#         now_time = time.time()-604800
#         data = item[5]
#         date = datetime.datetime.strptime(data,"%Y-%m-%d %H:%M")
#         b = time.mktime(date.timetuple())
#         if b>now_time:
#             v1 = item[5]
#             v2 = item[1]+item[2]+item[3]
#             v3 = (readers[0]).replace("个回复", "")
#             v4 = (readers[2]).replace("次查看", "")
#             v5=eval(item[0].replace("&amp;", "&"))
#             v6="中吴网"
#             v7=key
#             db = pymysql.connect("localhost", "root", "1234", "rxgl", charset="utf8mb4")
#             cursor = db.cursor()
#             sql = "INSERT INTO yuqing_yqin(publish_time,title, hf,ck, url,ly,gjc)VALUES (%s,%s,%s,%s,%s,%s,%s)"
#             cursor.execute(sql, (v1, v2, v3, v4, v5, v6, v7))
#             db.commit()
#             cursor.close()
#             db.close()
#         else:
#             break
#
# def main_zww(key):  #关键词操作
#     url ='http://www.zhong5.cn/search.php?mod=forum'
#     html = get_pagecontent(url,key)
#     get_txt(html,key)
#     ################
#
# def get_format_datetime(datestr):
#     now = datetime.datetime.now()
#     ymd = now.strftime("%Y-%m-%d")
#     y = now.strftime("%Y")
#     newstr = datestr
#     newdate = now
#
#     if ("今天" in newstr):
#         mdate = time.mktime(time.strptime(ymd + newstr, '%Y-%m-%d今天%H:%M'))
#         newdate = datetime.datetime.fromtimestamp(mdate)
#     elif ("年" in newstr):
#         newdate = datetime.datetime.strptime(newstr, '%Y年%m月%d日 %H:%M')
#     elif ("月" in newstr):
#         mdate = time.mktime(time.strptime(y + newstr, '%Y%m月%d日 %H:%M'))
#         newdate = datetime.datetime.fromtimestamp(mdate)
#     elif ("分钟前" in newstr):
#         newdate = now - datetime.timedelta(minutes=int(newstr[:-3]))
#     elif ("秒前" in newstr):
#         newdate = now - datetime.timedelta(seconds=int(newstr[:-2]))
#     return newdate
#
# def get_weibocontent(url):
#     header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}
#     res = requests.get(url,headers =header )
#     res.encoding = "uft-8"
#     selector = etree.HTML(res.text)
#     contents = []
#     content_all = selector.xpath('//*[@id="pl_feedlist_index"]/div[1]/div/div/div[1]/div[2]/p[1]')
#     for content in content_all:
#         content = content.xpath('string(.)')
#         contents.append(content.strip())
#
#
#     weibotimes =selector.xpath('//*[@class="content"]/p[@class="from"]/a[1]/text()')
#     weibotimes = list(map(lambda x: x.strip(),weibotimes))
#     weibotimes = list(map(lambda x: get_format_datetime(x),weibotimes))
#
#     hrefs =selector.xpath('//*[@class="content"]/p[@class="from"]/a[1]/@href')
#     zf = selector.xpath('//*[@class="card-act"]/ul/li[2]/a/text()')
#     zf = list(map(lambda x:x.replace('转发 ',''),zf))
#     zf = list(map(lambda x: 0 if len(x)==0 else x,zf))
#     pl = selector.xpath('//*[@class="card-act"]/ul/li[3]/a/text()')
#     pl = list(map(lambda x:x.replace('评论 ',''),pl))
#     pl = list(map(lambda x: 0 if len(x)==0 else x,pl))
#     dianzans = selector.xpath('//*[@class="card-act"]/ul/li[4]/a/em')
#     dz = []
#     for dianzan in dianzans:
#         if dianzan.xpath('text()'):
#             dianzan = dianzan.xpath('text()')[0]
#             dz.append(dianzan)
#         else:
#             dz.append(0)
#     return contents, weibotimes, hrefs, pl,dz
#
#
# def load_weibodata(contents, weibotimes, hrefs, pl,dz,key):
#     db= pymysql.connect(host="localhost",user="root",password="1234",db="rxgl",port=3306)
#    # db= pymysql.connect(host="localhost",user="root",password="187490",db="2.1",port=3306)
#     # 使用cursor()方法获取操作游标
#     # SQL 插入语句
#     for i in range(len(contents)):
#         if int(time.mktime(weibotimes[i].timetuple()))> time.time()-604800:
#             cur=db.cursor()
#             sql = "INSERT INTO yuqing_yqin(publish_time,title,hf,ck,url,ly,gjc)VALUES (%s,%s,%s,%s,%s,%s,%s)"
#             v1 = weibotimes[i]
#             v2 = contents[i]
#             # print(pl)
#             v3 = pl[i]
#             # print(dz)
#             v4 = dz[i]
#             v5 = hrefs[i]
#             v6 = '新浪微博'
#             v7 = key
#             cur.execute(sql,(v1,v2,v3,v4,v5,v6,v7))
#     db.commit()
#     db.close()
#
# def main_weibo(key):
#     url = "https://s.weibo.com/weibo?q=" +list_key[0]+key+"&Refer=index&page="+"1"
#     contents, weibotimes , hrefs, pl,dz = get_weibocontent(url)
#     load_weibodata(contents, weibotimes, hrefs, pl,dz,key)
#
#
# def qk():
#     db = pymysql.connect("localhost", "root", "1234", "rxgl", charset="utf8mb4")
#     cur = db.cursor()
#     cur.execute("truncate yuqing_yqin")
#     # cur.execute("INSERT INTO yq_out(publish_time, title, hf, ck, url, ly, gjc)select publish_time publish_time, title title, hf hf, ck ck, url url, ly ly, gjc gjc from yq_in group by DATE_FORMAT (publish_time,'%Y-%m-%d') order by publish_time desc")
#     db.commit()
#     db.close()
#
#
# def copy_data():
#     db = pymysql.connect(host="localhost", user="root", password="1234", db="rxgl", port=3306, charset="utf8")
#     cur = db.cursor()
#     cur.execute('ALTER TABLE yuqing_yqout CONVERT TO CHARACTER SET utf8mb4')
#     cur.execute("truncate yuqing_yqout")
#     cur.execute("INSERT INTO yuqing_yqout(publish_time, title, hf, ck, url, ly, gjc)select publish_time publish_time, title title, hf hf, ck ck, url url, ly ly, gjc gjc from yuqing_yqin order by publish_time desc")
#     db.commit()
#     db.close()

def pp():
    # qk()
    # gjc_list = []
    gjc_list=models.gjc.objects.all()
    # print(gjc_list)
    for i in gjc_list:
        print(i.title)
        # key = i.title
        # print(key)
    #     main_hlx(key)
    #     # main_zww(key)
    #     # main_weibo(key)
    # copy_data()
    # print(time.asctime( time.localtime(time.time()) ))

if __name__=="__main__":
    # while True:
        # try:
        #     pp()
        #     time.sleep(1800)
        # except:
        #     print("出错")

    pp()



    

