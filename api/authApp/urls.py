from django.urls import path
from . import views

urlpatterns= [
    path('', views.say_hello, name='say_hello'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('getinformation/', views.get_user_information, name='get_user_information')
]