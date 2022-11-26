from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


# Create your models here.
class UserAccountManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("All users are required to have an email.")
        
        email=self.normalize_email(email)
        user=self.model(email=email, **extra_fields)

        #SET PASSWORD - SALTS PASSWORDS FOR STORING IN DB
        user.set_password(password)
        user.save()

        return user
    
    def create_superuser(self, email, password, **extra_fields):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
            is_superuser=True,
            **extra_fields,
        )
        user.is_staff = True
        user.is_admin = True
        user.save()
        return user
    
# Email: me_admin@gmail.com
# First name: Me
# Last name: Admin
# Password: Merror_1234 / Merror_12345
# Test_123456

class UserAccount(AbstractBaseUser, PermissionsMixin):
    # User Account Attributes
    email=models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    city=models.CharField(max_length=255, default='College Station')
    head_shot=models.ImageField(upload_to='user_profile_images', blank=True)

    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_admin=models.BooleanField(default=False)

    objects= UserAccountManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS= ['first_name', 'last_name']

    def get_user(self):
        return self.first_name
    
    def get_head_shot(self):
        return self.head_shot
    
    def get_city(self):
        return self.city

    def __str__(self):
        return self.email