"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))

"""
from django.conf.urls import url
from django.contrib import admin
from mysite1 import views

urlpatterns = [
    url(r'^admin/',admin.site.urls),
    url(r'^$',views.createuser,name='createuser'),
    url(r'^createuser/$',views.createuser,name='createuser'),
    url(r'^query$', views.query, name='query'),

    url(r'^newuser$',views.newuser,name='newuser'),
    url(r'^index$',views.index,name='index'),
    url(r'^login$',views.login,name='login'),
    url(r'^roomv$',views.roomv,name='roomv'),
    url(r'^roomt$', views.roomt, name='roomt'),
    url(r'^normaluser$',views.normaluser,name='normaluser'),
    url(r'^logout$',views.logout,name='logout'),
    url(r'^buildinguserv$', views.buildinguserv, name='buildinguserv'),
    url(r'^messagev$', views.messagev, name='messagev'),
    url(r'^adminuserv$', views.adminuserv, name='adminuserv'),
    url(r'^departmentv$', views.departmentv, name='departmentv'),
]
'''
    url(r'^$',views.login,name='login'),
    url(r'^$',views.auth_view,name='auth'),
    url(r'^$',views.logout_view,name='logout'),
    url(r'^$',views.loggedin_view,name='loggedin'),
    url(r'^$',views.invalidlogin_view,name='invalidlogin'),
'''

