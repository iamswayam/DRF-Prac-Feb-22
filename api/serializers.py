from rest_framework import serializers
from secureApp.models import Software, SecureHub


class SecureSerializer(serializers.Serializer):
    class Meta:
        model = SecureHub
        fields = "__all__"
