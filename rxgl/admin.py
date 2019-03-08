from django.contrib import admin
from django.contrib import admin
from rxgl import models

class czcAdmin(admin.ModelAdmin):
    list_display = ('gdbh',"slsj","sllx",'gdsx','slr','ly','zbdw','gdzt','zjzt','cbdw','czlx')
    list_filter = ("sllx",'slr','ly','gdzt','zjzt','czlx')
    search_fields = ('gdbh',"slsj","sllx",'slnr','gdsx','slr','ly','zbdw','gdzt','zjzt','czlx')#外键搜索必须确定搜哪一个字段
    # search_fields = ('contact','consultant_name')#外键搜索必须确定搜哪一个字段
    # raw_id_fields = ('consult_course',)
    # filter_horizontal = ('tags',)
    # list_editable = ('status',)
    list_per_page = 20
    date_hierarchy = 'slsj'
# class UserProfileAdmin(admin.ModelAdmin):
#     list_display = ('user','name',)


class taxiAdmin(admin.ModelAdmin):
    list_display = ('gdbh',"tsrq","company",'taxi_number','sfrq','geton_time','geton_address','getoff_time','getoff_address','sqlb','slnr','czlx')
    list_filter = ("tsrq",'company','sqlb','czlx')
    search_fields = ('gdbh',"tsrq","company",'taxi_number','sfrq','sqlb')#外键搜索必须确定搜哪一个字段
    # search_fields = ('contact','consultant_name')#外键搜索必须确定搜哪一个字段
    # raw_id_fields = ('consult_course',)
    # filter_horizontal = ('tags',)
    # list_editable = ('status',)
    list_per_page = 20
    date_hierarchy = 'tsrq'


# class UserProfileAdmin(admin.ModelAdmin):
#     list_display = ('user','name',)

class gjcAdmin(admin.ModelAdmin):
    list_display = ('gdbh',"slsj","sllx",'gdsx','slr','ly','zbdw','gdzt','zjzt','cbdw')
    list_filter = ("sllx",'slr','ly','gdzt','zjzt')
    search_fields = ('gdbh',"slsj","sllx",'slnr','gdsx','slr','ly','zbdw','gdzt','zjzt')#外键搜索必须确定搜哪一个字段
    # search_fields = ('contact','consultant_name')#外键搜索必须确定搜哪一个字段
    # raw_id_fields = ('consult_course',)
    # filter_horizontal = ('tags',)
    # list_editable = ('status',)
    list_per_page = 20
    date_hierarchy = 'slsj'
# class UserProfileAdmin(admin.ModelAdmin):
#     list_display = ('user','name',)


class busAdmin(admin.ModelAdmin):
    list_display = ('gdbh',"tsrq","lb",'bus_number','bus_zbh','sfrq','wait_time','geton_time','geton_address','getoff_time','getoff_address','sqlb','slnr')
    list_filter = ("tsrq",'sqlb')
    search_fields = ('gdbh',"tsrq","lb",'bus_number','sfrq','sqlb','bus_zbh')#外键搜索必须确定搜哪一个字段
    # search_fields = ('contact','consultant_name')#外键搜索必须确定搜哪一个字段
    # raw_id_fields = ('consult_course',)
    # filter_horizontal = ('tags',)
    # list_editable = ('status',)
    list_per_page = 20
    date_hierarchy = 'tsrq'


# class MenusAdmin(admin.ModelAdmin):
#     list_display=('name','url_name')




admin.site.register(models.czc,czcAdmin)
admin.site.register(models.gjc,gjcAdmin)
# admin.site.register(models.Menus,MenusAdmin)
admin.site.register(models.taxi,taxiAdmin)
admin.site.register(models.bus,busAdmin)
# admin.site.register(models.Role)
# admin.site.register(models.UserInfo)
