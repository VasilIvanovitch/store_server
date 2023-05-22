# from users.models import User

from django.contrib import admin

from products.models import Basket, Product, ProductCategory

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


# admin.site.register(ProductCategory, ProductCategoryAdmin)
# admin.site.register(Product)

admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'quontity', 'category',)
    fields = ('image', 'name', 'description', ('price', 'quontity'), 'stripe_product_price_id', 'category')
    readonly_fields = ('stripe_product_price_id',)
    search_fields = ('name', 'price',)
    ordering = ('name',)


class BasketAdmin(admin.TabularInline):
    model = Basket
    list_display = ('product', 'quontity', 'created_timestamp')
    readonly_fields = ('created_timestamp',)
    extra = 0
