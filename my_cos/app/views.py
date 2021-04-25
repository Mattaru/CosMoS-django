from django.db.models import Q
from django.shortcuts import get_list_or_404, render
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy

from app.models import Product, Country, Brand
from app.forms import BrandForm, CountryForm, OneRowSearch, ProductForm


TEXT = 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit.' \
       ' Aenean commodo ligula eget dolor.' \
       ' Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes,' \
       ' nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu,' \
       ' pretium quis, sem. Nulla consequat massa quis enim.' \
       ' Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu.' \
       ' In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo.' \
       ' Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus.' \
       ' Vivamus elementum semper nisi. Aenean vulputate eleifend tellus.' \
       ' Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim.' \
       ' Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus.' \
       ' Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum.' \
       ' Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi.' \
       ' Nam eget dui. Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus,' \
       ' sem quam semper libero, sit amet adipiscing sem neque sed ipsum.' \
       ' Nam quam nunc, blandit vel, luctus pulvinar, hendrerit id, lorem.' \
       ' Maecenas nec odio et ante tincidunt tempus.' \
       ' Donec vitae sapien ut libero venenatis faucibus. Nullam quis ante.' \
       ' Etiam sit amet orci eget eros faucibus tincidunt. Duis leo.' \
       ' Sed fringilla mauris sit amet nibh. Donec sodales sagittis magna.' \
       ' Sed consequat, leo eget bibendum sodales, augue velit cursus nunc,'


def create_objects(name, number):
    for num in range(number):
        product = Product.objects.create(
            brand=Brand.objects.filter(name='MISSHA').first(),
            name=f'{name}{num}',
            ingredients=TEXT
        )
        product.save()


class AboutUsView(TemplateView):
    """
        The resource description view.
    """
    template_name = 'about_us.html'


class BrandCreate(CreateView):
    """
        A brand creation view.
    """
    model = Brand
    form_class = BrandForm
    template_name = 'brands/brand_create.html'
    success_url = reverse_lazy('app:product_create')


class CountryCreate(CreateView):
    """
        A country creation view.
    """
    model = Country
    form_class = CountryForm
    template_name = 'countries/country_create.html'
    success_url = reverse_lazy('app:brand_create')


class ProductList(ListView):
    """
        The product list view, where value of the 'Approved' field equal True,
        and required field contains 'search' parameters.
    """
    model = Product
    paginate_by = 10
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
                    | Q(brand__name__icontains=data)
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


class SuccessView(TemplateView):
    """
        Creation success view.
    """
    template_name = 'success.html'
