from django.urls import path
from .views import (
    ProductListView, ProductCreateView, ProductUpdateView, ProductDeleteView, ProductDetailView,
    BrandListView, BrandCreateView, BrandUpdateView, BrandDeleteView,
    StoreListView, StoreCreateView, StoreUpdateView, StoreDeleteView,
    PriceListView, PriceCreateView, PriceUpdateView, PriceDeleteView,
)

urlpatterns = [
    # Produits
    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/add/', ProductCreateView.as_view(), name='product_add'),
    path('products/<int:pk>/edit/', ProductUpdateView.as_view(), name='product_edit'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),


    # Marques
    path('brands/', BrandListView.as_view(), name='brand_list'),
    path('brands/add/', BrandCreateView.as_view(), name='brand_add'),
    path('brands/<int:pk>/edit/', BrandUpdateView.as_view(), name='brand_edit'),
    path('brands/<int:pk>/delete/', BrandDeleteView.as_view(), name='brand_delete'),

    # Magasins
    path('stores/', StoreListView.as_view(), name='store_list'),
    path('stores/add/', StoreCreateView.as_view(), name='store_add'),
    path('stores/<int:pk>/edit/', StoreUpdateView.as_view(), name='store_edit'),
    path('stores/<int:pk>/delete/', StoreDeleteView.as_view(), name='store_delete'),

    # Prix
    path('', PriceListView.as_view(), name='price_list'),
    path('add/', PriceCreateView.as_view(), name='price_add'),
    path('<int:pk>/edit/', PriceUpdateView.as_view(), name='price_edit'),
    path('<int:pk>/delete/', PriceDeleteView.as_view(), name='price_delete'),
]
