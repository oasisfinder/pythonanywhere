# Create your views here.
import urllib.parse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Menu, Memo, ImageURL
from django.db.models import Q
from .form import MenuSearchForm, MenuCreateForm

def naver_search(request, menu_id):
    menu = get_object_or_404(Menu, id=menu_id)
    encoded_query = urllib.parse.quote(f"{menu.name} {menu.location}")
    naver_search_url = f"https://search.naver.com/search.naver?query={encoded_query}"
    return redirect(naver_search_url)


def random(request):
    import random
    form = MenuSearchForm(request.GET)
    random_menu = None

    if form.is_valid():
        type = form.cleaned_data.get('type')
        location = form.cleaned_data.get('location')
        menus = Menu.objects.filter(confirmed='Y')
        if type:
            menus = menus.filter(type=type)
        if location:
            menus = menus.filter(location=location)
        if menus.exists():
            random_menu = random.choice(menus)
            encoded_query = urllib.parse.quote(f"{random_menu.name} {random_menu.location}")
            naver_search_url = f"https://search.naver.com/search.naver?query={encoded_query}"
    context = {
        'form': form,
        'random_menu': random_menu,
        'naver_search_url': naver_search_url
    }

    return render(request, 'pybo/random.html', context)


def index(request):
    kw = request.GET.get('kw', '')  # 검색어
    base_queryset = Menu.objects.filter(confirmed='Y')
    if kw:
        menu_list = base_queryset.filter(
            Q(name__icontains=kw) |  # 이름에 검색어가 포함된 항목
            Q(type__icontains=kw) |  # 타입에 검색어가 포함된
            Q(distance__icontains=kw)|
            Q(menu_detail__icontains=kw)|
            Q(location__icontains=kw)
        ).distinct()  # 중복 제거
    else:
        menu_list = Menu.objects.filter(confirmed='Y')  # 검색어가 없으면 모든 항목 가져오기

    context = {'menu_list': menu_list, 'kw': kw}
    return render(request, 'pybo/menu_list.html', context)

def detail(request,menu_id):
    menu = Menu.objects.get(id=menu_id)
    # menu_list = Menu.objects.all()

    naver_search_url = f"https://search.naver.com/search.naver?query={menu.location} {menu.name}"
    context = {'menu': menu, 'naver_search_url': naver_search_url}

    return render(request, 'pybo/menu_detail.html', context)



def memo_view(request):  # 함수 이름을 memo에서 memo_view로 변경
    memos = Memo.objects.order_by('status') # Memo.objects.all()을 사용하여 모든 Memo 객체 가져오기
    context = {'memos': memos}
    return render(request, 'pybo/memo.html', context)


def gia_view(request):
    image_url = ImageURL.objects.first()
    return render(request, 'pybo/gia.html',{'image_url': image_url})

def menu_create(request):
    if request.method == 'POST':
        form = MenuCreateForm(request.POST)
        if form.is_valid():
            menu = form.save(commit=False)
            menu.save()
            return redirect('pybo:index')
    else:
        form = MenuCreateForm()
    context ={'form':form}
    return render(request, 'pybo/menu_form.html',context)
