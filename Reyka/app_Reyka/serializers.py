from rest_framework import serializers
from .models import User

class UserSeriaLizer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','email']
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

print(User.objects.all())
