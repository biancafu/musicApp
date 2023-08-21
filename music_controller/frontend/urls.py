from django.urls import path
from .views import index

urlpatterns = [
    path('', index) #this would be use by users #send whichever urls with / to frontend
]