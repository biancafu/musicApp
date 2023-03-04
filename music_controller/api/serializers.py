# take model (python code) and translate this room into json response

from rest_framework import serializers
from .models import Room

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room    #models that we want to serialize
        fields = ('id', 'code', 'host', 'guest_can_pause', 'votes_to_skip', 'created_at')  #fields we want to include for serialization