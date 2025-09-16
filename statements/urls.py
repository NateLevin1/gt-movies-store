from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='statements.index'),
    path('create_statement/', views.create_statement, name='statements.create_statement'),
]
