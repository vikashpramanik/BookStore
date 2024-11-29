from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
   path("" , views.index , name='home'),

   path("contact" , views.contact , name='contact'),
     path('shop/', views.shop, name='shop'),      # shop page
    
    path('recipe/', views.recipe, name='recipe'),      # recipe page

    path('login/', views.login, name='login'),      # login page
    path('houseOfSky/', views.houseOfSky, name='houseOfSky'),      # houseOfSky page
  
    path('cart/', views.cart, name='cart'),      # cart page
    path('blog/', views.blog, name='blog'),      # blog page
    path('bestSellingItem/', views.bestSellingItem, name='bestSellingItem'),      # bestSellingItem page
    path('Anime/', views.Anime, name='Anime'),      # Anime page
    path('about/', views.about, name='about'),      # about page
]