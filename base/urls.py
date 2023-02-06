from django.urls import path
from base import views

urlpatterns = [
    path('', views.index, name='index'),
    path('alta_personas/', views.alta_personas, name='alta_personas'),
    path('obra-social/', views.ObraSocialListView.as_view(), name='obra-social-list-view'),
    path('obra-social/<int:pk>/', views.ObraSocialDetailView.as_view(), name='obra-social-detail-view'),
    path('obra-social/crear/', views.ObraSocialCreateView.as_view(), name='obra-social-create-view'),
    path('obra-social/<int:pk>/modificar/', views.ObraSocialUpdateView.as_view(), name='obra-social-update-view'),
    path('obra-social/<int:pk>/borrar/', views.ObraSocialDeleteView.as_view(), name='obra-social-delete-view'),
]
