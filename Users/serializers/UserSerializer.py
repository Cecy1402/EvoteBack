from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
User = get_user_model()


class UserSerializer(serializers.ModelSerializer):


    class Meta:
        model = User
        fields = ('__all__')


class UserLoginSerializer(serializers.Serializer):

    username = serializers.CharField()
    password = serializers.CharField(min_length=8, max_length=64)

    def validate(self, data):
        '''Check credentials.'''
        user = authenticate(
            username=data['username'], password=data['password'])

        if user is not None:
            self.context['user'] = user
            return data
        else:
            raise serializers.ValidationError('Invalid credentials')

        

    def create(self, data):
        '''Generate or retrieve new token.'''
        token, created = Token.objects.get_or_create(user=self.context['user'])
        return self.context['user'], token.key

    def update(self, instance, validated_data):

        return instance
