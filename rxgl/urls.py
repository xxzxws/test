from django.conf.urls import url
from rxgl import views


urlpatterns = [
    # url(r'^index$', views.index),
    url(r'^czcsc/', views.czcsc,name='czcsc'),
    url(r'^czccl/', views.czccl,name='czccl'),
    url(r'^gjcsc/', views.gjcsc,name='gjcsc'),
    url(r'^gjccl/', views.gjccl,name='gjccl'),
    # url(r'^index/', views.index,name='index'),

]
