from django.urls import path, re_path
from shop import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "shop"

urlpatterns = [
    path("", views.Index, name="index"),
    path("products", views.Products,name="products"),
    path("search",views.Search,name="search"),
    path("<str:id>",views.Single_product,name="single_product")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)