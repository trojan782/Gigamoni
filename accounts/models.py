from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class UserManager(BaseUserManager):

    def create_user(self, email, password, **other_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **other_fields)
        user.set_password(password)
        user.save()
        return user

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

    objects = UserManager()
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
    company_address = models.CharField(max_length=255, verbose_name="Company Address", default="Address")
    rc_no = models.CharField(max_length=12, verbose_name="RC NO")
    bank_details = models.CharField(max_length=120, verbose_name="Bank Details", default="details")
    bvn = models.CharField(max_length=12, verbose_name="BVN")
    utility_bill = models.CharField(max_length=120, verbose_name="Current Utility Bill", default="utility")
    reference_letter = models.FileField(verbose_name="Letter of Reference")
    contact_person_name = models.CharField(max_length=255, verbose_name='Contact Person Name', default="Name")
    contact_person_email = models.EmailField(max_length=255, verbose_name="Contact Person Email", default="mail@gmail.com")
    contact_person_number = models.CharField(max_length=12, verbose_name="Contact Person Number", default="0818202023")
    gps_cordinates = models.CharField(verbose_name="GPS Cordinates", max_length=255, default="jdfjfowjr")
    credit_check = models.BooleanField(default=False)

    REQUIRED_FIELDS=['company_name', 'company_type', 'rc_no', 'bank_details', 'bvn', 'utility_bill', 'reference_letter', 'company_address', 'contact_person_name', 'contact_person_name', 'contact_person_number', 'credit_check']

    def __str__(self):
        return self.company.email
