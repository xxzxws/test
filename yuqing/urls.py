from django.conf.urls import url
from yuqing import views


urlpatterns = [
    url(r'^yu_list/', views.yu_list),
    url(r'^gjc_list/', views.gjc_list),
    url(r'^gjc/', views.gjc),
    url(r'^sc/', views.sc),
    url(r'^zj/', views.zj),

]
