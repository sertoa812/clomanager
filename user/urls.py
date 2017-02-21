'''
Created on 2016年4月1日

@author: dc
'''
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.login,name = 'login'),
    url(r'^dologin',views.dologin , name = 'dologin'),
    url(r'^regist',views.regist, name = "regist"),
    url(r'^dologout',views.dologout,name = 'dologout'),
    url(r'^userinfo',views.userInfo,name='userinfo'),
    url(r'^multiplebuy',views.multiplebuy,name='multiplebuy'),
    url(r'^singlebuy',views.singlebuy,name='singlebuy'),
    url(r'^password',views.passWordChange,name='changepwd'),
    url(r'^doregist',views.doregist,name='doregist'),
    url(r'^up',views.up,name='up'),
    url(r'^doup',views.doup,name='doup'),
    url(r'^down',views.down,name='down'),
    url(r'^rq',views.raisequestion,name='RaiseQuestion'),
    url(r'^question/(?P<id>\d+)',views.quelist,name='quelist'),
    url(r'^questionlist$',views.questionslist,name='questionlist'),
    url(r'^doans$',views.doans,name='doans')
]

