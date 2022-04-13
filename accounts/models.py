from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class User(AbstractUser):
    is_person = models.BooleanField(default=False)
    is_company = models.BooleanField(default=False)

    username = None
    email = models.EmailField(
        verbose_name='Email Address',
        max_length=255,
        unique=True
        )
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Person(models.Model):
    person = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    full_name = models.CharField(max_length=60, verbose_name='Fullname')
    # phone_number = PhoneNumberField(blank=True, region='NG', verbose_name='Phone number')
    phone_number = models.CharField(max_length=11, verbose_name="Phone number")

    REQUIRED_FIELDS = ['full_name', 'phone_number']

    def __str__(self):
        return self.person.email


class Company(models.Model):
    company = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)

    company_name = models.CharField(max_length=255, verbose_name="Company Name")
    company_type = models.CharField(max_length=255, verbose_name="Company Type")
    rc_no = models.CharField(max_length=12, verbose_name="RC NO")
    bank_details = models.CharField(max_length=120, verbose_name="details")
    bvn = models.CharField(max_length=12, verbose_name="BVN")
    utility_bill = models.CharField(max_length=120, verbose_name="Current Utility Bill")
    reference_letter = models.FileField(verbose_name="Letter of Reference")
    credit_check = models.CharField(max_length=120)

    REQUIRED_FIELDS=['company_name', 'company_type', 'rc_no', 'bank_details', 'bvn', 'utility_bill', 'reference_letter', 'credit_check']

    def __str__(self):
        return self.company.email
