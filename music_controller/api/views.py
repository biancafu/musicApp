from django.shortcuts import render
from rest_framework import generics
from .serializers import RoomSerializer
from .models import Room

# render views, api end points (end point = / (paths?))

class RoomView(generics.CreateAPIView):  #CreateAPIView (post), ListAPIView (get)
    queryset = Room.objects.all()  #what we want to return
    serializer_class = RoomSerializer #how to convert the data to a format to user them
