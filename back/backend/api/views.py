from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from rest_framework import viewsets

class ProductViewSet(viewsets.ModelViewSet):
   queryset = Product.objects.all()
   
   serializer_class = ProductSerializer
   def get_serializer_context(self):
      return {"request": self.request}