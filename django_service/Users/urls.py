from .views import *
from django.urls import path
# from rest_framework_simplejwt.views import TokenRefreshView,


urlpatterns = [
    path('Registration/', RegistrationView.as_view()),
    path('Logout/', LogoutView.as_view()),
    path('Login/', LoginView.as_view())
]