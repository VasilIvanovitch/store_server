from django.contrib import admin
from products.models import ProductCategory, Product, Basket
from users.models import User

# class WomenAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title', 'time_create', 'photo', 'is_published')
#     list_display_links = ('id', 'title')
#     search_fields = ('title', 'content')
#     list_editable = ('is_published',)
#     list_filter = ('is_published', 'time_create')
#     prepopulated_fields = {"slug": ("title",)}
#
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name')
#     list_display_links = ('id', 'name')
#     search_fields = ('name',)
#     prepopulated_fields = {"slug": ("name",)}


#admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(ProductCategory)
#admin.site.register(Product)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'quontity', 'category',)
    fields = ('image', 'name', 'description', ('price', 'quontity'), 'category')
    readonly_fields = ('description',)
    search_fields = ('name', 'price',)
    ordering = ('name',)

class BasketAdmin(admin.TabularInline):
    model = Basket
    list_display = ('product', 'quontity', 'created_timestamp')
    readonly_fields = ('created_timestamp',)
    extra = 0