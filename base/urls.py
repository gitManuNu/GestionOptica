from django.urls import path
from base.views import index, alta_personas

urlpatterns = [
    path('', index, name='index'),
    path('alta_personas/', alta_personas, name='alta_personas'),
]
