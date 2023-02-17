from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from trabajos.models import Trabajo

# CRUD - TRABAJOS
class TrabajoListView(ListView):
    model = Trabajo
    template_name = "trabajo_list.html"


class TrabajoDetailView(DetailView):
    model = Trabajo
    template_name = "trabajo_detail.html"
    context_object_name = 'trabajo'


class TrabajoCreateView(CreateView):
    model = Trabajo
    fields = '__all__'
    template_name = 'trabajo_create_form.html'
    

class TrabajoUpdateView(UpdateView):
    model = Trabajo
    fields = '__all__'
    template_name = "trabajo_update_form.html"


class TrabajoDeleteView(DeleteView):
    model = Trabajo
    template_name = "trabajo_confirm_delete.html"
    success_url = reverse_lazy('trabajo-list-view')