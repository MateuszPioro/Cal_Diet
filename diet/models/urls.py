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
    path('diary/add_product/<int:diary_id>/',views.add_product_to_diary,name='add_product_to_diary'),
    path('add_product/',views.add_product,name="add_product"),
    path('products/<int:product_id>',views.remove_product,name='remove_product'),
    path('product/<int:product_id>',views.update_product,name='update_product'),
    path('add_diary/',views.add_diary,name="add_diary"),
    path('diary/<int:diary_id>/add_product/', views.add_product_to_diary, name='add_product_to_diary'),
    path('diary/<int:diary_id>/update_product_grams/<int:product_id>/',views.update_product_grams, name='update_product_grams'),
]
