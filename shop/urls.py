from django.urls import path
from shop import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "myapp"

urlpatterns = [
    path("", views.Index, name="index"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
