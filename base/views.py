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

def alta_personas(request):
    if request.method == 'GET':
        html = render(request, 'form_personas.html')
    else:
        nombre = request.POST['nombre']
        print(nombre)
        html = render(request, 'personas.html')
    return HttpResponse(html)