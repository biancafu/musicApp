from django.shortcuts import render

#render index template and let react take care of it
def index(request, *args, **kwargs):
    return render(request, 'frontend/index.html') #render index template
    #render will take request, take the template, return html to where ever we send the request