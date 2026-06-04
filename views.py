from django.shortcuts import render
from app1.models import Players
# Create your views here.
def home(request):
    name=request.GET.get('name')
    score=request.GET.get('score')
    team=request.GET.get('team')
    birthdate=request.GET.get('birthdate')
    play=Players.objects.all().order_by('runs')
    if name:
        play=Players.object.filter(name__icontains('name'))