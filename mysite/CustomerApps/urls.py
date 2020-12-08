from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_app, name='add_app'),
    path('<str:token>/', views.app, name='app'),
    path('<str:token>/delete/', views.delete_app, name='delete_app')
]