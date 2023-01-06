from django.shortcuts import render
from django.http import HttpResponse
from .models import Persona

def index(request):
    personas = Persona.objects.all()
    print(personas)
    html = render(request, 'personas.html', {
        'personas':personas
    })
    return HttpResponse(html)


    
