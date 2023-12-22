from django.urls import path
from products.views import products, basket_add, basket_remove

app_name = 'products'

urlpatterns = [
    path('', products, name = 'index'),
    path('category/<int:cat_id>/', products, name = 'view_category'),
    path('page/<int:page>/', products, name = 'paginator'),
    path('baskets/add/<int:product_id>/', basket_add, name = 'basket_add'),
    path('baskets/remove/<int:basket_id>/', basket_remove, name = 'basket_remove')
]