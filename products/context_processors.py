from products.models import Basket


def baskets(request):
    # Получаем текущего пользователя
    user = request.user
    # Извлекаем данные из модели Basket для текущего пользователя
    basket_items = Basket.objects.filter(user=user) if user.is_authenticated else []
    # Добавляем данные в контекст шаблона
    return {'baskets': basket_items}
