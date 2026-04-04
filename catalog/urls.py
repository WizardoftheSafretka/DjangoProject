from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import HomeListView, HomeDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('home/', HomeListView.as_view(), name="home"),
    path('product/<int:pk>/', HomeDetailView.as_view(), name="product_detail"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)