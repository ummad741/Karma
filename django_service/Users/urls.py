from .views import *
from django.urls import path

urlpatterns = [
    path('Registration/', RegistrationView.as_view()),
]
