from django.urls import path

from app.views import (ProductDetail, ProductList)


app_name = 'app'

urlpatterns = [
    path('', ProductList.as_view(), name='product_list'),
    path('<int:pk>/', ProductDetail.as_view(), name='product_detail'),
]