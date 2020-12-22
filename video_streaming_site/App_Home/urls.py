from django.urls import path
from . import views

app_name = 'App_Home'

urlpatterns=[
    path('', views.home, name='home'),
    path('category/', views.cat, name='cat'),
    path('catVideo/<catId>/', views.catVideo, name='catVideo'),
]
