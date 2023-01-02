from django.urls import path
from .views import *
# import login view inbuild
from django.contrib.auth import views as authentication_view

app_name = 'users'
urlpatterns = [
    
    # path('register/',register, name="register"),
    # path('register/',register1, name="register1"),
    path('sign_up/',sign_up, name="sign_up"),
    # class base login(.as_view())
    path('login/', authentication_view.LoginView.as_view(template_name="users/login.html"), name="login"), 
    path('logout/',authentication_view.LogoutView.as_view(template_name="users/logout.html"), name="logout"),
    path('profile/',profile, name="profile"),
    path('createprofile/',createprofile, name="createprofile"),
    path('seller_profile/<int:id>/',seller_profile, name="seller_profile"),
    # path('Products/',Products, name="Products"),
    # path('Products/<int:id>',product_detail, name="product_detail"),
   
]
