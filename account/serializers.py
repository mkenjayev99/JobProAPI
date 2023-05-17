from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from .models import Account, WorkHistory


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'email', 'first_name', 'last_name', 'image', 'role', 'bio', 'location']


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6, max_length=68, write_only=True)
    password2 = serializers.CharField(min_length=6, max_length=68, write_only=True)

    class Meta:
        model = Account
        fields = ('email', 'role', 'password', 'password2')
        extra_kwargs = {
            "role": {'read_only': True}
        }

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')

        if password != password2:
            raise serializers.ValidationError({'success': False, 'message': 'Password did not match, please try again!'})
        return attrs

    def create(self, validated_data):
        del validated_data['password2']
        return Account.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(max_length=68, write_only=True)
    tokens = serializers.SerializerMethodField(read_only=True)

    def get_tokens(self, obj):
        email = obj.get('email')
        tokens = Account.objects.get(email=email).tokens
        return tokens

    class Meta:
        model = Account
        fields = ('email', 'password', 'tokens')

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        user = authenticate(email=email, password=password)
        if not user:
            raise AuthenticationFailed({
                'message': 'Email or password is not correct'
            })
        if not user.is_active:
            raise AuthenticationFailed({
                'message': 'Account disabled'
            })

        return attrs


class WorkHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkHistory
        fields = ['id', 'account', 'company', 'location', 'start_date', 'end_date', 'is_current']
