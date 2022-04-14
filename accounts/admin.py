from django.contrib import admin
from .models import User, Person, Company

#Register your models here.
admin.register(User)
admin.register(Person)
admin.register(Company)