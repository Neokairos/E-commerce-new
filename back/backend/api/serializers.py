from rest_framework import serializers
from .models import Product
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from .models import User
from .utils import validate_email as email_is_valid


class RegistrationSerializer(serializers.ModelSerializer[User]):
    
    password = serializers.CharField(max_length=20,min_length=4,write_only=True)
    
    class Meta:
        model = User
        fields = ['username',
                'email',
                'password',
                'is_staff',
                'is_active',
                'created_at',
                'updated_at',
                'birth_date']

    def validate_email(self, value:str) -> str:
        valid, error_text = email_is_valid(value)
        if not valid:
        #if valid is False
            raise serializers.ValidationError(error_text)
        try:
            #splitting the email in two vars and starting it from @
            email_name, domain_part = value.strip().rsplit('@',1)
        except ValueError:
            raise ValueError("Email address must contain exactly one '@' symbol.")
        else:
            value = '@'.join([email_name, domain_part.lower()])
            
        return value
            
    

    def create(self, validated_data):
        user = user.objects.create_user(
            username=validated_data['username'], email=validated_data['email'], password=validated_data['password']
        )
        return user

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

