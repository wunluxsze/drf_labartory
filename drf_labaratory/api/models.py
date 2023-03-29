from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin, AbstractBaseUser


# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=200)
    lang = models.CharField(max_length=200)


class Exscursion(models.Model):
    name = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    time = models.TimeField()
    price = models.IntegerField()


class Tour(models.Model):
    LIVE_TIME = (
        ('1 неделя', '1 неделя'),
        ('2 недели', '2 недели'),
        ('3 недели', '3 неделя')
    )

    SERVICE = (
        ('все включено', 'все включено'),
        ('нет', 'нет'),
    )

    STARS = (
        ('1 Звезда', '1 Звезда'),
        ('2 Звезды', '2 Звезды'),
        ('3 Звезды', '3 Звезды')
    )
    name = models.CharField(max_length=200)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    live_time = models.CharField(max_length=200, choices=LIVE_TIME)
    service = models.CharField(max_length=50)
    counts = models.IntegerField()
    stars = models.CharField(max_length=50, choices=STARS)
    excursion = models.ForeignKey(Exscursion, on_delete=models.CASCADE)
    price = models.IntegerField()


class Profile(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    price = models.IntegerField()
    time = models.TimeField()
    user = models.ForeignKey("User", on_delete=models.CASCADE)


class MyUserManager(BaseUserManager):
    def _create_user(self, email, username, password, **extra_fields):
        if not email:
            raise ValueError("Вы не ввели Email")
        if not username:
            raise ValueError("Вы не ввели Логин")
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, email, username, password):
        return self._create_user(email, username, password)

    def create_superuser(self, email, username, password):
        return self._create_user(email, username, password, is_staff=True, is_superuser=True)


class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True, unique=True)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = MyUserManager()

    def __str__(self):
        return self.email
