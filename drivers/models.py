from django.db import models
from django.contrib.auth.models import AbstractUser
from users.models import CustomUser


class CarCategory(models.Model):
    type = models.CharField(max_length=255)
    minimum = models.PositiveIntegerField()
    summa_per_km = models.PositiveIntegerField()
    waiting_cost = models.PositiveIntegerField()
    baggage_cost = models.PositiveIntegerField()
    firm_percent = models.PositiveSmallIntegerField()
    bonus_percent = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name_plural = 'Car Category'

    def __str__(self):
        return self.type


class Driver(CustomUser):
    first_name = None
    last_name = None
    is_staff = None
    is_superuser = None
    fullname = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    gender = models.CharField(max_length=255, default="Erkak")
    photo = models.FileField(upload_to="drivers/", blank=True, null=True)
    birth_date = models.DateField()
    car_type = models.CharField(max_length=255)
    car_number = models.CharField(max_length=255)
    sms_code = models.CharField(max_length=255, blank=True)
    balance = models.PositiveIntegerField(default=0)
    has_baggage = models.BooleanField(default=True)
    confirmed = models.BooleanField(default=False)
    category = models.ForeignKey(CarCategory, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Driver'

    def __str__(self):
        return self.fullname
