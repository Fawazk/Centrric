from dataclasses import fields
from wsgiref import validate
from rest_framework import serializers
from .models import Account,UserFollow

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"
    
    def validate_password(self,value):
        if len(value)<4:
            raise serializers.ValidationError("Password must be minimum 4 characters")
        else:
            return value
    def save(self):
        reg = Account(
            email=self.validated_data['email'],
            full_name=self.validated_data['full_name'],
            phone_number = self.validated_data['phone_number'],
            place=self.validated_data['place'],
            date_of_birth=self.validated_data['date_of_birth']
        )
        password=self.validated_data['password']
        reg.set_password(password)
        reg.save()
        return reg


class UserFollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFollow
        fields = "__all__"

class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ["full_name","email","phone_number","place","date_of_birth",]
