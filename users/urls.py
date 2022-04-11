from django.urls import path
from .views import RegisterView, VerifyView

app_name = 'users'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register-user'),
    path('verify/', VerifyView.as_view(), name='email-verify'),
]