from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('user_logout/', views.user_logout, name='user_logout'),
    path('user_login/', views.user_login, name='user_login'),
    path('register/', views.register, name='register'),
    path('', views.index, name='index'),
]