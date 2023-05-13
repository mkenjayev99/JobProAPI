from django.conf import settings
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils.safestring import mark_safe
from rest_framework_simplejwt.tokens import RefreshToken


class AccountManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        if email is None:
            raise TypeError('User should have an email')
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        if password is None:
            raise TypeError('Password should not be None')

        user = self.create_user(
            email=email,
            password=password,
            **extra_fields,
        )
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save(using=self._db)
        return user


def file_path(instance, filename):
    return f"courses/{instance.title}/{instance.title}/{filename}"


class Account(AbstractBaseUser, PermissionsMixin):
    ROLE = (
        (0, 'HR'),
        (1, 'Candidate'),
        (2, 'Staff'),
    )
    email = models.EmailField(max_length=50, unique=True, verbose_name='Email', db_index=True)
    first_name = models.CharField(max_length=50, verbose_name='First name', null=True)
    last_name = models.CharField(max_length=50, verbose_name='Last name', null=True)
    image = models.ImageField(upload_to=file_path, null=True, blank=True)
    role = models.IntegerField(choices=ROLE, default=1)
    location = models.ForeignKey('main.City', on_delete=models.CASCADE, null=True, blank=True)
    is_superuser = models.BooleanField(default=False, verbose_name='Super user')
    is_active = models.BooleanField(default=True, verbose_name='Active user')
    is_staff = models.BooleanField(default=False, verbose_name='Staff user')
    bio = models.TextField()
    date_modified = models.DateTimeField(auto_now=True, verbose_name='Date modified')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Date created')
    objects = AccountManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    @property
    def position(self):
        position = models.ForeignKey('main.Position', on_delete=models.CASCADE, null=True, blank=True)
        if Account.ROLE == 1:
            return position
        return None

    def __str__(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        return self.email

    def image_tag(self):
        if self.image:
            return mark_safe(f'<a href="{self.image.url}"><img src="{self.image.url}" style="height:30px;"/></a>')
        else:
            return "-"

    @property
    def image_url(self):
        if self.image:
            if settings.DEBUG:
                return f'{settings.LOCAL_BASE_URL}{self.image.url}'
            return f'{settings.PROD_BASE_URL}{self.image.url}'
        return None

    @property
    def tokens(self):
        refresh = RefreshToken.for_user(self)
        data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
        return data


class WorkHistory(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='work_history')
    company = models.ForeignKey('main.Company', on_delete=models.SET_NULL, null=True, blank=True)
    location = models.ForeignKey('main.City', on_delete=models.SET_NULL, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    is_current = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.account} - {self.company}'
