from http import HTTPStatus
import uuid

from django.test import TestCase, Client
from django.urls import reverse

from model_bakery import baker
from pprint import pprint

from .models import Product, Country, Ingredient
from .forms import ProductForm


class CountryModelTests(TestCase):

    def setUp(self):
        self.country = baker.make('Country')

    def test_country_fields(self):
        self.assertIsInstance(self.country.id, uuid.UUID)
        self.assertIsInstance(self.country.name, str)
        self.assertIsInstance(self.country.slug, str)
        self.assertIsInstance(self.country.flag_img_name, str)

    def test_builtin_str_method(self):
        self.assertEqual(str(self.country), self.country.name)

    def test_make_flag_image_name(self):
        self.assertEqual(self.country.flag_img_name, f"{'-'.join(self.country.name.split(' ')).lower()}.svg")

    def test_make_name_format(self):
        self.assertEqual(self.country.name, self.country.name.capitalize())


class IngredientModelTests(TestCase):

    def setUp(self):
        self.ingredient = baker.make('Ingredient')
        pprint(self.ingredient.__dict__)

    def test_ingredient_fields(self):
        self.assertIsInstance(self.ingredient.id, uuid.UUID)
        self.assertIsInstance(self.ingredient.name, str)
        self.assertIsInstance(self.ingredient.slug, str)
        self.assertIsInstance(self.ingredient.description, str)
        self.assertEqual(self.ingredient.safety_classification, None)
        self.assertIsInstance(self.ingredient.description, str)
        self.assertFalse(self.ingredient.approved)

    def test_builtin_str_method(self):
        self.assertEqual(str(self.ingredient), self.ingredient.name)


class ProductModelTests(TestCase):
    fixtures = ['fixtures/db_testdata.json']

    def setUp(self):
        self.product = Product.objects.get(name='Alkohol')
        self.ingredient_one = Ingredient.objects.get(name='Tromethamine')
        self.ingredient_two = Ingredient.objects.get(name='Panthenol')
        self.product.ingredients_list.set([self.ingredient_one.pk, self.ingredient_two.pk])

    def test_product_fields(self):
        self.assertIsInstance(self.product.id, uuid.UUID)
        self.assertIsInstance(self.product.brand, str)
        self.assertEqual(self.product.line, None)
        self.assertIsInstance(self.product.name, str)
        self.assertIsInstance(self.product.slug, str)
        self.assertIsInstance(self.product.country.id, uuid.UUID)
        self.assertIsInstance(self.product.img.url, str)
        self.assertIsInstance(self.product.ph, str)
        self.assertIsInstance(self.product.effect_type, list)
        self.assertIsInstance(self.product.skin_type, list)
        self.assertIsInstance(self.product.for_what, list)
        self.assertEqual(self.product.ebay_link, None)
        self.assertEqual(self.product.amazon_link, None)
        self.assertIsInstance(self.product.blog_link, str)
        self.assertEqual(self.product.youtube_link, None)
        self.assertEqual(self.product.facebook_link, None)
        self.assertEqual(self.product.telegram_link, None)
        self.assertEqual(self.product.instagram_link, None)
        self.assertIsInstance(self.product.created_by.id, int)
        self.assertTrue(self.product.approved, True)

    def test_builtin_str_method(self):
        self.assertEqual(str(self.product), f'{self.product.name} -- {self.product.brand}')

    def test_absolute_url(self):
        self.assertEqual(self.product.get_absolute_url(), reverse(
            'app:product_detail',
            kwargs={'slug': self.product.slug}
        ))


class ProductFormTests(TestCase):

    def test_form_valid(self):
        data = {
            'brand': 'Test brand',
            'line': 'Test line',
            'name': 'Test name',
            'ingredients': 'Test one, test two, test three',
        }
        form = ProductForm(data=data)
        self.assertTrue(form.is_valid())

    def test_form_invalid(self):
        form = ProductForm(data={
            'brand': 'Test brand'
        })
        form1 = ProductForm(data={
            'name': 'Test name'
        })
        form2 = ProductForm(data={
            'line': 'Test line'
        })
        self.assertFalse(form.is_valid())
        self.assertFalse(form1.is_valid())
        self.assertFalse(form2.is_valid())


class AppViewsTests(TestCase):
    fixtures = ['fixtures/db_testdata.json']

    def test_main_page_view(self):
        main_page_context = Product.objects.filter(approved=True).order_by('-creation_date')[:9]
        response = self.client.get('/en/')
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(len(response.context['recently_added']), 9)

        for product in main_page_context:
            self.assertIn(
                product,
                response.context['recently_added']
            )

    def test_about_us_view(self):
        response = self.client.get('/en/about-us/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_product_list_view(self):
        response = self.client.get('/en/list/')
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(len(response.context['object_list']), 30)

        response = self.client.get('/en/list/', {'search': 'Product'})
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(len(response.context['object_list']), 30)

        response = self.client.get('/en/list/', {'search': 'solar alkohol news'})
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(len(response.context['object_list']), 1)

        response = self.client.get('/en/list/', {'search': 'corpuscular theory for dummies'})
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(len(response.context['object_list']), 0)

    def test_product_detail_view(self):
        response = self.client.get('/en/list/alkohol/')
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTrue(response.context['object'])
        self.assertEqual(response.context['object'].name, 'Alkohol')
        self.assertEqual(response.context['object'].brand, 'Cordlo by name of this hand')

    def tet_product_create_view_get(self):
        response = self.client.get('/en/create/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def tet_product_create_view_post(self):
        response = self.client.post('/en/create/', {'brand': 'Test brand', 'name': 'Test name'})
        test_obj = Product.objects.get(name='Test name')
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTrue(test_obj)
        self.asserEqual(test_obj.brand, 'Test brand')
        self.asserEqual(test_obj.name, 'Test name')

    def test_success_view(self):
        response = self.client.get('/en/success/')
        self.assertEqual(response.status_code, HTTPStatus.OK)
