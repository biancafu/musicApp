from django.shortcuts import render
from rest_framework import generics
from .serializers import RoomSerializer
from .models import Room

#render views, api end points (end point = / (paths?))
#with react, we will fetch a request and this will return the json data
#CreateAPIView (post request), ListAPIView (get request)

#api views to view all the rooms in database
#this allows us to view and create room
#generics.CreateAPIView is a view that is set up already to return to us all the stuff we want to return (queryset) and the translator (serializer)
class RoomView(generics.CreateAPIView):  #CreateAPIView (post), ListAPIView (get)
    queryset = Room.objects.all()  #what we want to return
    serializer_class = RoomSerializer #how to convert the data to a format to user them 
