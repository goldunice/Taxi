from django.contrib import admin
from .models import Operator, Client, Order


@admin.register(Operator)
class OperatorAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'work_time', 'phone')
    search_fields = ('fullname', 'work_time', 'phone')


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('phone', 'total_bonus')
    search_fields = ('phone',)
    list_editable = ('total_bonus',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'client', 'driver', 'total_sum', 'baggage', 'for_women', 'status', 'starting_point', 'destination', 'date',
        'waiting_seconds')
    search_fields = ('client__phone', 'driver__fullname', 'starting_point', 'destination')
    list_filter = ('status',)
    date_hierarchy = 'date'
