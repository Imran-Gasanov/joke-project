from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import UserSerializer, JokeSerializer
from . import models
from rest_framework.response import Response
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.views import APIView
import requests
import json


class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = UserSerializer


class JokeViewSet(viewsets.ModelViewSet):
    queryset = models.Joke.objects.all()
    serializer_class = JokeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request):
        serializer = JokeSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)  # check all fields is valid before attempting to save
        serializer.save(user=request.user)
        return Response(serializer.data)


class GenerateJokeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        res = requests.get("https://v2.jokeapi.dev/joke/Programming?type=single")
        data = json.loads(res.text)
        joke = data["joke"]
        models.Joke.objects.create(content=joke, user=request.user)
        return Response(joke)



