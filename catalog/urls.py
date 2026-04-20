from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import HomeListView, HomeDetailView, HomeUpdateView, HomeDeleteView, HomeCreateView, \
    UnpublishProductView, CategoryDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeListView.as_view(), name="home"),
    path('product/<int:pk>/', HomeDetailView.as_view(), name="product_detail"),
    path('product/create/', HomeCreateView.as_view(), name="product_create"),
    path('product/<int:pk>/update/', HomeUpdateView.as_view(), name="product_update"),
    path('product/<int:pk>/delete/', HomeDeleteView.as_view(), name="product_delete"),
    path('product/unpublish/<int:pk>', UnpublishProductView.as_view(), name='product_unpublish'),
    path('category/<int:pk>/products/', CategoryDetailView.as_view(), name='category_products')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)