from django.urls import path
from . import views

urlpatterns= [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('getinformation/', views.get_user_information, name='get_user_information'),
    path('validate/', views.validate_email, name='validate_email')
]