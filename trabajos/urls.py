from django.urls import path
from trabajos import views

urlpatterns = [
    path('<int:pk>/', views.TrabajoDetailView.as_view(), name='trabajo-detail-view'),
    path('crear-trabajo/', views.TrabajoCreateView.as_view(), name='generar-trabajo'),
    path('planilla-trabajos/', views.TrabajoListView.as_view(), name='planilla-trabajos')
]
