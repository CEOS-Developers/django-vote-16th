from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of username
    """

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email=self.normalize_email(email), password=password, **extra_fields)



PART_CHOICE = (
    ('Backend', 'Backend'),
    ('Frontend', 'Frontend'),
    ('Design', 'Design'),
    ('PM', 'PM')
)


TEAM_CHOICE = (
    ('Recipeasy', 'Recipeasy'),
    ('Forgetmenot', 'Forgetmenot'),
    ('Prefolio', 'Prefolio'),
    ('Diametes', 'Diametes'),
    ('Teample', 'Teample')
)


class User(AbstractUser):
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=500)
    name = models.CharField(max_length=20)
    part = models.CharField(max_length=20, choices=PART_CHOICE)
    team = models.CharField(max_length=20, choices=TEAM_CHOICE)
    vote_demoday = models.BooleanField(default=False)
    vote_part = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'name', 'part', 'team']
    objects = CustomUserManager()

    def __str__(self):
        return f'{self.name} ({self.part})'
