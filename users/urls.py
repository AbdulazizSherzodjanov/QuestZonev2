from django.urls import path
from .views import signUp, profile
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetConfirmView, \
    PasswordResetDoneView,PasswordResetCompleteView
urlpatterns = [
    path('signUp/', signUp, name='signUp-page'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login-page'),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='logout-page'),
    path('profile/', profile, name='profile-page'),
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
path('password_reset_complete', PasswordResetCompleteView.as_view(), name='password_reset_complete')
]
