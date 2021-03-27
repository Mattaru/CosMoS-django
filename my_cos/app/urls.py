from django.urls import path

from app.views import (
    AboutUsView,
    BrandCreate,
    CountryCreate,
    ProductDetail,
    ProductList,
    ProductCreate,
    SuccessView
)


app_name = 'app'

urlpatterns = [
    path('', ProductList.as_view(), name='product_list'),
    path('about-us/', AboutUsView.as_view(), name='about_us'),
    path('<int:pk>/', ProductDetail.as_view(), name='product_detail'),
    path('create/', ProductCreate.as_view(), name='product_create'),
    path('create/brand/', BrandCreate.as_view(), name='brand_create'),
    path('create/brand/country', CountryCreate.as_view(), name='country_create'),
    path('success', SuccessView.as_view(), name='success'),
]