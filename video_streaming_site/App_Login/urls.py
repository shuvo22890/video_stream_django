from django.urls import path
from . import views

app_name = 'App_Login'

urlpatterns = [
    path('signup/', views.user_sign_up, name='signup'),
    path('login/', views.user_login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout_user, name='logout'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('view/<vidId>/', views.see_review, name='view'),
    path('user_other/<pk>/', views.user_other, name='user_other'),
]
