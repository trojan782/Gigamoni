from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class GigaUserManager(BaseUserManager):
    def create_superuser(self, email, full_name, phone_number, password, **other_fields):
        """
        Creates and saves a superuser with the given email and password.
        """

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_superuser=True')
        
        return self.create_user(email, full_name, phone_number, password, **other_fields)


    def create_user(self, email, full_name, phone_number, password, **other_fields):
        """
        Creates and saves a staff user with the given email, full name, phone number and password.
        """
        if not email:
            raise ValueError("Users must have an email address")
        
        user = self.model(email=self.normalize_email(email), full_name=full_name,
            phone_number=phone_number, **other_fields)

        user.set_password(password)
        user.save()
        return user



class GigaUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='Email Address',
        max_length=255,
        unique=True
        )
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    full_name = models.CharField(max_length=60, verbose_name='Fullname')
    phone_number = PhoneNumberField(blank=True, region='NG', verbose_name='Phone number')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name', 'phone_number']

    objects = GigaUserManager()
    
    def get_full_name(self):
        return self.full_name
    
    def __str__(self):
        return self.email