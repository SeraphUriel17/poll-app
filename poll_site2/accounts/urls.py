from django.urls import path
from accounts import views as account_views

urlpatterns = [
    path('',account_views.login,name="login"),
    path('login',account_views.login,name="login"),
    path('signup',account_views.signup,name="signup"),
]

