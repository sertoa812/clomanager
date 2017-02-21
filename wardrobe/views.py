from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.http.response import HttpResponse
from django.core.urlresolvers import reverse
from .models import Menu
from .models import Clothes
from .models import MainMenu
import datetime
import os

# Create your views here.
def index(request):
    context = {}

    main_menu_list_raw = MainMenu.objects.filter()
    main_menu_list = []
    for item in main_menu_list_raw:
        single = {}
        single['id'] = item.id
        single['Name'] = item.Name
        single['menu_list'] = Menu.objects.filter(Menu = item.id)
        main_menu_list.append(single)
    context['main_menu_list'] = main_menu_list
    return render(request,'wardrobe/Index.html',context)

def add_item(request):
    name = request.POST['name']
    main_menu_id = request.POST['main_menu']
    m_menu = Menu()
    main_menu = MainMenu.objects.get(id=main_menu_id)

    m_menu.Wardrobe = main_menu
    m_menu.Menu = main_menu_id
    m_menu.Detail = name
    m_menu.User = main_menu_id

    m_menu.save()
    return HttpResponseRedirect(reverse('Wardrobe:index',args=()))

def sub_item(request,id):
    menu_id = id
    m_menu = Menu.objects.get(id=menu_id)
    m_menu.delete()
    return HttpResponseRedirect(reverse('Wardrobe:index',args=()))

def edit_item(request):
    menu_id = request.POST['menu_id']
    menu_name = request.POST['menu_name']

    Menu.objects.filter(id = menu_id).update(Detail = menu_name)
    return HttpResponseRedirect(reverse('Wardrobe:show_detail',args=(menu_id)))

def show_detail(request,id):
    context={}
    context['username'] = 'dc'
    menu_id = id

    clothes = Clothes.objects.filter(Menu = menu_id)
    clothes_list = []

    #此类型衣服信息
    for item in clothes :
        clothe = {}
        clothe['time'] = item.Time
        print(item.Time)
        clothe['path'] = "/static/up/"+item.Detail.name[2:]
        clothe['note'] = item.Note
        clothe['id'] = item.id
        print(item.Note)
        clothes_list.append(clothe)

    #此类型路径信息
    m_menu = Menu.objects.get(id=menu_id)
    clothe_of = ['爸爸的衣橱','妈妈的衣橱','羽凡的衣橱']
    route_list = []
    route_first = {}
    route_first['name'] = MainMenu.objects.get(id = m_menu.User).Name
    route_list.append(route_first)
    route_second = {}
    route_second['name'] = m_menu.Detail
    route_list.append(route_second)
    print(route_list)

    #左侧菜单信息
    main_menu_list_raw = MainMenu.objects.filter()
    main_menu_list = []
    for item in main_menu_list_raw:
        single = {}
        single['id'] = item.id
        single['Name'] = item.Name
        single['menu_list'] = Menu.objects.filter(Menu=item.id)
        main_menu_list.append(single)


    context['main_menu_list'] = main_menu_list
    context['route_list'] = route_list
    context['clothes_list'] = clothes_list
    context['menu_id'] = menu_id

    print("test")

    return render(request,'wardrobe/Detail.html',context)
    pass

def do_up(request):
    m_clothe = Clothes()
    menu_id = request.POST['menu_id']
    note = request.POST['note']

    m_menu = Menu()
    m_menu = Menu.objects.get(id = menu_id)

    m_clothe.Menu = m_menu
    m_clothe.setClothes(Detail = request.FILES['clothes'] , Time = datetime.datetime.now())
    m_clothe.Note = note

    m_clothe.save()
    return HttpResponseRedirect(reverse('Wardrobe:show_detail',args=(menu_id)))

def edit_clothe(request):
    note = request.POST['clothe_name']
    id = request.POST['clothe_id']
    menu_id = request.POST['menu_id']

    Clothes.objects.filter(id = id).update(Note = note)
    return (HttpResponseRedirect(reverse('Wardrobe:show_detail',args=(menu_id))))

def sub_clothe(request,id,menuid):
    Clothes.objects.filter(id = id).delete()
    return HttpResponseRedirect(reverse('Wardrobe:show_detail',args=(menuid)))

def main_menu_edit_show(request):
    main_menu_list = MainMenu.objects.filter()
    context = {}
    context['main_menu_list'] = main_menu_list
    return render(request,'wardrobe/MenuEdit.html',context)

def main_menu_add(request):
    menu_name = request.POST['menu_name']

    main_menu = MainMenu()
    main_menu.Name = menu_name
    main_menu.save()

    return HttpResponseRedirect(reverse('Wardrobe:main_menu_edit_show',args=()))

def main_menu_delete(request,id):
    MainMenu.objects.filter(id = id).delete()
    return HttpResponseRedirect(reverse('Wardrobe:main_menu_edit_show', args=()))

def main_menu_edit(request):
    menu_id = request.POST['menu_id']
    name = request.POST['menu_name']

    main_menu = MainMenu.objects.get(id = menu_id)
    main_menu.Name = name
    main_menu.save()
    return HttpResponseRedirect(reverse('Wardrobe:main_menu_edit_show',args=()))



