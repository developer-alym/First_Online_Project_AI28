from django.urls import path
from .views import (CategoryListViewSet, ProductListViewSet,
                    ProductDetailViewSet, ProductCreateViewSet,
                    ProductUpdateViewSet, ProductDeleteViewSet)


urlpatterns = [
    path('category/', CategoryListViewSet.as_view(), name='category_list'),
    path('product/', ProductListViewSet.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductDetailViewSet.as_view(), name='product_detail'),
    path('create_product/', ProductCreateViewSet.as_view(), name='product_create'),
    path('product_update/<int:pk>/',  ProductUpdateViewSet.as_view(), name='product_update'),
    path('product_delete/<int:pk>/', ProductDeleteViewSet.as_view(), name='product_delete')
]