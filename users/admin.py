from django.contrib import admin

from users.models import User
from products.admin import BasketAdmin

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username',)
    inlines =  (BasketAdmin,)   # импортируем корзину из админки продукта для пользователя, возможно при наличии связи Forenkeyn


