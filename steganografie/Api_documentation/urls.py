
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('hide/', views.hide_text, name='hide')
]
