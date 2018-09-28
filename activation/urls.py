from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('authenticate/', views.login_user, name='authenticate'),
    path('logout/', views.logout_user, name='logout'),
]
