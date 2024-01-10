
from django.urls import path

from . import views

app_name = 'goods'

urlpatterns = [
    path('<slug:catalog_slug>/', views.catalog, name='index'),
    path('<slug:catalog_slug>/<int:page>/', views.catalog, name='index'),
    path('product/<slug:product_slug>/', views.product, name='product'),

]