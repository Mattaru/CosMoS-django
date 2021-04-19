from django.db.models import Q
from django.core.paginator import Paginator
from django.views.generic import DetailView, ListView, UpdateView
from django.views.generic.base import TemplateView
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User


from app.models import Product
from app.forms import OneRowSearch
from acc.forms import ProductAdminForm


class AdministrationPanel(LoginRequiredMixin, TemplateView):
    """
        View with the product list, where the 'Approved' field equal False.
    """
    template_name = 'accounts/administration/admin_panel.html'

    def get_context_data(self, *args, **kwargs):
        context = super(AdministrationPanel, self).get_context_data(*args, **kwargs)
        if self.request.user.is_authenticated:
            qs = Product.objects.filter(approved=False)
            paginator = Paginator(qs, 10)
            page_number = self.request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            context['list_for_approval'] = page_obj

        return context


class AdminProductList(LoginRequiredMixin, ListView):
    """
        View with the product list.
    """
    model = Product
    paginate_by = 10
    template_name = 'accounts/administration/pages/admin_product_list.html'

    def get_context_data(self, **kwargs):
        context = super(AdminProductList, self).get_context_data(**kwargs)
        context['search_form'] = OneRowSearch()

        return context

    def get_queryset(self):
        queryset = []
        params = self.request.GET.dict()

        if params.get('search'):
            data = params.get('search')
            queryset = Product.objects.all()
            data_list = data.split(' ')
            data_list.insert(0, data)

            for data in data_list:
                qs = queryset.filter(
                    Q(name__icontains=data)
                    | Q(line__icontains=data)
                    | Q(brand__name__icontains=data)
                )
                if qs:
                    return qs

        return queryset


class AdminProductUpdate(LoginRequiredMixin, UpdateView, ):
    """
        View with the product update form.
    """
    model = Product
    form_class = ProductAdminForm
    success_url = reverse_lazy('acc:admin_panel')
    template_name = 'accounts/administration/pages/admin_product_update.html'
