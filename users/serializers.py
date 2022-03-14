from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


class RegisterUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        max_length=255,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    name = serializers.CharField(max_length=100)
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )
    token = serializers.CharField(max_length=255, read_only=True)
    
    class Meta:
        model = User
        fields = '__all__'
        
    def create(self, validated_data):
        return User.objects.create_user(
            **validated_data
        )
        
        
