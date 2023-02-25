from django.urls import path
from base import views
from django.views.generic import TemplateView

urlpatterns = [
    path('obra-social/', views.ObraSocialListView.as_view(), name='obra-social-list-view'),
    path('obra-social/crear/', views.ObraSocialCreateView.as_view(), name='obra-social-create-view'),
    path('obra-social/<int:pk>/modificar/', views.ObraSocialUpdateView.as_view(), name='obra-social-update-view'),
    path('obra-social/<int:pk>/borrar/', views.ObraSocialDeleteView.as_view(), name='obra-social-delete-view'),
    path('persona/', views.PersonaListView.as_view(), name='persona-list-view'),
    path('persona/<int:pk>/', views.PersonaDetailView.as_view(), name='persona-detail-view'),
    path('persona/crear/', views.PersonaCreateView.as_view(), name='persona-create-view'),
    path('persona/<int:pk>/modificar/', views.PersonaUpdateView.as_view(), name='persona-update-view'),
    path('persona/<int:pk>/borrar/', views.PersonaDeleteView.as_view(), name='persona-delete-view'),
    path('doctor/', views.DoctorListView.as_view(), name='doctor-list-view'),
    path('doctor/<int:pk>/', views.DoctorDetailView.as_view(), name='doctor-detail-view'),
    path('doctor/crear/', views.DoctorCreateView.as_view(), name='doctor-create-view'),
    path('doctor/<int:pk>/modificar/', views.DoctorUpdateView.as_view(), name='doctor-update-view'),
    path('doctor/<int:pk>/borrar/', views.DoctorDeleteView.as_view(), name='doctor-delete-view'),
    path('lente/', views.LenteListView.as_view(), name='lente-list-view'),
    path('lente/crear/', views.LenteCreateView.as_view(), name='lente-create-view'),
    path('lente/<int:pk>/modificar/', views.LenteUpdateView.as_view(), name='lente-update-view'),
    path('lente/<int:pk>/borrar/', views.LenteDeleteView.as_view(), name='lente-delete-view'),
    path('test', TemplateView.as_view(template_name="test.html")),
]
