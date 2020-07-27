from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from product.models import Product

class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""
    
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    
    first_regex = RegexValidator(regex=r'^\w[a-z|A-Z]+$', message='Enter valid first name')
    last_regex = RegexValidator(regex=r'^\w[a-z|A-Z]+$', message='Enter valid last name')
    phone_regex = RegexValidator(regex=r'^[9|8|7|6]\d{9}', message='Enter valid phone number')

    """Model definition for User."""
    username = None
    first_name = models.CharField(max_length=250, null=False, validators=[first_regex])
    last_name = models.CharField(max_length=250, null=False, validators=[last_regex])
    email = models.EmailField(
        verbose_name=_('email address'), max_length=255, unique=True
    )
    phone = models.CharField(max_length=10, unique=True, validators=[phone_regex])
    cart = models.ManyToManyField(Product)
    verified_email = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone']

    objects = UserManager()

    class Meta:
        """Meta definition for User."""
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        """Unicode representation of User."""
        return f'{self.first_name} {self.last_name}({self.email})'