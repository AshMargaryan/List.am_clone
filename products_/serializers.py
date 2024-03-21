from rest_framework.serializers import ModelSerializer, ListField, ImageField

from .models import Product, ProductImage

class ProductImageSerializer(ModelSerializer):
    class Meta:
        model = ProductImage
        fields = "__all__"


class ProductSerializer(ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    uploaded_images = ListField(
        child=ImageField(max_length=100000, allow_empty_file=False, use_url=False),
        write_only=True
    )
    class Meta:
        model = Product
        fields = ('title', 'about_product', 'price', 'category', 'subcategory', 'posted_date',
                  'updated_date', 'author', 'images', 'uploaded_images')

        def create(self, validated_data):
            uploaded_images = validated_data.pop("uploaded_images")
            product = Product.objects.create(**validated_data)
            for image in uploaded_images:
                ProductImage.objects.create(product=product, image=image)

            return product

