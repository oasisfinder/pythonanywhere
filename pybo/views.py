
# Create your views here.

from django.shortcuts import render, get_object_or_404
from .models import Menu


def index(request):
    menu_list = Menu.objects.all()
    # for menu in menu_list:
    #     print(menu.name, menu.type, menu.distance, menu.price)

    context = {'menu_list': menu_list}


    return render(request, 'pybo/menu_list.html', context)


def detail(request,menu_id):
    menu = Menu.objects.get(id=menu_id)
    # menu_list = Menu.objects.all()
    context = {'menu': menu}

    return render(request, 'pybo/menu_detail.html', context)

def random(request):
    import random
    queryset = Menu.objects.all()
    count = queryset.count()  # 데이터베이스에서 개수를 직접 가져옴
    if count > 0:
       random_no = random.randrange(1,count)
       menu = Menu.objects.get(id=random_no)
       context = {'menu': menu}

    else :
        context = {}

    return render(request, 'pybo/random.html', context)
