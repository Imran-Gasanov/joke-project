from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Joke


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class JokeSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Joke
        fields = ['url', 'user', 'content']
