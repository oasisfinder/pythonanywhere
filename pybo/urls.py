
from django.urls import path
from . import views

from .views import detail


app_name = 'pybo'


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:menu_id>/', views.detail, name = 'detail'),
    path('random/', views.random, name='random'),
    path('memo/', views.memo_view, name='memo'),
    path('gia/', views.gia_view, name='gia'),
    path('naver-search/<int:menu_id>/', views.naver_search, name='naver_search'),
    path('random/naver-search/<int:menu_id>/', views.naver_search, name='naver_search'),
    path('create/', views.menu_create, name='menu_create'),]

