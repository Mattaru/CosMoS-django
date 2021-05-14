from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy

from app.models import Product, Country
from app.forms import OneRowSearch, ProductForm
from core.handlers import make_list_from_searching_string,\
    get_queryset_with_filtered_data_for_search,\
    get_search_data


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
        approved_products = super(ProductList, self).get_queryset()\
            .filter(approved=True)
        search_data = get_search_data(self.request)
        qs = []

        if search_data:
            search_list = make_list_from_searching_string(string=search_data)
            qs = get_queryset_with_filtered_data_for_search(
                queryset=approved_products,
                search_list=search_list
            )

            if qs:
                return qs

        return qs


class ProductDetail(DetailView):
    """A product detail view."""
    model = Product
    template_name = 'products/product_detail.html'
    extra_context = {
        'search_form': OneRowSearch()
    }

    def get_queryset(self):
        qs = super(ProductDetail, self).get_queryset()\
            .prefetch_related('ingredients_list')

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
