from django.db import models
import string
import random

# put most logic/stuff on models, and less on views
# database models
# when we change model or database, run python3 ./manage.py makemigrations
# we need to run this command to start up the database as well

def generate_unique_code():
    length = 6

    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length)) #using join cuz random.choices returns an array 
        if Room.objects.filter(code = code).count() == 0: #Room.objects gives all Room objects
            break

    return code

class Room(models.Model):
    code = models.CharField(max_length = 8, default = "", unique = True) #each room has unique name
    host = models.CharField(max_length=50, unique=True) #one host has one room only
    guest_can_pause = models.BooleanField(null=False, default=False) #permission for guest to pause music (null=False means must pass a value)
    votes_to_skip = models.IntegerField(null=False, default=1)
    created_at = models.DateTimeField(auto_now_add=True) #when create a new room, automatic add the time in

    #can add methods in class too