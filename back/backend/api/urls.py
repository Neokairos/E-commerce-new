from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, RegistrationAPIView

router = DefaultRouter()
router.register(r'products',ProductViewSet)
urlpatterns = [path('/register', RegistrationAPIView.as_view(), name='register_user')]

urlpatterns += router.urls
