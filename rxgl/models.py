from django.db import models
from django.contrib.auth.models import User
from rbac.models import *

class czc(models.Model):
    '''咨询投诉列表'''
    gdbh = models.CharField(max_length=64,unique=True,verbose_name='工单编号')
    slsj = models.DateTimeField(max_length=64,verbose_name='受理时间')
    sllx = models.CharField(max_length=30,verbose_name='受理类型')
    slnr = models.TextField(max_length=1000,verbose_name='受理内容')
    gdsx = models.CharField(max_length=1000,verbose_name='工单时限')
    slr = models.CharField(max_length=64,verbose_name='受理人员')
    ly = models.CharField(max_length=64,verbose_name='来源')
    zbdw = models.CharField(max_length=64,verbose_name='主办单位')
    gdzt = models.CharField(max_length=64,verbose_name='工单状态')
    zjzt = models.CharField(max_length=64,verbose_name='质检状态')
    cbdw = models.CharField(max_length=64,verbose_name='承办单位')
    cbyj = models.CharField(max_length=1000,verbose_name='承办意见')
    czlx = models.CharField(max_length=32,verbose_name='出租车类型',default='巡游出租车')

    def __str__(self):
        return self.gdbh

    class Meta:
        verbose_name = '出租车工单信息'
        verbose_name_plural = '出租车工单信息'

class taxi(models.Model):
    '''咨询投诉列表'''
    gdbh = models.CharField(max_length=64,unique=True,verbose_name='工单编号')
    tsrq = models.DateField(max_length=30,verbose_name='投诉日期')
    company_choice = (
        ("巴士出租","巴士出租"),
        ("常运出租","常运出租"),
        ("东方出租","东方出租"),
        ("东吴出租","东吴出租"),
        ("华泰出租","华泰出租"),
        ("吉达出租","吉达出租"),
        ("交服出租","交服出租"),
        ("捷安出租","捷安出租"),
        ("捷达出租","捷达出租"),
        ("凯凯商务","凯凯商务"),
        ("联创出租","联创出租"),
        ("苏南交运","苏南交运"),
        ("外汽出租","外汽出租"),
        ("武进汽运","武进汽运"),
        ("武进顺发","武进顺发"),
        ("新联龙城","新联龙城"),
        ("众联出租","众联出租"),
        ("新能源出租","新能源出租"),
        ("金坛天霸","金坛天霸"),
        ("金坛金港","金坛金港"),
        ("金坛鑫大","金坛鑫大"),
        ("溧阳出租","溧阳出租"),
        ("八达旅游","八达旅游"),
        ("无","无"),
    )
    company = models.CharField(max_length=64,verbose_name='所属公司',choices=company_choice)
    taxi_number = models.CharField(max_length=64,verbose_name='车牌号')
    sfrq = models.CharField(max_length=64,verbose_name='事发日期')
    geton_time = models.CharField(max_length=32,verbose_name='上车时间')
    geton_address = models.CharField(max_length=600,verbose_name='上车地点')
    getoff_time = models.CharField(max_length=64,verbose_name='下车时间')
    getoff_address = models.CharField(max_length=600,verbose_name='下车地点')
    sqlb_choices= (('绕路','绕路'),
        ('不使用计价器','不使用计价器'),
        ('不提供票据','不提供票据'),
        ('异地经营','异地经营'),
        ('公司经营纠纷','公司经营纠纷'),
        ('不文明驾驶','不文明驾驶'),
        ('计价器问题','计价器问题'),
        ('多收费','多收费'),
        ('甩客','甩客'),
        ('爽约','爽约'),
        ('擅自拼车','擅自拼车'),
        ('拒载','拒载'),
        ('服务质量','服务质量'),
        ('其他','其他'),)
    sqlb = models.CharField(max_length=64,choices=sqlb_choices,verbose_name='诉求类别')
    # sqlb = models.CharField(max_length=64,verbose_name='诉求类别')
    slnr = models.TextField(max_length=1000,verbose_name='受理内容')
    czlx = models.CharField(max_length=1000,verbose_name='出租车类型',default='巡游出租车')



    def __str__(self):
        return self.gdbh

    class Meta:
        verbose_name = '出租车整理信息'
        verbose_name_plural = '出租车整理信息'


class gjc(models.Model):
    '''咨询投诉列表'''
    gdbh = models.CharField(max_length=64,unique=True,verbose_name='工单编号')
    slsj = models.DateTimeField(max_length=30,verbose_name='受理时间')
    sllx = models.CharField(max_length=30,verbose_name='受理类型')
    slnr = models.TextField(max_length=1000,verbose_name='受理内容')
    gdsx = models.CharField(max_length=64,verbose_name='工单时限')
    slr = models.CharField(max_length=64,verbose_name='受理人员')
    ly = models.CharField(max_length=64,verbose_name='来源')
    zbdw = models.CharField(max_length=64,verbose_name='主办单位')
    gdzt = models.CharField(max_length=64,verbose_name='工单状态')
    zjzt = models.CharField(max_length=64,verbose_name='质检状态')
    cbdw = models.CharField(max_length=64,verbose_name='承办单位')
    cbyj = models.TextField(max_length=1000,verbose_name='承办意见')

    def __str__(self):
        return self.gdbh

    class Meta:
        verbose_name = '公交车基础数据'
        verbose_name_plural = '公交车基础数据'


class bus(models.Model):
    '''咨询投诉列表'''
    gdbh = models.CharField(max_length=64, unique=True, verbose_name='工单编号')
    tsrq = models.DateField(max_length=30, verbose_name='投诉日期')
    lb = models.CharField(max_length=30, verbose_name='线路')
    bus_number = models.CharField(max_length=64, verbose_name='车牌号')
    bus_zbh = models.CharField(max_length=64, verbose_name='自编号')
    sfrq = models.CharField(max_length=64, verbose_name='事发日期')
    wait_time = models.CharField(max_length=32, verbose_name='等待时间')
    geton_time = models.CharField(max_length=32, verbose_name='上车时间')
    geton_address = models.CharField(max_length=600, verbose_name='上车地点')
    getoff_time = models.CharField(max_length=64, verbose_name='下车时间')
    getoff_address = models.CharField(max_length=600, verbose_name='下车地点')
    sqlb_choices = (('站点设置不合理', '站点设置不合理'),
                    ('线路规划/调整', '线路规划/调整'),
                    ('未按站点停靠/到站不停靠/二次停站', '未按站点停靠/到站不停靠/二次停站'),
                    ('车辆车况', '车辆车况'),
                    ('运行时间问题（晚点)', '运行时间问题（晚点)'),
                    ('服务质量', '服务质量'),
                    ('消极驾驶', '消极驾驶'),
                    ('一卡通问题', '一卡通问题'),
                    ('不安全（文明）行车', '不安全（文明）行车'),
                    ('不照顾赶来的乘客', '不照顾赶来的乘客'),
                    ('公交站台、设施问题', '公交站台、设施问题'),
                    ('事故纠纷', '事故纠纷'),
                    ('不文明行为', '不文明行为'),
                    ('不开空调', '不开空调'),
                    ('拒载', '拒载'),
                    ('开车车速慢', '开车车速慢'),
                    ('其他', '其他'),)
    sqlb = models.CharField(max_length=64, verbose_name='诉求类别', choices=sqlb_choices)
    slnr = models.TextField(max_length=1000, verbose_name='受理内容')

    def __str__(self):
        return self.gdbh

    class Meta:
        verbose_name = '公交车整理信息'
        verbose_name_plural = '公交车整理信息'

class User(models.Model):
    '''用户信息表'''
    user = models.OneToOneField(to=UserInfo,null=True)
    name = models.CharField(max_length=32)
    # roles = models.ManyToManyField('Role',blank=True)
    phone = models.CharField(verbose_name='联系方式', max_length=32)
    level_choices = (
        (1, '主任'),
        (2, '科长'),
        (3, '副科'),
        (4, '科员'),
        (5, '职工'),
    )
    level = models.IntegerField(verbose_name='级别', choices=level_choices)

    depart = models.ForeignKey(verbose_name='部门', to='department')


class department(models.Model):
    title = models.CharField(verbose_name="部门", max_length=64)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '部门表'
        verbose_name_plural = '部门表'


# class Menus(models.Model):
#     '''动态菜单'''
#     name = models.CharField(max_length=32)
#     url_type_choices = ((0,'absolute'),(1,'dynamic'),)
#     url_type = models.SmallIntegerField(choices=url_type_choices,default=0)
#     url_name = models.CharField(max_length=64,unique=True)
#     def __str__(self):
#         return self.name
#     class Meta:
#         unique_together =('name','url_name')
#         verbose_name='菜单名'
#         verbose_name_plural='菜单名'


# class Role(models.Model):
#     '''角色表'''
#     name = models.CharField(max_length=32,unique=True)
#     menus = models.ManyToManyField("Menus",blank=True)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name='角色表'
#         verbose_name_plural='角色表'