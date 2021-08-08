from django.urls import path
from django.shortcuts import redirect
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [
# path('', RedirectView.as_view(url='/shome/')),
path('', views.home, name='home'),
path('register', views.register, name='register'),
path('login', views.loginuser, name='login'),
path('logout', views.logoutuser, name='logout'),
path('dashboard', views.dashboard, name='dashboard'),
path('add', views.add, name='add'),
path('delete/<int:id>/', views.delete_data, name='delete_data'),
path('update/<int:id>/', views.update_data, name='update_data'),

]