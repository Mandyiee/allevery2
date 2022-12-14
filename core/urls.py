from django.urls import path
from . import views

urlpatterns = [
  path('',views.index,name='index'),
  path('about',views.about,name='about'),
  path('search',views.search,name='search'),
  path('logout',views.logout,name='logout'),
  path('login',views.login,name='login'),
  path('register',views.register,name='register'),
  path('interests',views.interest,name='interest'),
  path('explore',views.explore,name='explore'),
  ]