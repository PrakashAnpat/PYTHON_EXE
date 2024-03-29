from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser
from django.conf import settings
User = settings.AUTH_USER_MODEL
# Create your models here.

class User(AbstractBaseUser):
    username= None
    email= models.EmailField(verbose_name='email address',max_length=255,unique=True)
    is_active= models.BooleanField(default=True)
    staff= models.BooleanField(default=False)
    admin= models.BooleanField(default=False)
    
    USERNAME_FIELD= 'username'
    REQUIRED_FIELDS= []
    
    def get_full_name(self):
        return self.email
    
    def short_full_name(self):
        return self.email

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self,app_label):
        return True
    
    @property
    def is_staff(self):
        return self.staff
    
    @property
    def is_admin(self):
        return self.admin
    
class UserManager(BaseUserManager):
    
    def create_user(self,email,password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(email=self.normalize_email(email),        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_staffuser(self,email,password):
        user = self.create_user(email,password=password,)
        user.staff = True
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password):
        user = self.create_user(email,password=password,)
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser): 
    
    objects = UserManager()