from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:token>/', views.app, name='app'),
    path('add/', views.add_app, name='add_app')
]