from rest_framework import serializers
from .models import GigaUser

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = GigaUser
        fields = ('email', 'full_name', 'phone_number', 'password')
        extra_kwargs = {'password': {'write_only': True}}
        password = serializers.CharField(max_length=128, write_only=True, required=True)

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance