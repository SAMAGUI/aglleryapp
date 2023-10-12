from django.urls import path

from accounts import views


urlpatterns = [
    path('accounts/signup',views.signup,name='signup'),
    path('accounts/signin',views.signin,name='login'),
    path('accounts/logout',views.logoutUser,name='logout'),
]