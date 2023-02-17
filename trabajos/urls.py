from django.urls import path
from trabajos import views

urlpatterns = [
    path('trabajo/<int:pk>/', views.TrabajoDetailView.as_view(), name='trabajo-detail-view'),
]
