from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .serializers import *
from events.models import *


class CountryCreateApi(generics.CreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class EventsApi(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class AthleteUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Athlete.objects.all()
    serializer_class = AthleteSerializer

class CommentDeleteApi(generics.DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
