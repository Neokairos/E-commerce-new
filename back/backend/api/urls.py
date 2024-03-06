from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, RegistrationAPIView,protected_view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


router = DefaultRouter()
router.register(r'products',ProductViewSet)

urlpatterns = [ path('register', RegistrationAPIView.as_view(), name='register'),
                path('protected_view', protected_view, name='protected_view'),
                path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
                path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    ]

urlpatterns += router.urls
