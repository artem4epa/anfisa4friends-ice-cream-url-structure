from django.urls import path

from . import views


# Файл urls.py

# ice_cream/urls.py
from django.urls import path
from . import views
app_name = 'ice_cream'
urlpatterns = [
    # Главная страница
    path('', views.index),
    # Страница со списком сортов мороженого
    path('ice_cream/', views.ice_cream_list),
    # Отдельная страница с информацией о сорте мороженого
    path('ice_cream/<pk>/', views.ice_cream_detail),
    path('first/', views.first, name='first_page')
]