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
        company.company_name = self.validated_data.get('full_name')
        company.company_type = self.validated_data.get('company_type')
        company.rc_no = self.validated_data.get('rc_no')
        company.save()
        return company
    
    

class CompanyStage2Serializer(serializers.ModelSerializer):
    company_address = serializers.CharField(required=True)
    utility_bill = serializers.FileField(required=True)
    gps_cordinates = serializers.CharField(required=True)

    class Meta:
        model = Company
        fields = ['company_address', 'utility_bill', 'gps_cordinates']

    def create(self, company=None):
        company['company_address'] = self.validated_data.get('company_address')
        company['utility_bill'] = self.validated_data.get('utility_bill')
        company['gps_cordinates'] = self.validated_data.get('gps_cordinates')
        company.save()
        return company
        
class CompanyStage3Serializer(serializers.ModelSerializer):
    reference_letter = serializers.FileField(required=True)
    contact_person_name = serializers.CharField(required=True)
    contact_person_email = serializers.EmailField(required=True)
    contact_person_number = serializers.CharField(required=True)
    bank_details = serializers.CharField(required=True)
    bvn = serializers.CharField(required=True)
    credit_check = serializers.BooleanField(required=True)


    class Meta:
        model = Company
        fields = ['reference_letter', 'contact_person_name', 'contact_person_email', 'contact_person_number', 'bank_details', 'bvn', 'credit_check']

    def create(self, company=None):
        company['reference_letter'] = self.validated_data.get('reference_letter')
        company['contact_person_name'] = self.validated_data.get('contact_person_name')
        company['contact_person_email'] = self.validated_data.get('contact_person_email')
        company['contact_person_number'] = self.validated_data.get('contact_person_number')
        company['bank_details'] = self.validated_data.get('bank_details')
        company['bvn'] = self.validated_data.get('bvn')
        company['credit_check'] = self.validated_data.get('credit_check')
        print(company)
        return company