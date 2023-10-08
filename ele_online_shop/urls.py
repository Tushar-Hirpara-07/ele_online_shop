from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("shop.urls")),# requests on a route starting with "myapp/" will be forwarded to "myapp.urls"
]