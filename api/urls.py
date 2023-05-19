from django.urls import path, include

from rest_framework import routers

from api.views import ProductModelViewSet

app_name = 'api'


router = routers.DefaultRouter()
router.register(r'products',ProductModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('product-list/', ProductListAPIView.as_view(), name='product_list'),

]