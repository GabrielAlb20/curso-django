from django.urls import path

from . import views

urlpatterns = [
    path('', views.home), # Home
    path('recipes/<int:id>/', views.recipe), # Recipe
]