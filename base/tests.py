from django.test import TestCase
from django.urls import reverse

from base.models import ObraSocial

class ObraSocialListViewTests(TestCase):
    def test_listar_obras_sociales(self):
        """La List View de Obra Sociales muestra las obras sociales cargadas"""
        nombre_os = 'IAPOS'
        os = ObraSocial(nombre_os)
        os.save()
        response = self.client.get(reverse('base:obra-social-list-view'))
        print(response.status_code)
        print(response.context)
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['obra_social_list'],[os])
