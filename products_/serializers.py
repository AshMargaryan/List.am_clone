from rest_framework.serializers import ModelSerializer

from .models import Product

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ('title', 'about_product', 'price', 'category', 'subcategory', 'posted_date', 'updated_date', 'author',)
