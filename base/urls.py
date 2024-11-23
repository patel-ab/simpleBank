from django.urls import path
from . import views



urlpatterns = [
    path("", views.default, name="Default"),
    path('login/', views.login, name="Login"),
    path('home/', views.home, name="Home"),
    path('signup/', views.signup, name="signup"),
    path('signout/', views.signout, name="signout"),
    path('transfer/', views.zelle, name="zelle"),
]