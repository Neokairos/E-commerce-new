from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
import uuid
from typing import Any, Optional
from rest_framework_simplejwt.tokens import RefreshToken

class UserManager(BaseUserManager):
    def create_user(self,username:str, email:str, password:Optional[str]=None) -> 'User':
        
        if username is None:
            raise TypeError('Users must have an username')

        if email is None:
            raise TypeError('Users must have an email nigga')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        
        return user
    
    def create_sudo(self,username:str,email:str,password:str) -> "User":
        
        if password is None:
            raise TypeError('Superusers must have a password.')
        
        user = self.create_user(username,email,password)
        user.is_superuser = True
        user.is_active = True
        user.is_staff = True
        user.save()

        return user

class User(AbstractBaseUser,PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(db_index=True, max_lengh=255, unique=True)
    email = models.EmailField(db_index=True,unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DatetimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    birth_date = models.DateField(null=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    objects = UserManager()

    def __str__(self) -> str:
        string = self.email if self.email != '' else self.get_user_name()
        return f'{self.id} {string}'

    @property
    def tokens(self) -> dict[str,str]:
        """Allow us to get a user's token by calling `user.token`."""
        refresh = RefreshToken.for_user(self)
        return {'refresh': str(refresh), 'access': str(refresh.access_token)}
    



class Product(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=9,decimal_places=2)
    description = models.TextField(default="nigga be empty")
    image = models.ImageField(upload_to='images/')
    rating = models.DecimalField(max_digits=2, decimal_places=2, null=True, blank=True)


