from xml.etree.ElementTree import C14NWriterTarget
import phonenumbers
from rest_framework import serializers
from .models import Person, User


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

class CompanySerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(required=True)
    company_type = serializers.CharField(required=True)
    rc_no = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ['company_name', 'company_type', 'rc_no', 'email']

    def create(self, validated_data):
        user = User.objects.create_user(email=validated_data['email'], password=validated_data['password'])