from django.contrib import admin
from yuqing import models
# Register your models here.
class gjcAdmin(admin.ModelAdmin):
    list_display = ('title',)


class yqoutAdmin(admin.ModelAdmin):
    list_display = ('title','publish_time','hf','ck','ly','gjc')
    list_filter = ('ly','gjc')


admin.site.register(models.gjc,gjcAdmin)
admin.site.register(models.yqout,yqoutAdmin)