from rest_framework import serializers
from users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone_number', 'age', 'created_at']
        read_only_fields = ['id', 'created_at']

def validate_phone_number(value):
    if not value.startswith('+996') or len(value) != 13:
        raise serializers.ValidationError("Номер должен начинаться с +996 и содержать 13 символов.")
    return value
