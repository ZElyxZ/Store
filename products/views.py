from django.http import HttpResponseRedirect
from products.models import *
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, ListView
from common.views import TitleMixixn

class IndexView(TitleMixixn, TemplateView):
    template_name = 'products/index.html'
    title = 'Home'

class ProductsListView(TitleMixixn, ListView):
    model = Product
    template_name = 'products/products.html'
    paginate_by = 3
    title = 'Products'

    def get_queryset(self):
        queryset = super(ProductsListView, self).get_queryset()
        cat_id = self.kwargs.get('cat_id')  # C помощью get если нет такого ключа => None
        return queryset.filter(category_id=cat_id) if cat_id else queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductsListView, self).get_context_data()
        context['category'] = ProductCategory.objects.all()
        return context


@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    basket = Basket.objects.filter(user=request.user, product=product).first()
    if not basket:
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket.quantity += 1
        basket.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required()
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
