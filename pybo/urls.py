
from django.urls import path
from . import views

from .views import detail


app_name = 'pybo'


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:menu_id>/', views.detail, name = 'detail'),
    path('random/', views.random, name='random'),
    path('memo/', views.memo_view, name='memo')]

