from rest_framework import serializers
from django.shortcuts import get_object_or_404
from .models import User
from PetitionWebapp.settings import AUTH_PASSWORD_VALIDATORS


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'password',
            'email',
            'first_name',
            'last_name'
        )
        extra_kwargs = {
            'password' : {'write_only':True},
            'id' : {'read_only':True},
            'username' : {'required':True},
            'email' : {'required':True},
            'first_name' : {'required':True},
            'last_name' : {'required':True}
        }

    def create(self, validated_data):
        user = User_Model.objects.create_user(
            username = validated_data['username'],
            email = validated_data['email'],
            password = validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        return user


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True, max_length=30)
    new_password1 = serializers.CharField(
        required=True,
        max_length=30,
        validators = AUTH_PASSWORD_VALIDATORS
        )
    new_password2 = serializers.CharField(required=True, max_length=30)

    def validate(self, data):
        user = self.context['request'].user
        if not user.check_password(data.get('old_password')):
            raise serializers.ValidationError(('Old password was entered incorrectly'))
        if data['new_password1']!=data['new_password2']:
            raise serializers.ValidationError("Passwords are not the same")
        if data['old_password']==data['new_password1']:
            raise serializers.ValidationError("New password cannot be the same as current password")
        return data
    

class SendregisterEmailSerializer(serializers.Serializer):
    model = User
    email = serializers.EmailField(required=True)
    username=serializers.CharField(required=True)

    def validate(self,data):
        if (User_Model.objects.filter(email=data['email'])):
            raise serializers.ValidationError("There is another account with this email")
        if (User_Model.objects.filter(username=data['username'])):
            raise serializers.ValidationError("There is another account with this username")
        return data


class SendpasswordresetEmailSerializer(serializers.Serializer):
    model = User
    email = serializers.EmailField(required=True)

    def validate(self,data):
        if not User_Model.objects.filter(email=data['email']):
            raise serializers.ValidationError("Email Does Not Exist")
        return data


class ResetPasswordSerializer(serializers.Serializer):
    model = User
    new_password1 = serializers.CharField(
        required=True,
        max_length=30,
        validators = AUTH_PASSWORD_VALIDATORS
        )
    new_password2 = serializers.CharField(required=True)
    email=serializers.EmailField(required=True)
    def validate(self,data):
        if data['new_password1']!=data['new_password2']:
            raise serializers.ValidationError("Passwords are not the same")
        if not User_Model.objects.filter(email=data['email']):
            raise serializers.ValidationError("Email Does Not Exist")
        if get_object_or_404(User_Model, email=data['email']).check_password(data['new_password1']):
            raise serializers.ValidationError("New password cannot be the same as current password")
        return data


class PrivateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'gender',
            'birthdate',
            'profile_image',
            'email',
            'phone_number'
        ]

    def validate(self, data):
        birthdate = data.get('birthdate')
        if birthdate != None:
            today = datetime.date.today()
            age = (today - birthdate).days / 365
            if age < 18:
                raise serializers.ValidationError('You must be at least 18 years old')
        return data


class PublicProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'gender',
            'profile_image'
        ]
