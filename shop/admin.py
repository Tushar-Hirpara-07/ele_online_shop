from django.contrib import admin
from .models import *

class ImagesTublerinline(admin.TabularInline):
    model = Images
class TagsTublerinline(admin.TabularInline):
    model = Tags
class ProductAdmin(admin.ModelAdmin):
    inlines = [ImagesTublerinline,TagsTublerinline]
# Register your models here.
admin.site.register(Product,ProductAdmin)
admin.site.register(Categories)
admin.site.register(Color)
admin.site.register(Brands)
admin.site.register(Filter_price)
admin.site.register(Images)
admin.site.register(Tags)


