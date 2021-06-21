from http import HTTPStatus

from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory, TestCase

from app.models import Product, Country, Ingredient
from .forms import ProductAdminForm
from .views import (
    AdministrationUnapprovedList,
    AdminProductList,
    AdminProductUpdate,
    AdminProductDelete,
    admin_unapproved_list_delete
)


class ProductAdminFormTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='TestName', email='test@email.com', password='Password')

    def test_form_valid(self):
        form = ProductAdminForm(data={
            'brand': 'Test brand',
            'line': 'Test line',
            'name': 'Test name',
            'country': '',
            'img': '',
            'ingredients': 'One, Two, Three',
            'ingredients_list': '',
            'ph': '',
            'effect_type': '',
            'skin_type': '',
            'for_what': '',
            'ebay_link': '',
            'amazon_link': '',
            'blog_link': '',
            'youtube_link': '',
            'facebook_link': '',
            'telegram_link': '',
            'instagram_link': '',
            'approved': True
        })
        self.assertTrue(form.is_valid())

    def test_form_invalid(self):
        form = ProductAdminForm(data={
            'brand': 'Test brand'
        })
        form1 = ProductAdminForm(data={
            'name': 'Test name'
        })
        form2 = ProductAdminForm(data={
            'line': 'Test line'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'name': ['This field is required.']
        })
        self.assertFalse(form1.is_valid())


class AdministrationViewsTests(TestCase):
    fixtures = ['db_testdata.json']

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='TestName', email='test@email.com', password='Password')
        self.slug = 'alkohol'

    def test_administration_unapproved_list_view_with_user(self):
        request = self.factory.get('/en/administration/')
        request.user = self.user
        response = AdministrationUnapprovedList.as_view()(request)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTrue(response.context_data['list_for_approval'])
        self.assertEqual(len(response.context_data['list_for_approval']), 30)
        self.assertTrue(response.context_data['search_form'])

    def test_administration_unapproved_list_view_without_user(self):
        request = self.factory.get('/en/administration/')
        request.user = AnonymousUser()
        response = AdministrationUnapprovedList.as_view()(request)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

    def test_admin_product_list_view_with_user(self):
        request = self.factory.get('/en/administration/list/')
        request.user = self.user
        response = AdminProductList.as_view()(request)
        view = AdminProductList()
        view.setup(request)
        queryset = view.get_queryset()
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTrue(queryset)
        self.assertEqual(len(queryset), len(Product.objects.all()))
        self.assertTrue(response.context_data['search_form'])

    def test_admin_product_list_view_without_user(self):
        request = self.factory.get('/en/administration/list/')
        request.user = AnonymousUser()
        response = AdminProductList.as_view()(request)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

    def test_admin_product_update_view_with_user(self):
        request = self.factory.get(f'/en/administration/{self.slug}/')
        request.user = self.user
        response = AdminProductUpdate.as_view()(request, slug=self.slug)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTrue(response.context_data['object'])
        self.assertEqual(response.context_data['object'].name, 'Alkohol')
        self.assertTrue(response.context_data['search_form'])


    def test_admin_product_update_view_without_user(self):
        request = self.factory.get(f'/en/administration/{self.slug}/')
        request.user = AnonymousUser()
        response = AdminProductUpdate.as_view()(request)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

    def test_admin_product_delete_view_with_user(self):
        request = self.factory.get(f'/en/administration/{self.slug}/delete')
        request.user = self.user
        response = AdminProductDelete.as_view()(request, slug=self.slug)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTrue(response.context_data['object'])
        self.assertEqual(response.context_data['object'].name, 'Alkohol')
        self.assertTrue(response.context_data['search_form'])

    def test_admin_product_delete_view_without_user(self):
        request = self.factory.get(f'/en/administration/{self.slug}/delete')
        request.user = AnonymousUser()
        response = AdminProductDelete.as_view()(request)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

    def test_admin_unapproved_list_delete_view_with_user(self):
        self.client.force_login(self.user)
        response = self.client.get('/en/administration/delete-all')
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTrue(response.context['search_form'])

    def test_admin_unapproved_list_delete_view_without_user(self):
        request = self.factory.get('/en/administration/delete-all')
        request.user = AnonymousUser()
        response = admin_unapproved_list_delete(request)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
