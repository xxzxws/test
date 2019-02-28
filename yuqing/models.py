from django.db import models
# Create your models here.


class yqin(models.Model):
    '''咨询投诉列表'''
    publish_time = models.CharField(max_length=32,verbose_name='发布时间')
    title = models.CharField(max_length=300,verbose_name='标题')
    hf = models.CharField(max_length=30,verbose_name='回复数量')
    ck = models.CharField(max_length=32,verbose_name='查看量')
    url = models.CharField(max_length=500,verbose_name='连接')
    ly = models.CharField(max_length=64,verbose_name='来源网站')
    gjc = models.CharField(max_length=32,verbose_name='关键词')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '临时舆情信息'
        verbose_name_plural = '临时舆情信息'

class yqout(models.Model):
    '''咨询投诉列表'''
    publish_time = models.CharField(max_length=32,verbose_name='发布时间')
    title = models.CharField(max_length=300,verbose_name='标题')
    hf = models.CharField(max_length=30,verbose_name='回复数量')
    ck = models.CharField(max_length=32,verbose_name='查看量')
    url = models.CharField(max_length=500,verbose_name='连接')
    ly = models.CharField(max_length=64,verbose_name='来源网站')
    gjc = models.CharField(max_length=32,verbose_name='关键词')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '舆情信息'
        verbose_name_plural = '舆情信息'

class yqin1(models.Model):
    '''咨询投诉列表'''
    publish_time = models.CharField(max_length=32,verbose_name='发布时间')
    title = models.CharField(max_length=300,verbose_name='标题')
    hf = models.CharField(max_length=30,verbose_name='回复数量')
    ck = models.CharField(max_length=32,verbose_name='查看量')
    url = models.CharField(max_length=500,verbose_name='连接')
    ly = models.CharField(max_length=64,verbose_name='来源网站')
    gjc = models.CharField(max_length=32,verbose_name='关键词')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '实时舆情信息'
        verbose_name_plural = '实时舆情信息'

class yqout1(models.Model):
    '''咨询投诉列表'''
    publish_time = models.CharField(max_length=32,verbose_name='发布时间')
    title = models.CharField(max_length=300,verbose_name='标题')
    hf = models.CharField(max_length=30,verbose_name='回复数量')
    ck = models.CharField(max_length=32,verbose_name='查看量')
    url = models.CharField(max_length=500,verbose_name='连接')
    ly = models.CharField(max_length=64,verbose_name='来源网站')
    gjc = models.CharField(max_length=32,verbose_name='关键词')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '实时舆情信息'
        verbose_name_plural = '实时舆情信息'


class gjc(models.Model):
    '''咨询投诉列表'''
    title = models.CharField(max_length=300,verbose_name='标题')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '关键词'
        verbose_name_plural = '关键词'