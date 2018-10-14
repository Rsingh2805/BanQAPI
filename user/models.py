from django.db import models
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone

class BUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Enter email')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        user = self.create_user(email, password, **extra_fields)
        user.is_superuser = True
        user.is_active = True
        user.is_staff = True
        user.save()
        return user


class BUser(AbstractBaseUser, PermissionsMixin):
    USER_TYPE = (
        ('BAN', 'Banquet Hall'),
        ('USR', 'User')
        # ('AMB', 'Campus Ambassador'),
    )

    name = models.CharField(max_length=50, )
    user_type = models.CharField(
        max_length=3, choices=USER_TYPE, default='USR', verbose_name='User Type')
    email = models.EmailField(
        verbose_name='Email Address', max_length=255, unique=True, db_index=True)
    phone = models.CharField(max_length=10, verbose_name="Contact Number")
    state = models.CharField(max_length=20, verbose_name='State')
    last_updated = models.DateTimeField(verbose_name='Last Updated', auto_now=True, null=True)
    date_joined = models.DateTimeField(verbose_name='Date Joined', blank=True, default=timezone.now, null=True)
    objects = BUserManager()
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['user_type',  'name', 'phone', 'state']
    is_active = models.BooleanField(
        verbose_name='Active',
        default=True,
        help_text='Designates whether this user should be treated as active. '
                  'Unselect this instead of deleting accounts.',
    )
    is_staff = models.BooleanField(
        verbose_name='Staff Status',
        default=False,
        help_text='Check if is staff ',
    )

    def __str__(self):
        return self.email

    def get_short_name(self):
        return self.name

    def get_full_name(self):
        return self.name

    class Meta:
        verbose_name_plural = "Users"


