from django.urls import path
from . import views

# recipes:recipe
app_name = 'recipes'

urlpatterns = [
    path('', views.home, name="home"),
    path('category/<int:category_id>/',
         views.category, name='category'),
    path('recipes/<int:id>/', views.recipe, name="recipe"),
    path('recipes/search/', views.search, name="search")

]