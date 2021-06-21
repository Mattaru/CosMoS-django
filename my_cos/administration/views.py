from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.db.models import ProtectedError
from django.core.cache import cache
from django.core.paginator import Paginator
from django.views.generic import DeleteView, DetailView, ListView, UpdateView
from django.views.generic.base import TemplateView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect

from app.models import Product
from app.forms import OneRowSearch
from core.handlers import (make_list_from_searching_string,
    get_queryset_with_filtered_data_for_search,
    get_search_data)
from .forms import ProductAdminForm


class AdministrationUnapprovedList(LoginRequiredMixin, TemplateView):
    """View with the product list, where the 'Approved' field equal False."""
    template_name = 'administration/admin_unapproved_list.html'
    extra_context = {
        'search_form': OneRowSearch()
    }

    def get_context_data(self, *args, **kwargs):
        context = super(AdministrationUnapprovedList, self).get_context_data(*args, **kwargs)
        qs = cache.get_or_set(
            'unapproved_product_list',
            Product.objects.filter(approved=False).order_by('name')
        )
        paginator = Paginator(qs, 30)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['list_for_approval'] = page_obj

        return context


class AdminProductList(LoginRequiredMixin, ListView):
    """View with the product list."""
    model = Product
    paginate_by = 30
    template_name = 'administration/pages/admin_product_list.html'
    extra_context = {
        'search_form': OneRowSearch()
    }

    def get_queryset(self):
        queryset = super(AdminProductList, self).get_queryset()\
            .select_related('country')
        search_string = get_search_data(self.request)
        qs = cache.get_or_set('product_list', queryset)

        if search_string:
            search_list = make_list_from_searching_string(string=search_string)
            qs = get_queryset_with_filtered_data_for_search(
                queryset=queryset,
                search_list=search_list
            )

        return qs


class AdminProductUpdate(LoginRequiredMixin, UpdateView, ):
    """View with the product update form."""
    model = Product
    form_class = ProductAdminForm
    success_url = reverse_lazy('administration:admin_unapproved_list')
    template_name = 'administration/pages/admin_product_update.html'
    extra_context = {
        'search_form': OneRowSearch()
    }

    @transaction.atomic
    def form_valid(self, form):
        product = form.save(commit=False)
        product.save()
        form.save_m2m()

        return redirect(reverse_lazy('administration:admin_unapproved_list'))


class AdminProductDelete(LoginRequiredMixin, DeleteView):
    """Delete the particular product object."""
    model = Product
    form_class = ProductAdminForm
    success_url = reverse_lazy('administration:admin_unapproved_list')
    template_name = 'administration/pages/admin_product_delete.html'
    extra_context = {
        'search_form': OneRowSearch()
    }


@login_required
def admin_unapproved_list_delete(request):
    """Delete all of the products, where the 'approved' field equal False."""
    queryset = Product.objects.filter(approved=False)
    context = {
        'search_form': OneRowSearch()
    }

    if request.method == 'POST':
        try:
            queryset.delete()
        except ProtectedError:
            return HttpResponse("This object can't be deleted!!")
        return HttpResponseRedirect(reverse_lazy('administration:admin_unapproved_list'))

    return render(
        request,
        'administration/pages/admin_product_delete_unapproved.html',
        context
    )
