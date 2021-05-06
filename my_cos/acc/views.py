from django.db.models import ProtectedError, Q
from django.core.paginator import Paginator
from django.views.generic import DeleteView, DetailView, ListView, UpdateView
from django.views.generic.base import TemplateView
from django.shortcuts import get_object_or_404, get_list_or_404, render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin

from app.models import Product
from app.forms import OneRowSearch
from acc.forms import ProductAdminForm


class AdministrationUnapprovedList(LoginRequiredMixin, TemplateView):
    """
        View with the product list, where the 'Approved' field equal False.
    """
    template_name = 'accounts/administration/admin_unapproved_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(AdministrationUnapprovedList, self).get_context_data(*args, **kwargs)

        if self.request.user.is_authenticated:
            qs = Product.objects.filter(approved=False).order_by('name')
            paginator = Paginator(qs, 30)
            page_number = self.request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            context['list_for_approval'] = page_obj

        return context


class AdminProductList(LoginRequiredMixin, ListView):
    """
        View with the product list.
    """
    model = Product
    paginate_by = 30
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
                    | Q(brand__icontains=data)
                ).order_by('name')
                if qs:
                    return qs

        return queryset


class AdminProductUpdate(LoginRequiredMixin, UpdateView, ):
    """
        View with the product update form.
    """
    model = Product
    form_class = ProductAdminForm
    success_url = reverse_lazy('acc:admin_unapproved_list')
    template_name = 'accounts/administration/pages/admin_product_update.html'

    def get_context_data(self, **kwargs):
        context = super(AdminProductUpdate, self).get_context_data(**kwargs)
        context['search_form'] = OneRowSearch

        return context


class AdminProductDelete(LoginRequiredMixin, DeleteView):
    """
        Delete the particular product object.
    """
    model = Product
    form_class = ProductAdminForm
    success_url = reverse_lazy('acc:admin_unapproved_list')
    template_name = 'accounts/administration/pages/admin_product_delete.html'


def admin_unapproved_list_delete(request):
    """
    Delete all of the products, where the 'approved' field equal False.
    """
    query_set = Product.objects.filter(approved=False)

    if request.method == 'POST':
        try:
            query_set.delete()
        except ProtectedError:
            return HttpResponse("This object can't be deleted!!")
        return HttpResponseRedirect(reverse_lazy('acc:admin_unapproved_list'))

    return render(request, 'accounts/administration/pages/admin_product_delete_unapproved.html')
