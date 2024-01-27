from django.db import models
from drivers.models import *
from operators.models import *


class Payment(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True)
    operator = models.ForeignKey(Operator, on_delete=models.SET_NULL, null=True)
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)
    amount = models.PositiveIntegerField(default=0)
    type = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.operator} - {self.driver}"

    class Meta:
        verbose_name_plural = 'Payment'
