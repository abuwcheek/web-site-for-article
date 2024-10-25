from django.urls import path
from django.contrib.auth import views as auth_views
from .views import UserRegisterView, MyProfileView, UpdateUserView, ChangePasswordView, LoginView, LogoutView, ContactView, SearchView



app_name = "account"
urlpatterns = [
     path('sign-up/', UserRegisterView.as_view(), name='signup'),
     path('my-profile/', MyProfileView.as_view(), name='myprofile'),
     path('update-profile/', UpdateUserView.as_view(), name='updateprofile'),
     path('change-password/', ChangePasswordView.as_view(), name='changepassword'),
     path('sign-in/', LoginView.as_view(), name='signin'),
     path('logout/', LogoutView.as_view(), name='logout'),
     path('contact/', ContactView.as_view(), name='contact'),
     path('search/', SearchView.as_view(), name='search'),


     path('password-reset/', auth_views.PasswordResetView.as_view(template_name='account/password_reset_form.html'), name='password_reset'),
     path('password-reset-done/', auth_views.PasswordResetDoneView.as_view(template_name='account/password_reset_done.html'), name='password_reset_done'),
     path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='account/password_reset_confirm.html'), name='password_reset_confirm'),
     path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view('account/password_reset_complete.html'), name='password_reset_complete'),
]