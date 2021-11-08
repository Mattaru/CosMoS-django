from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

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
    }

    def get_context_data(self, *args, **kwargs):
        context = super(MainPageView, self).get_context_data(*args, **kwargs)
        main_page_qs = cache.get_or_set(
            'main_page_queryset',
            Product.objects.filter(approved=True).order_by('-creation_date')[:9]
        )
        context['recently_added'] = main_page_qs

        return context


@method_decorator(cache_page(60*5), name='dispatch')
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
            .select_related('country')\
            .filter(approved=True)\
            .order_by('name')
        search_data = get_search_data(self.request)
        qs = cache.get_or_set('approved_product_list', approved_products)

        if search_data:
            search_list = make_list_from_searching_string(string=search_data)
            qs = get_queryset_with_filtered_data_for_search(
                queryset=approved_products,
                search_list=search_list
            )

        return qs


class ProductDetail(DetailView):
    """A product detail view."""
    model = Product
    template_name = 'products/product_detail.html'
    extra_context = {
        'search_form': OneRowSearch()
    }


class ProductCreate(LoginRequiredMixin, CreateView):
    """A product creation view."""
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('app:success')
    template_name = 'products/product_create.html'
    extra_context = {
        'search_form': OneRowSearch()
    }

    def form_valid(self, form):
        product = form.save(commit=False)
        product.created_by = self.request.user
        product.save()

        return super(ProductCreate, self).form_valid(form)


class SuccessView(TemplateView):
    """Creation success view."""
    template_name = 'success.html'
    extra_context = {
        'search_form': OneRowSearch()
    }
