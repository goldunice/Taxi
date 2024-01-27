from django.db import models
from users.models import CustomUser
from drivers.models import Driver


class Operator(CustomUser):
    first_name = None
    last_name = None
    is_staff = None
    is_superuser = None
    email = None
    fullname = models.CharField(max_length=255)
    work_time = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name_plural = 'Operator'


class Client(models.Model):
    phone = models.CharField(max_length=255)
    total_bonus = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.phone

    class Meta:
        verbose_name_plural = 'Client'


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True, blank=True)
    total_sum = models.PositiveIntegerField(default=0)
    baggage = models.BooleanField(default=False)
    for_women = models.BooleanField(default=False)
    status = models.CharField(max_length=255, choices=(("active", "active"), ("olindi", "olindi"),
                                                       ("boshlandi", "boshlandi"), ("yakunlandi", "yakunlandi"),
                                                       ("bekor qilindi", "bekor qilindi")))
    starting_point = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    izoh = models.CharField(max_length=255, blank=True, null=True)
    grade = models.PositiveSmallIntegerField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    waiting_seconds = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.client.phone}"

    class Meta:
        verbose_name_plural = 'Order'
