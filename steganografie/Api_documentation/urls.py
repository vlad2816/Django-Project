
from django.urls import path, include
from . import views
from .views import HideMessageView


urlpatterns = [
    path('', views.home, name='home'),
    path('hide/', HideMessageView.as_view(), name='hide'),
    path('decrypt/', views.decrypt, name='decrypt')
]
