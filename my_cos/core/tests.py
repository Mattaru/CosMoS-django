from django.test import RequestFactory, TestCase

from app.models import Product
from .handlers import (
    get_img_upload_path,
    _capitalize_every_word_in_string,
    get_ingredients_names_list_from_string,
    make_list_from_searching_string,
    get_search_data
)


class HandlersTests(TestCase):
    fixtures = ['fixtures/db_testdata.json']

    def setUp(self):
        self.factory = RequestFactory()
        self.product = Product.objects.get(name='Alkohol')
        self.test_str = 'test, sTring For caPItalize, eVeRY worD'

    def test_get_img_upload_path(self):
        result = get_img_upload_path(self.product, 'Test_img_name.png')
        self.assertIsInstance(result, str)
        self.assertEqual(result, f'product-images/{self.product.name}/Test_img_name.png')

    def test_capitalize_every_word_in_string(self):
        result = _capitalize_every_word_in_string(self.test_str)
        self.assertEqual(result, 'Test, String For Capitalize, Every Word')

    def test_get_ingredients_names_list_from_string(self):
        result = get_ingredients_names_list_from_string(self.test_str)
        self.assertIsInstance(result, list)
        self.assertEqual(result, ['Test', 'String For Capitalize', 'Every Word'])

    def test_make_list_from_searching_string(self):
        result = make_list_from_searching_string(self.test_str)
        self.assertIsInstance(result, list)
        self.assertEqual(
            result,
            [
                'test, sTring For caPItalize, eVeRY worD',
                'test,',
                'sTring',
                'For',
                'caPItalize,',
                'eVeRY',
                'worD'
            ]
        )

    def test_get_search_data(self):
        request = self.factory.get('/', {'search': 'Test search data'})
        result = get_search_data(request)
        self.assertIsInstance(result, str)
        self.assertEqual(result, 'Test search data')