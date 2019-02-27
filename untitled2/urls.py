"""untitled2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url,include
from  . import views
from stark.service.v1 import site
urlpatterns = [
    url(r'^admin/', admin.site.urls,name ='admin'),
    url(r'^login/', views.acc_login,name='login'),
    url(r'^logout/', views.acc_logout,name='logout'),
    url(r'^rxgl/', include('rxgl.urls')),
    url(r'^yuqing/', include('yuqing.urls')),
    url(r'^stark/', site.urls),

]
