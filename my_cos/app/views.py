from django.db.models import Q
from django.shortcuts import get_list_or_404, render
from django.views.generic import ListView, DetailView

from app.models import Product, Country, Brand
from app.forms import OneRowSearch


# def starting_page(request):
#     return render(request, 'starting_page.html')


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

