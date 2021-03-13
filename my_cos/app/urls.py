from django.urls import path

from app.views import (starting_page, ProductDetail, ProductList)


app_name = 'app'

urlpatterns = [
    path('', starting_page, name='starting_page'),
    path('list/', ProductList.as_view(), name='product_list'),
    path('list/<int:pk>/', ProductDetail.as_view(), name='product_detail'),
]