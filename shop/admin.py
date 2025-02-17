from django.contrib import admin
from .models import Brand, Shoe, Category
class BrandAdmin(admin.ModelAdmin):
    list_display = ("name","description","logo")
    list_filter = ("name",)
    search_fields = ("name",)

class ShoeAdmin(admin.ModelAdmin):
    list_display = ("name","color","price","size","sale","gender","slug",)
    list_filter = ("name","color","price","size","sale","gender","slug",)
    search_fields = ("name","slug",)
    list_per_page = 25

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name","description")
    list_filter = ("name",)
    search_fields = ("name",)

admin.site.register(Brand, BrandAdmin)
admin.site.register(Shoe,ShoeAdmin)
admin.site.register(Category,CategoryAdmin)

