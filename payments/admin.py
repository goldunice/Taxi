from django.contrib import admin
from .models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('driver', 'operator', 'date', 'amount', 'type')
    search_fields = ('driver__fullname', 'operator__fullname', 'type')
    list_filter = ('type',)
    date_hierarchy = 'date'
