from django.urls import path
from .views import RoomView
urlpatterns = [
    path('home', RoomView.as_view()), #use RoomView.as_view() is saying take the class and give me the view for it
]
