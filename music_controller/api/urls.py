from django.urls import path
from .views import main
urlpatterns = [
    path('', main) #if we get url = '', call main (from views)
]
