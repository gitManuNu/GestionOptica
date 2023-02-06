from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from .models import *

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


class ObraSocialListView(ListView):
    model = ObraSocial
    template_name = "obra_social_list.html"


class ObraSocialDetailView(DetailView):
    model = ObraSocial
    template_name = "obra_social_detail.html"
    context_object_name = 'obra_social'


class ObraSocialCreateView(CreateView):
    model = ObraSocial
    fields = '__all__'
    template_name = 'obra_social_create_form.html'
    success_url = reverse_lazy('obra-social-list-view')
    

class ObraSocialUpdateView(UpdateView):
    model = ObraSocial
    fields = '__all__'
    template_name = "obra_social_update_form.html"
    success_url = reverse_lazy('obra-social-list-view')


class ObraSocialDeleteView(DeleteView):
    model = ObraSocial
    template_name = "obra_social_confirm_delete.html"
    success_url = reverse_lazy('obra-social-list-view')



