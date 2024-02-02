from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    seller = serializers.ReadOnlyField(source='seller.username')

    class Meta:
        model = Product
        fields = ['id','seller', 'title', 'price', 'description', 'image', 'rating']
    def create(self, validated_data):
        image = validated_data.pop('image')
        product = Product.objects.create(**validated_data)
        product.image.save(image.name, image)
        return product
