from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import ObraSocial, Persona, Doctor, Lente

# CRUD - OBRAS SOCIALES
class ObraSocialListView(ListView):
    model = ObraSocial
    template_name = "obra_social_list.html"


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


# CRUD - PERSONAS
class PersonaListView(ListView):
    model = Persona
    template_name = "persona_list.html"


class PersonaDetailView(DetailView):
    model = Persona
    template_name = "persona_detail.html"
    context_object_name = 'persona'


class PersonaCreateView(CreateView):
    model = Persona
    fields = '__all__'
    template_name = 'persona_create_form.html'
    

class PersonaUpdateView(UpdateView):
    model = Persona
    fields = '__all__'
    template_name = "persona_update_form.html"


class PersonaDeleteView(DeleteView):
    model = Persona
    template_name = "persona_confirm_delete.html"
    success_url = reverse_lazy('persona-list-view')


# CRUD - DOCTORES
class DoctorListView(ListView):
    model = Doctor
    template_name = "doctor_list.html"


class DoctorDetailView(DetailView):
    model = Doctor
    template_name = "doctor_detail.html"
    context_object_name = 'doctor'


class DoctorCreateView(CreateView):
    model = Doctor
    fields = '__all__'
    template_name = 'doctor_create_form.html'
    

class DoctorUpdateView(UpdateView):
    model = Doctor
    fields = '__all__'
    template_name = "doctor_update_form.html"


class DoctorDeleteView(DeleteView):
    model = Doctor
    template_name = "doctor_confirm_delete.html"
    success_url = reverse_lazy('doctor-list-view')


# CRUD - LENTES
class LenteListView(ListView):
    model = Lente
    template_name = "lente_list.html"


class LenteCreateView(CreateView):
    model = Lente
    fields = '__all__'
    template_name = 'lente_create_form.html'
    success_url = reverse_lazy('lente-list-view')
    

class LenteUpdateView(UpdateView):
    model = Lente
    fields = '__all__'
    template_name = "lente_update_form.html"
    success_url = reverse_lazy('lente-list-view')


class LenteDeleteView(DeleteView):
    model = Lente
    template_name = "lente_confirm_delete.html"
    success_url = reverse_lazy('lente-list-view')

