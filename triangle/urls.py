from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('accounts/dashboard/', views.dashboard, name='dashboard'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='reset_password'),
    path('accounts/password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_sent.html'), name='password_reset_done'),
    path('accounts/reset/<uibd64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    

]