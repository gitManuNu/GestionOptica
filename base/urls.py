from django.urls import path
from base import views

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
]
