from ast import Try
from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest_framework import permissions, generics, mixins, status, response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
import jwt
from core.settings import SECRET_KEY

from accounts.models import User, Person, Company
from .serializers import PersonSignUpSerializer, CompanyStage1Serializer, CompanyStage2Serializer, CompanyStage3Serializer
from .utils import Utils
from core.settings import SECRET_KEY

# Create your views here.
class UserRegisterView(generics.GenericAPIView, mixins.CreateModelMixin):
    permissions_classes=[permissions.AllowAny]
    serializer_class=PersonSignUpSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user_data = serializer.data
        user = Person.objects.get(email=user_data['email'])
        token = RefreshToken.for_user(user).access_token
        site = f"http://{get_current_site(request).domain}email-verify/?token={token}"

        email = {
            'email_body': f"Hi {user.full_name}, Use the link below to verify your email \n{site}",
            'email_subject': 'Verify your email',
            'to_email': (user.email,)
        }
        Utils.send_email(email)

        return response.Response(status=status.HTTP_201_CREATED)

class CompanyStage1View(generics.GenericAPIView, mixins.CreateModelMixin):
    permissions_classes=[permissions.AllowAny]
    serializer_class=CompanyStage1Serializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, **kwargs)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(status=status.HTTP_201_CREATED)

class CompanyStage2View(generics.UpdateAPIView):
    queryset = Company.objects.all()
    permissions_classes=[permissions.AllowAny]
    serializer_class = CompanyStage2Serializer

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

class CompanyStage3View(generics.UpdateAPIView):
    queryset = Company.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class = CompanyStage3Serializer

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
        
class VerifyView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        token = request.GET.get('token')
        try:
            payload = jwt.decode(jwt=token, algorithms=SECRET_KEY)
            users = User.objects.get(id=payload['user_id'])

            if not users.is_active:
                users.is_active=True
                users.save()
            return response.Response({'email': "Successfully activated"}, status=status.HTTP_200_OK)
        except jwt.exceptions.ExpiredSignatureError as identifier:
            return response.Response({'error': "Activation Expired"}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as identifier:
            return response.Response({'error': "Invalid Token"}, status=status.HTTP_400_BAD_REQUEST)
from django.shortcuts import render

# Create your views here.
