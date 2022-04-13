import phonenumbers
from rest_framework import serializers
from .models import Person, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['email', 'password']

class PersonSignUpSerializer(serializers.ModelSerializer):
    person = UserSerializer()
    full_name = serializers.CharField(required=True)
    phone_number = serializers.CharField(required=True)

    class Meta:
        model = Person
        fields = ['person', 'full_name', 'phone_number']

    def create(self, validated_data):
        person_data = validated_data.pop('person')
        user = User.objects.create(**self.validated_data.get('person'))
        Person.objects.create(person=data, **self.validated_data)
        return user

class PersonRegisterSerializer(serializers.Serializer):
    person = serializers.PrimaryKeyRelatedField(read_only=True,)
    email = serializers.EmailField(required=User.USERNAME_FIELD)
    full_name = serializers.CharField(required=True)
    phone_number = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True)

    def get_cleaned_data(self):
            data = {
                'password': self.validated_data.get('password', ''),
                'email': self.validated_data.get('email', ''),
                'full_name' : self.validated_data.get('full_name', ''),
                'phone_number' : self.validated_data.get('address', ''),
            }
            return data


    def save(self):
        print(self.validated_data)
        self.cleaned_data = self.get_cleaned_data
        user = UserSerializer(data={'email': self.validated_data['email'],
                                'password': self.validated_data['password']})
        print(user)
        user.is_valid(raise_exception=True)
        user.is_person = True
        user.save()
        print(user)
        person = Person(person=user, full_name=self.cleaned_data.get('full_name'), 
                phone_number=self.cleaned_data.get('phone_number'),
                )
        person.save()
        return user