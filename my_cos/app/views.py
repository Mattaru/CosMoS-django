from django.db.models import Q
from django.shortcuts import get_list_or_404, render
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy

from app.models import Product, Country
from app.forms import CountryForm, OneRowSearch, ProductForm


TEXT = 'Just a new ingredient, very nice day, simple program, one, 1.2 prices'


def create_objects(name, number):
    for num in range(number):
        product = Product(
            brand='MISSHA',
            name=f'{name}{num}',
            ingredients=TEXT
        )
        product.save()


class MainPageView(TemplateView):
    """
        Show the ordered queryset by 'creation_date', and show a last four of it.
    """
    template_name = 'main_page.html'

    def get_context_data(self, **kwargs):
        context = super(MainPageView, self).get_context_data(**kwargs)
        context['search_form'] = OneRowSearch()
        context['last_four_added'] = Product.objects.filter(approved=True).order_by('-creation_date')[:4]

        return context


class AboutUsView(TemplateView):
    """
        The resource description view.
    """
    template_name = 'about_us.html'

    def get_context_data(self, **kwargs):
        context = super(AboutUsView, self).get_context_data(**kwargs)
        context['search_form'] = OneRowSearch()

        return context


class ProductList(ListView):
    """
        The product list view, where value of the 'Approved' field equal True,
        and required field contains 'search' parameters.
    """
    model = Product
    paginate_by = 30
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
            data_list = data.split(' ')
            data_list.insert(0, data)

            for data in data_list:
                qs = queryset.filter(
                    Q(name__icontains=data)
                    | Q(line__icontains=data)
                    | Q(brand__icontains=data)
                ).order_by('name')
                if qs:
                    return qs

        return queryset


class ProductDetail(DetailView):
    """
        A product detail view.
    """
    model = Product
    template_name = 'products/product_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDetail, self).get_context_data(**kwargs)
        context['search_form'] = OneRowSearch()

        return context


class ProductCreate(CreateView):
    """
        A product creation view.
    """
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('app:success')
    template_name = 'products/product_create.html'

    def get_context_data(self, **kwargs):
        context = super(ProductCreate, self).get_context_data(**kwargs)
        context['search_form'] = OneRowSearch()

        return context


class SuccessView(TemplateView):
    """
        Creation success view.
    """
    template_name = 'success.html'

    def get_context_data(self, **kwargs):
        context = super(SuccessView, self).get_context_data(**kwargs)
        context['search_form'] = OneRowSearch()

        return context
