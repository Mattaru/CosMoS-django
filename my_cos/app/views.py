from django.shortcuts import get_list_or_404, render
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy

from app.models import Product, Country
from app.forms import CountryForm, OneRowSearch, ProductForm
from .handlers_service import make_list_from_searching_string,\
    get_queryset_with_filtered_data_for_search


class MainPageView(TemplateView):
    """Show the ordered queryset by 'creation_date', and show a last four of it."""
    template_name = 'main_page.html'
    extra_context = {
        'search_form': OneRowSearch(),
        'last_four_added': Product.objects.filter(approved=True).order_by('-creation_date')[:4]
    }


class AboutUsView(TemplateView):
    """The resource description view."""
    template_name = 'about_us.html'
    extra_context = {
        'search_form': OneRowSearch()
    }


class ProductList(ListView):
    """The product list view, where value of the 'Approved' field equal True,
    and required field contains 'search' parameters."""
    model = Product
    paginate_by = 30
    template_name = 'products/product_list.html'
    extra_context = {
        'search_form': OneRowSearch()
    }

    def get_queryset(self):
        queryset = []
        params = self.request.GET.dict()

        if params.get('search'):
            data = params.get('search')
            queryset = Product.objects.filter(approved=True)
            data_list = make_list_from_searching_string(string=data)
            qs = get_queryset_with_filtered_data_for_search(
                queryset=queryset,
                search_list=data_list
            )
            if qs:
                return qs

        return queryset


class ProductDetail(DetailView):
    """A product detail view."""
    model = Product
    template_name = 'products/product_detail.html'
    extra_context = {
        'search_form': OneRowSearch()
    }

    def get_queryset(self):
        qs = super(ProductDetail, self).get_queryset()
        qs = qs.prefetch_related('ingredients_list')

        return qs


class ProductCreate(CreateView):
    """A product creation view."""
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('app:success')
    template_name = 'products/product_create.html'
    extra_context = {
        'search_form': OneRowSearch()
    }


class SuccessView(TemplateView):
    """Creation success view."""
    template_name = 'success.html'
    extra_context = {
        'search_form': OneRowSearch()
    }
