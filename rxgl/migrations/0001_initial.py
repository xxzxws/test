# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-03-07 13:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rbac', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='bus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gdbh', models.CharField(max_length=64, unique=True, verbose_name='工单编号')),
                ('tsrq', models.DateField(max_length=30, verbose_name='投诉日期')),
                ('lb', models.CharField(max_length=30, verbose_name='线路')),
                ('bus_number', models.CharField(max_length=64, verbose_name='车牌号')),
                ('bus_zbh', models.CharField(max_length=64, verbose_name='自编号')),
                ('sfrq', models.CharField(max_length=64, verbose_name='事发日期')),
                ('wait_time', models.CharField(max_length=32, verbose_name='等待时间')),
                ('geton_time', models.CharField(max_length=32, verbose_name='上车时间')),
                ('geton_address', models.CharField(max_length=600, verbose_name='上车地点')),
                ('getoff_time', models.CharField(max_length=64, verbose_name='下车时间')),
                ('getoff_address', models.CharField(max_length=600, verbose_name='下车地点')),
                ('sqlb', models.CharField(choices=[('站点设置不合理', '站点设置不合理'), ('线路规划/调整', '线路规划/调整'), ('未按站点停靠/到站不停靠/二次停站', '未按站点停靠/到站不停靠/二次停站'), ('车辆车况', '车辆车况'), ('运行时间问题（晚点)', '运行时间问题（晚点)'), ('服务质量', '服务质量'), ('消极驾驶', '消极驾驶'), ('一卡通问题', '一卡通问题'), ('不安全（文明）行车', '不安全（文明）行车'), ('不照顾赶来的乘客', '不照顾赶来的乘客'), ('公交站台、设施问题', '公交站台、设施问题'), ('事故纠纷', '事故纠纷'), ('不文明行为', '不文明行为'), ('不开空调', '不开空调'), ('拒载', '拒载'), ('开车车速慢', '开车车速慢'), ('其他', '其他')], max_length=64, verbose_name='诉求类别')),
                ('slnr', models.TextField(max_length=1000, verbose_name='受理内容')),
            ],
            options={
                'verbose_name': '公交车整理信息',
                'verbose_name_plural': '公交车整理信息',
            },
        ),
        migrations.CreateModel(
            name='czc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gdbh', models.CharField(max_length=64, unique=True, verbose_name='工单编号')),
                ('slsj', models.DateTimeField(max_length=64, verbose_name='受理时间')),
                ('sllx', models.CharField(max_length=30, verbose_name='受理类型')),
                ('slnr', models.TextField(max_length=1000, verbose_name='受理内容')),
                ('gdsx', models.CharField(max_length=1000, verbose_name='工单时限')),
                ('slr', models.CharField(max_length=64, verbose_name='受理人员')),
                ('ly', models.CharField(max_length=64, verbose_name='来源')),
                ('zbdw', models.CharField(max_length=64, verbose_name='主办单位')),
                ('gdzt', models.CharField(max_length=64, verbose_name='工单状态')),
                ('zjzt', models.CharField(max_length=64, verbose_name='质检状态')),
                ('cbdw', models.CharField(max_length=64, verbose_name='承办单位')),
                ('cbyj', models.CharField(max_length=1000, verbose_name='承办意见')),
                ('czlx', models.CharField(default='巡游出租车', max_length=32, verbose_name='出租车类型')),
            ],
            options={
                'verbose_name': '出租车工单信息',
                'verbose_name_plural': '出租车工单信息',
            },
        ),
        migrations.CreateModel(
            name='department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='部门')),
            ],
            options={
                'verbose_name': '部门表',
                'verbose_name_plural': '部门表',
            },
        ),
        migrations.CreateModel(
            name='gjc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gdbh', models.CharField(max_length=64, unique=True, verbose_name='工单编号')),
                ('slsj', models.DateTimeField(max_length=30, verbose_name='受理时间')),
                ('sllx', models.CharField(max_length=30, verbose_name='受理类型')),
                ('slnr', models.TextField(max_length=1000, verbose_name='受理内容')),
                ('gdsx', models.CharField(max_length=64, verbose_name='工单时限')),
                ('slr', models.CharField(max_length=64, verbose_name='受理人员')),
                ('ly', models.CharField(max_length=64, verbose_name='来源')),
                ('zbdw', models.CharField(max_length=64, verbose_name='主办单位')),
                ('gdzt', models.CharField(max_length=64, verbose_name='工单状态')),
                ('zjzt', models.CharField(max_length=64, verbose_name='质检状态')),
                ('cbdw', models.CharField(max_length=64, verbose_name='承办单位')),
                ('cbyj', models.TextField(max_length=1000, verbose_name='承办意见')),
            ],
            options={
                'verbose_name': '公交车基础数据',
                'verbose_name_plural': '公交车基础数据',
            },
        ),
        migrations.CreateModel(
            name='taxi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gdbh', models.CharField(max_length=64, unique=True, verbose_name='工单编号')),
                ('tsrq', models.DateField(max_length=30, verbose_name='投诉日期')),
                ('company', models.CharField(choices=[('巴士出租', '巴士出租'), ('常运出租', '常运出租'), ('东方出租', '东方出租'), ('东吴出租', '东吴出租'), ('华泰出租', '华泰出租'), ('吉达出租', '吉达出租'), ('交服出租', '交服出租'), ('捷安出租', '捷安出租'), ('捷达出租', '捷达出租'), ('凯凯商务', '凯凯商务'), ('联创出租', '联创出租'), ('苏南交运', '苏南交运'), ('外汽出租', '外汽出租'), ('武进汽运', '武进汽运'), ('武进顺发', '武进顺发'), ('新联龙城', '新联龙城'), ('众联出租', '众联出租'), ('新能源出租', '新能源出租'), ('金坛天霸', '金坛天霸'), ('金坛金港', '金坛金港'), ('金坛鑫大', '金坛鑫大'), ('溧阳出租', '溧阳出租'), ('八达旅游', '八达旅游'), ('无', '无')], max_length=64, verbose_name='所属公司')),
                ('taxi_number', models.CharField(max_length=64, verbose_name='车牌号')),
                ('sfrq', models.CharField(max_length=64, verbose_name='事发日期')),
                ('geton_time', models.CharField(max_length=32, verbose_name='上车时间')),
                ('geton_address', models.CharField(max_length=600, verbose_name='上车地点')),
                ('getoff_time', models.CharField(max_length=64, verbose_name='下车时间')),
                ('getoff_address', models.CharField(max_length=600, verbose_name='下车地点')),
                ('sqlb', models.CharField(choices=[('绕路', '绕路'), ('不使用计价器', '不使用计价器'), ('不提供票据', '不提供票据'), ('异地经营', '异地经营'), ('公司经营纠纷', '公司经营纠纷'), ('不文明驾驶', '不文明驾驶'), ('计价器问题', '计价器问题'), ('多收费', '多收费'), ('甩客', '甩客'), ('爽约', '爽约'), ('擅自拼车', '擅自拼车'), ('拒载', '拒载'), ('服务质量', '服务质量'), ('其他', '其他')], max_length=64, verbose_name='诉求类别')),
                ('slnr', models.TextField(max_length=1000, verbose_name='受理内容')),
                ('czlx', models.CharField(default='巡游出租车', max_length=1000, verbose_name='出租车类型')),
            ],
            options={
                'verbose_name': '出租车整理信息',
                'verbose_name_plural': '出租车整理信息',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('phone', models.CharField(max_length=32, verbose_name='联系方式')),
                ('level', models.IntegerField(choices=[(1, '主任'), (2, '科长'), (3, '副科'), (4, '科员'), (5, '职工')], verbose_name='级别')),
                ('depart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rxgl.department', verbose_name='部门')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='rbac.UserInfo')),
            ],
        ),
    ]
