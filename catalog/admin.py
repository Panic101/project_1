from django.contrib import admin

from .models import ProductDirectory, ProductItem
# Register your models here.

class ProductItemInline(admin.TabularInline):
    model = ProductItem
    extra = 1

class ProductDirectoryAdmin(admin.ModelAdmin):    
    fieldsets = [
        ('Directory Name',               {'fields': ['directory_name'], 'classes': ['collapse']}),
        ('Total Items in Directory', {'fields': ['total_items'], 'classes': ['collapse']}),
    ]
    inlines = [ProductItemInline]
    list_display = ('directory_name', 'total_items')
    search_fields = ['directory_name']

admin.site.register(ProductDirectory, ProductDirectoryAdmin)

