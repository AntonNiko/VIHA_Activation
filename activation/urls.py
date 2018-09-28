from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('authenticate/', views.login_user, name='authenticate'),
    path('logout/', views.logout_user, name='logout'),
    path('send_activation/', views.send_activation, name='send_activation'),
    path('actions/', views.actions, name='actions'),
    path('respond/<int:activation_id>/<str:verify_id>', views.respond_to_request, name='respond'),
    path('respond_response/', views.response_handle, name='response'),
]
