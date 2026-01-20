from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Product, Category

from .forms import ProductForm
from django.urls import reverse_lazy

class CategoryListViewSet(ListView):
    queryset = Category.objects.all()
    context_object_name = 'category'
    template_name = 'category_list.html'

class ProductListViewSet(ListView):
    queryset = Product.objects.all()
    context_object_name = 'products'
    template_name = 'product_list.html'

class ProductDetailViewSet(DetailView):
    queryset = Product.objects.all()
    context_object_name = 'products'
    template_name = 'product_detail.html'

class ProductCreateViewSet(CreateView):
    form_class = ProductForm
    template_name = 'product_create.html'
    success_url = reverse_lazy('product_list')

class ProductUpdateViewSet(UpdateView):
    queryset = Product.objects.all()
    form_class = ProductForm
    context_object_name = 'product_update'
    template_name = 'product_update.html'
    success_url = reverse_lazy('product_list')


class ProductDeleteViewSet(DeleteView):
    queryset = Product.objects.all()
    context_object_name = 'product_delete'
    template_name = 'product_delete.html'
    success_url = reverse_lazy('product_list')



