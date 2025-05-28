from django.urls import path
from . import views

urlpatterns = [
    path('new_view/', views.new_view, name='new_view'),
    path('', views.new_view, name='home'),
]