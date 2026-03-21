from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from blogs.apps import BlogsConfig
from blogs.views import BlogListView, BlogCreateView, BlogDetailView, BlogUpdateView, BlogDeleteView

app_name = BlogsConfig.name

urlpatterns = [
    path('blogs/', BlogListView.as_view(), name="blogs_list"),
    path('blogs/<int:pk>/', BlogDetailView.as_view(), name="blogs_detail"),
    path('blogs/create/', BlogCreateView.as_view(), name="blogs_create"),
    path('blogs/<int:pk>/update/', BlogUpdateView.as_view(), name="blogs_update"),
    path('blogs/<int:pk>/delete/', BlogDeleteView.as_view(), name="blogs_delete"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)