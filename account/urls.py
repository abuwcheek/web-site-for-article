from django.urls import path
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
]