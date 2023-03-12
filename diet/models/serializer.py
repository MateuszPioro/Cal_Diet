from .models import Product,Diary
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        

class DiarySerializer(serializers.ModelSerializer):
    products = serializers.SlugRelatedField(
        many=True,
        slug_field='name',
        queryset=Product.objects.all()

    )
    
    class Meta:
        model = Diary
        fields = ('id','date', 'name', 'products')
