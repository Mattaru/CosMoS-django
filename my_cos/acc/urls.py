from django.urls import path, reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView

from acc.views import (
    AdministrationPanel,
    AdminProductList,
    AdminProductUpdate,
    AdminProductDelete,
    admin_unapproved_list_delete,
)


app_name = 'acc'

urlpatterns = [
    path('login/', LoginView.as_view(
        template_name='accounts/login.html'
    ), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('administration/', AdministrationPanel.as_view(), name='admin_panel'),
    path('administration/delete-all', admin_unapproved_list_delete, name='admin_delete_all_unapproved'),
    path('administration/list/', AdminProductList.as_view(), name='admin_product_list'),
    path('administration/<int:pk>/', AdminProductUpdate.as_view(), name='admin_product_update'),
    path('administration/<int:pk>/delete', AdminProductDelete.as_view(), name='admin_product_delete'),
]