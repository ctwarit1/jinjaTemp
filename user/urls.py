from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.UserLogin.as_view(), name='login'),
    path('register/', views.UserReg.as_view(), name='register'),
    path('profile/', views.UserProfile.as_view(), name='profile'),
    path('logout/', views.user_logout, name='logout'),
]