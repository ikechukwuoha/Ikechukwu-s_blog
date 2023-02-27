from django.urls import path
from . import views


app_name = 'users'



urlpatterns = [
   # path('', views.landinPage, name='landingpage'),
    
    
    # Routes for Auhentication
    path('signup/', views.signUp, name='signup'),
    path('signin/', views.signIn, name='signin'),
    path('signout/', views.signOut, name='signout'),
]