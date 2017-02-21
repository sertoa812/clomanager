'''
Created on 2016年4月6日

@author: dc
'''

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index,name = 'index'),
    url(r'^add_item',views.add_item,name='add_item'),
    url(r'^sub_item/(?P<id>\d+)',views.sub_item,name='sub_item'),
    url(r'^edit_item',views.edit_item,name='edit_item'),
    url(r'^show_detail/(?P<id>\d+)',views.show_detail,name='show_detail'),
    url(r'^do_up',views.do_up,name='do_up'),

    url(r'^sub_clothe/(?P<id>\d+)/(?P<menuid>\d+)',views.sub_clothe,name='sub_clothe'),
    url(r'^main_menu_edit_show',views.main_menu_edit_show,name='main_menu_edit_show'),
    url(r'^main_menu_add',views.main_menu_add,name='main_menu_add'),
    url(r'^main_menu_edit',views.main_menu_edit,name='main_menu_edit'),
    url(r'^main_menu_delete/(?P<id>\d+)',views.main_menu_delete,name='main_menu_delete'),
    url(r'^edit_clothe',views.edit_clothe,name='edit_clothe'),
]
