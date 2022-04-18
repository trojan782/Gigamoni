from xml.etree.ElementTree import C14NWriterTarget
import phonenumbers
from pkg_resources import require
from rest_framework import serializers
from .models import Person, Company, User


class PersonSignUpSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(required=True)
    phone_number = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ['email', 'full_name', 'phone_number', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(email=validated_data['email'], password=validated_data['password'])
        user.is_person=True
        user.save()

        person = Person.objects.create(person=user)
        person.full_name = self.validated_data.get('full_name')
        person.phone_number = self.validated_data.get('phone_number')
        person.save()
        return user

class CompanyStage1Serializer(serializers.ModelSerializer):
    company_name = serializers.CharField(required=True)
    company_type = serializers.CharField(required=True)
    rc_no = serializers.CharField(required=True)
    

    class Meta:
        model = User
        fields = ['email', 'company_name', 'company_type', 'rc_no', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(email=validated_data['email'], password=validated_data['password'])
        user.is_company = True
        user.save()

        company = Company.objects.create(company=user)
        company.company_name = self.validated_data.get('company_name')
        company.company_type = self.validated_data.get('company_type')
        company.rc_no = self.validated_data.get('rc_no')
        company.save()
        return company
    
    

class CompanyStage2Serializer(serializers.ModelSerializer):
    utility_bill = serializers.FileField(required=True)
    class Meta:
        model = Company
        fields = ['company_address', 'utility_bill', 'gps_cordinates']

    def update(self, instance, validated_data):
        company = Company.objects.get(pk=instance.id)
        Company.objects.filter(pk=instance.id).update(**validated_data)
        return company
        
class CompanyStage3Serializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['reference_letter', 'contact_person_name', 'contact_person_email', 'contact_person_number', 'bank_details', 'bvn', 'credit_check']

    def update(self, instance, validated_data):
        company = Company.objects.get(pk=instance.id)
        Company.objects.filter(pk=instance.id).update(**validated_data)
        return company