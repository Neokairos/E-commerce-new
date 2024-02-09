from .models import Product
from .serializers import ProductSerializer
from rest_framework import viewsets
from typing import Any, Optional

from django.conf import settings
from django.shortcuts import get_object_or_404
from rest_framework import parsers, status
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from .serializers import (
    RegistrationSerializer,
)



class RegistrationAPIView(APIView):
   permission_classes = (AllowAny,)
   serializer_class = RegistrationSerializer

   def post(self,request: Request) -> Response:
      user_request = request.data.get('user',{}) #returning an empty object if key pair user not found in dict
      serializer = self.serializer_class(data=user_request)
      serializer.is_valid(raise_exception=True)
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)



class ProductViewSet(viewsets.ModelViewSet):
   queryset = Product.objects.all()
   
   serializer_class = ProductSerializer
   def get_serializer_context(self):
      return {"request": self.request}