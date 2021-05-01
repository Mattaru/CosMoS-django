from django.urls import path

from app.views import (
    AboutUsView,
    MainPageView,
    ProductDetail,
    ProductList,
    ProductCreate,
    SuccessView
)


app_name = 'app'

urlpatterns = [
    path('', MainPageView.as_view(), name='main_page'),
    path('list/', ProductList.as_view(), name='product_list'),
    path('list/<int:pk>/', ProductDetail.as_view(), name='product_detail'),
    path('create/', ProductCreate.as_view(), name='product_create'),
    path('about-us/', AboutUsView.as_view(), name='about_us'),
    path('success', SuccessView.as_view(), name='success'),
]