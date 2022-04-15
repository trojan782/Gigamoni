from django.urls import path
from .views import CompanyStage2View, CompanyStage3View, UserRegisterView, CompanyStage1View, VerifyView

app_name = 'users'

urlpatterns = [
    path('register/user/', UserRegisterView.as_view(), name='user_register'),
    path('register/company1/', CompanyStage1View.as_view(), name='company_register'),
    path('register/company2/', CompanyStage2View.as_view(), name='company_register2'),
    path('register/company3/', CompanyStage3View.as_view(), name='company_register3'),
    path('verify/', VerifyView.as_view(), name='email-verify'),
]