from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, Client
from django.utils import translation

from .models import Country, Product, Ingredient

User = get_user_model()


class AppTests(TestCase):
    fixtures = ['db_testdata.json']

    def test_main_page_view(self):
        main_page_context = Product.objects.filter(approved=True).order_by('-creation_date')[:9]
        response = self.client.get('/en/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['recently_added']), 9)

        for product in main_page_context:
            self.assertIn(
                product,
                response.context['recently_added']
            )

    def test_about_us_view(self):
        response = self.client.get('/en/about-us/')
        self.assertEqual(response.status_code, 200)

    def test_product_list_view(self):
        response = self.client.get('/en/list/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['object_list']), 30)

        response = self.client.get('/en/list/', {'search': 'Product'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['object_list']), 30)

        response = self.client.get('/en/list/', {'search': 'solar alkohol news'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['object_list']), 1)

        response = self.client.get('/en/list/', {'search': 'corpuscular theory for dummies'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['object_list']), 0)

