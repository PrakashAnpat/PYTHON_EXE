from django.db import models
from django.contrib.auth.models import AbstractUser,PermissionsMixin,AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager   
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self,email,password,**extra_fields):
        if not email:
            raise ValueError(_('The email must be set'))
        email= self.normalize_email(email)
        user= self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self,email,password,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_superuser',True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser is must have superuser=True'))
        return self.create_user(email,password,**extra_fields)
    
    
    
    
# class CustomUser(AbstractUser):
    # username= None
    # email= models.EmailField(_('email address'),unique=True)
    
    # USERNAME_FIELD= 'email'
    # REQUIRED_FIELDS= []
    
    # objects= CustomUserManager()
    
    # def __str__(self):
    #     return self.email

class CustomUser(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(max_length=100, blank=False, null=False, unique=True)
    first_name = models.CharField(max_length=150, blank=False, null=False)
    last_name = models.CharField(max_length=150, blank=False, null=False)
    # email= models.EmailField(_('email address'),unique=True)
    email= models.EmailField(_('email address'))
    is_staff= models.BooleanField(default=False)
    is_active= models.BooleanField(default=False)
    date_joined= models.DateTimeField(default=timezone.now)
    
    # USERNAME_FIELD= 'email'
    USERNAME_FIELD= 'username'
    REQUIRED_FIELDS= ['email']
    
    objects= CustomUserManager()
    
    def __str__(self):
        return self.email