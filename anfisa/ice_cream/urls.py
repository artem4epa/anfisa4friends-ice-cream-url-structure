from django.urls import path

from . import views


# Файл urls.py

# ice_cream/urls.py
from django.conf import settings
from django.conf.urls.static import static
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
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)