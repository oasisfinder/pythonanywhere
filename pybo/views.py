
# Create your views here.

from django.shortcuts import render, get_object_or_404
from .models import Menu
from django.db.models import Q
from .form import MenuSearchForm


def random(request):
    import random
    form = MenuSearchForm(request.GET)
    random_menu = None

    if form.is_valid():
        type = form.cleaned_data.get('type')
        location = form.cleaned_data.get('location')

        menus = Menu.objects.all()
        if type:
            menus = menus.filter(type=type)
        if location:
            menus = menus.filter(location=location)
        if menus.exists():
            random_menu = random.choice(menus)
    return render(request, 'pybo/random.html', {'form': form, 'random_menu': random_menu})


def index(request):
    kw = request.GET.get('kw', '')  # 검색어

    if kw:
        menu_list = Menu.objects.filter(
            Q(name__icontains=kw) |  # 이름에 검색어가 포함된 항목
            Q(type__icontains=kw) |  # 타입에 검색어가 포함된
            Q(distance__icontains=kw)|
            Q(menu_detail__icontains=kw)|
            Q(location__icontains=kw)
        ).distinct()  # 중복 제거
    else:
        menu_list = Menu.objects.all()  # 검색어가 없으면 모든 항목 가져오기

    context = {'menu_list': menu_list, 'kw': kw}
    return render(request, 'pybo/menu_list.html', context)

def detail(request,menu_id):
    menu = Menu.objects.get(id=menu_id)
    # menu_list = Menu.objects.all()
    context = {'menu': menu}

    return render(request, 'pybo/menu_detail.html', context)
