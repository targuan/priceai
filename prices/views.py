from django.db.models import Q
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import Price, Product, Store, Brand

class StoreListView(ListView):
    model = Store
    template_name = 'prices/store_list.html'
    context_object_name = 'stores'
    paginate_by = 20  # optionnel

    def get_queryset(self):
        return Store.objects.all().order_by('name')


class StoreCreateView(CreateView):
    model = Store
    template_name = 'prices/store_form.html'
    fields = ['name', 'store_type', 'city']

    def get_success_url(self):
        return reverse_lazy('store_list')


class StoreUpdateView(UpdateView):
    model = Store
    template_name = 'prices/store_form.html'
    fields = ['name', 'store_type', 'city']

    def get_success_url(self):
        return reverse_lazy('store_list')


class StoreDeleteView(DeleteView):
    model = Store
    template_name = 'prices/store_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('store_list')


class BrandListView(ListView):
    model = Brand
    template_name = 'prices/brand_list.html'
    context_object_name = 'brands'
    paginate_by = 20

    def get_queryset(self):
        return Brand.objects.all().order_by('name')


class BrandCreateView(CreateView):
    model = Brand
    template_name = 'prices/brand_form.html'
    fields = ['name']

    def get_success_url(self):
        return reverse_lazy('brand_list')


class BrandUpdateView(UpdateView):
    model = Brand
    template_name = 'prices/brand_form.html'
    fields = ['name']

    def get_success_url(self):
        return reverse_lazy('brand_list')


class BrandDeleteView(DeleteView):
    model = Brand
    template_name = 'prices/brand_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('brand_list')

class PriceListView(ListView):
    model = Price
    template_name = 'prices/price_list.html'
    context_object_name = 'prices'
    paginate_by = 20  # Optionnel : pagination

    def get_queryset(self):
        # On récupère tous les prix avec les relations préchargées pour éviter les requêtes multiples
        queryset = Price.objects.select_related('product', 'product__brand', 'store').order_by('-date')

        search_query = self.request.GET.get('q')
        if search_query:
            queryset = queryset.filter(
                Q(product__name__icontains=search_query) |
                Q(product__brand__name__icontains=search_query) |
                Q(store__name__icontains=search_query)
            )

        return queryset


class PriceCreateView(CreateView):
    model = Price
    template_name = 'prices/price_form.html'
    fields = ['product', 'store', 'amount']

    def get_success_url(self):
        return reverse_lazy('price_list')


class PriceUpdateView(UpdateView):
    model = Price
    template_name = 'prices/price_form.html'
    fields = ['product', 'store', 'amount']

    def get_success_url(self):
        return reverse_lazy('price_list')


class PriceDeleteView(DeleteView):
    model = Price
    template_name = 'prices/price_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('price_list')


class ProductListView(ListView):
    model = Product
    template_name = 'prices/product_list.html'
    context_object_name = 'products'
    paginate_by = 20

    def get_queryset(self):
        queryset = Product.objects.select_related('brand').order_by('name')
        search_query = self.request.GET.get('q')
        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query) |
                Q(brand__name__icontains=search_query)
            )
        return queryset


class ProductCreateView(CreateView):
    model = Product
    template_name = 'prices/product_form.html'
    fields = ['name', 'brand', 'packaging']

    def get_success_url(self):
        return reverse_lazy('product_list')


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'prices/product_form.html'
    fields = ['name', 'brand', 'packaging']

    def get_success_url(self):
        return reverse_lazy('product_list')


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'prices/product_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('product_list')

class ProductDetailView(DetailView):
    model = Product
    template_name = 'prices/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Historique des prix du produit trié par date décroissante
        context['prices'] = Price.objects.filter(product=self.object).select_related('store').order_by('-date')
        return context
