from django.db.models import Q
from django.shortcuts import get_list_or_404, render
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy

from app.models import Product, Country, Brand
from app.forms import BrandForm, CountryForm, OneRowSearch, ProductForm


class AboutUsView(TemplateView):
    template_name = 'about_us.html'


class BrandCreate(CreateView):
    model = Brand
    form_class = BrandForm
    template_name = 'brands/brand_create.html'
    success_url = reverse_lazy('app:product_create')


class CountryCreate(CreateView):
    model = Country
    form_class = CountryForm
    template_name = 'countries/country_create.html'
    success_url = reverse_lazy('app:brand_create')


class ProductList(ListView):
    model = Product
    template_name = 'products/product_list.html'

    def get_context_data(self, **kwargs):
        context = super(ProductList, self).get_context_data(**kwargs)
        context['search_form'] = OneRowSearch()

        return context

    def get_queryset(self):
        queryset = []
        params = self.request.GET.dict()

        if params.get('search'):
            data = params.get('search')
            queryset = Product.objects.filter(approved=True)
            queryset = queryset.filter(
                Q(name__icontains=data)
                | Q(line__icontains=data)
                | Q(brand__name__icontains=data)
            )

        return queryset


class ProductDetail(DetailView):
    model = Product
    template_name = 'products/product_detail.html'


class ProductCreate(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_create.html'
    success_url = reverse_lazy('app:success')








class SuccessView(TemplateView):
    template_name = 'success.html'