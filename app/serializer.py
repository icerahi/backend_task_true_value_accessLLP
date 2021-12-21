from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields='__all__'
        
    # def update(self, instance, validated_data):
    #     # Update the Foo instance
    #     instance.first_name = validated_data['first_name']
    #     instance.last_name = validated_data['last_name']
    #     instance.age = validated_data['age']
    #     instance.save()
    #     return instance
    
    
