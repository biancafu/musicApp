from django.shortcuts import render
from django.http import HttpResponse

# render views, api end points (end point = / (paths?))
def main(request): #request parameter is required when making view
    #this will return a response (from end point)
    return HttpResponse("Hello")
