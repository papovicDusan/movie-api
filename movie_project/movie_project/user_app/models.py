from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# from ..movie_view.models import Movie
#
# from django.contrib.auth import get_user_model
#
#
# User = get_user_model()


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, email, password, name, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        if not name:
            raise ValueError(_('The name must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, name, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, name, **extra_fields)


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    name = models.CharField(max_length=60)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = CustomUserManager()

    def __str__(self):
        return self.email


# class MovieWatchlist(models.Model):
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_watchlist')
#     movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_watchlist')
#     is_watched = models.BooleanField(default=False)
#
#     # class Meta:
#     #    pass # unique_together = ('user',)

# class MovieWatchlist(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_watchlist')
#     movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_watchlist')
#     is_watched = models.BooleanField(default=False)