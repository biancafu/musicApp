from django.urls import path
from .views import main
urlpatterns = [
    path('home', main) #if we get url = '', call main (from views)
]
