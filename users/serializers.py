import phonenumbers
from rest_framework import serializers
from .models import Person, PersonMore

class PersonRegisterSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True,) #by default allow_null = False
    full_name = serializers.CharField(required=True)
    phonenumbers = serializers.CharField(required=True)

    def get_cleaned_data(self):
            data = super(PersonRegisterSerializer, self).get_cleaned_data()
            extra_data = {
                'full_name' : self.validated_data.get('full_name', ''),
                'phone_number' : self.validated_data.get('phone_number', ''),
            }
            data.update(extra_data)
            return data

    def save(self, request):
        user = super(PersonRegisterSerializer, self).save(request)
        user.is_seller = True
        user.save()
        seller = Person(seller=user, area=self.cleaned_data.get('area'), 
                address=self.cleaned_data.get('address'),
                description=self.cleaned_data.get('description'))
        seller.save()
        return user