import re
from datetime import datetime

from django.conf import settings
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from setuptools._entry_points import _


def get_default_date():
    return datetime(day=1, month=1, year=1970)


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True, help_text="email address")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def save(self, *args, **kwargs):
        self.full_clean()

        has_is_superuser = CustomUser.objects.filter(
            is_superuser=True
        ).exists()

        if has_is_superuser and self.is_superuser:
            return None

        current_password = self.password
        hashed_password_pattern = self.__get_hashed_pattern()

        if not re.fullmatch(hashed_password_pattern, current_password):
            self.set_password(current_password)

        self.is_staff = False
        super().save(*args, **kwargs)

    def __get_hashed_pattern(self):
        current_hash_algorithm = settings.PASSWORD_HASHERS[0]

        if 'PBKDF2PasswordHasher' in current_hash_algorithm:
            return r'\w+[$]\d+[$]\w+[$].+'

        if 'MD5PasswordHasher' in current_hash_algorithm:
            return r'\w+[$]\w+[$].+'

    def delete(self, *args, **kwargs):
        if self.is_superuser:
            return None

        super().delete(*args, **kwargs)


class Patient(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=512, help_text='Имя')
    last_name = models.CharField(max_length=512, help_text='Фамилия')
    middle_name = models.CharField(max_length=512, help_text='Отчество')
    date_of_birth = models.DateField(default=get_default_date,
                                     help_text='Дата пождения')
    pol = models.CharField(max_length=64, help_text='Пол')
    image = models.ImageField(upload_to='patients/%Y/%m/%d/',
                              default=None, null=True, blank=True,
                              help_text='Изображение профиля')


class Category(models.Model):
    name = models.CharField(max_length=512, help_text='Название категории')


class Analysis(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=512, help_text='Название услуги')
    description = models.CharField(max_length=512, help_text='Описание услуги')
    price = models.DecimalField(max_digits=10, decimal_places=2,
                                help_text='Цена услуги')
    time_result = models.CharField(max_length=128,
                                   help_text='Время выполнения')
    preparation = models.CharField(max_length=512,
                                   help_text='Необходимая подготовка')
    bio = models.CharField(max_length=512, help_text='БИО материал')


class New(models.Model):
    analysis = models.ForeignKey(Analysis, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='news/%Y/%m/%d/')


class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    address = models.CharField(max_length=512, help_text='Адрес')
    date_time = models.DateField(default=timezone.now,
                                 help_text='Удобная дата')
    phone = models.CharField(max_length=12, help_text='Телефон для связи')
    comment = models.CharField(max_length=512, help_text='Комментарий')
    audio_comment = models.FileField(upload_to='audio/%Y/%m/%d/',
                                     default=True, null=True, blank=True,
                                     help_text='Аудио комментарий')


class PatientInOrder(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE,
                              related_name='patients')

    class Meta:
        unique_together = (
            ('patient', 'order',),
        )


class AnalysisInPatient(models.Model):
    patient_in_order = models.ForeignKey(PatientInOrder,
                                         on_delete=models.CASCADE,
                                         related_name='analysises')
    analysis = models.ForeignKey(Analysis, on_delete=models.CASCADE)

    class Meta:
        unique_together = (
            ('patient_in_order', 'analysis',),
        )
