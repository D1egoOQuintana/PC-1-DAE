from django.test import TestCase
from .models import Contacto

class ContactoModelTest(TestCase):

    def setUp(self):
        self.contacto = Contacto.objects.create(
            nombre='Juan Pérez',
            email='juan@example.com',
            telefono='123456789',
            direccion='Calle Falsa 123'
        )

    def test_contacto_creation(self):
        self.assertEqual(self.contacto.nombre, 'Juan Pérez')
        self.assertEqual(self.contacto.email, 'juan@example.com')
        self.assertEqual(self.contacto.telefono, '123456789')
        self.assertEqual(self.contacto.direccion, 'Calle Falsa 123')

    def test_contacto_str(self):
        self.assertEqual(str(self.contacto), 'Juan Pérez')  # Asegúrate de que el método __str__ esté definido en el modelo

    def test_contacto_creado(self):
        self.assertIsNotNone(self.contacto.creado)  # Verifica que el campo creado no sea None

    def test_contacto_email_validation(self):
        with self.assertRaises(ValueError):
            Contacto.objects.create(nombre='Error', email='noesunemail', telefono='123', direccion='Calle Error')  # Verifica que se lance un error al crear un contacto con email inválido