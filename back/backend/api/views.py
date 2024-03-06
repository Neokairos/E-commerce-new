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
from django.contrib.auth import login
from .models import User
from .renderers import UserJSONRenderer
from rest_framework.decorators import api_view, permission_classes
from .serializers import (
   RegistrationSerializer,
   LoginSerializer,
   LogoutSerializer,
   UserSerializer,
)




class RegistrationAPIView(APIView):
   permission_classes = (AllowAny,)
   renderer_classes = (UserJSONRenderer,)
   serializer_class = RegistrationSerializer

   def post(self,request: Request) -> Response:
      user_request = request.data.get('user',{}) #returning an empty object if key pair user not found in dict
      serializer = self.serializer_class(data=user_request)
      serializer.is_valid(raise_exception=True)
      user = serializer.save()
      
      login(request, user)
      tokens = user.tokens
      
      return Response({
         'user':serializer.data,
         'tokens': tokens
      }, status=status.HTTP_201_CREATED)


class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = LoginSerializer




class ProductViewSet(viewsets.ModelViewSet):
   queryset = Product.objects.all()
   
   serializer_class = ProductSerializer
   def get_serializer_context(self):
      return {"request": self.request}