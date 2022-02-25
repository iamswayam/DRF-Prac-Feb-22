from rest_framework import serializers
from secureApp.models import Software, SecureHub
from django.contrib.auth.models import User


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):

        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError(
                {'error': 'P1 & P2 should be the same!'})

        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError(
                {'error': 'Email already exists'})

        account = User(
            email=self.validated_data['email'], username=self.validated_data['username'])
        account.set_password(password)
        account.save()

        return account


class SecureSerializer(serializers.ModelSerializer):
    handledBy = serializers.StringRelatedField(read_only=True)
    linkedSoft = serializers.CharField(source='linkedSoft.name')

    class Meta:
        model = SecureHub
        fields = "__all__"


class SoftwareSerializer(serializers.ModelSerializer):
    devlopedBy = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Software
        fields = "__all__"
