from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='petitions.index'),
    path('create_petition/', views.create_petition, name='petitions.create_petition'),
]
