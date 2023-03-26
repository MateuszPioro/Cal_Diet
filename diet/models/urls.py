from rest_framework import routers
from django.urls import include, path
from .views import ProductViewSet, DiaryViewSet
from .import views


router = routers.DefaultRouter()
router.register(r'products',ProductViewSet, basename='product')
router.register(r'diet', DiaryViewSet, basename='diet')

urlpatterns = [
    path('api/',include(router.urls)),
    path('api-auth/', include('rest_framework.urls',namespace='rest_framework')),
    path('products/',views.product_list,name='product_list'),
    path('diary/',views.diary_list,name='diary_list'),
    path('diary/<int:diary_id>/',views.diary_detail,name='diary_detail'),
    path('diary/<int:diary_id>/remove/<int:product_id>/',views.diary_remove_product,name='diary_remove_product'),
    path('diary/add_product/<int:diary_id>/',views.diary_add_product,name='diary_add_product'),
    path('add_product/',views.add_product,name="add_product"),
    path('products/<int:product_id>',views.remove_product,name='remove_product')
]
