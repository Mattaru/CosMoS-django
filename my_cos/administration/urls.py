from django.urls import path, reverse_lazy

from .views import (
    AdministrationUnapprovedList,
    AdminProductList,
    AdminProductUpdate,
    AdminProductDelete,
    admin_unapproved_list_delete,
)


app_name = 'administration'

urlpatterns = [
    path('administration/', AdministrationUnapprovedList.as_view(), name='admin_unapproved_list'),
    path('administration/delete-all', admin_unapproved_list_delete, name='admin_delete_all_unapproved'),
    path('administration/list/', AdminProductList.as_view(), name='admin_product_list'),
    path('administration/<slug:slug>/', AdminProductUpdate.as_view(), name='admin_product_update'),
    path('administration/<slug:slug>/delete', AdminProductDelete.as_view(), name='admin_product_delete'),
]
