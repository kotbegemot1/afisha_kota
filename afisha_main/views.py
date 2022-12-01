from django.shortcuts import render, HttpResponse

from .models import Event, Place

# Create your views here.

def index(request):
    ev_list = Event.objects.all()
    return render(request, 'afisha_main/index.html', context={'ev_list': ev_list})