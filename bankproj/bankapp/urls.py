from . import views
from django.urls import path
app_name = 'bankapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('application', views.apply, name='apply'),
    path('control', views.control, name='control'),
    path('about', views.about, name='about'),
]

