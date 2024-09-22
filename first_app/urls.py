from django.urls import path
from . import views

urlpatterns = [
    path('', views.djangoForm),
    path('add/', views.home, name="homepage")
]