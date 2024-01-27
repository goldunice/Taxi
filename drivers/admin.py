from django.contrib import admin
from django.utils.html import format_html

from .models import CarCategory, Driver


@admin.register(CarCategory)
class CarCategoryAdmin(admin.ModelAdmin):
    list_display = ('type', 'minimum', 'summa_per_km', 'waiting_cost', 'baggage_cost', 'firm_percent', 'bonus_percent')
    search_fields = ('type',)


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = (
        'fullname', 'phone', 'gender', 'photo_display', 'birth_date', 'car_type', 'car_number', 'sms_code', 'balance',
        'has_baggage', 'confirmed', 'category', 'created_at')
    search_fields = ('fullname', 'phone', 'car_number')
    list_filter = ('gender', 'has_baggage', 'confirmed', 'category', 'created_at')
    date_hierarchy = 'created_at'

    def photo_display(self, obj):
        return format_html('<img src="{}" height="50" />', obj.photo.url) if obj.photo else 'N/A'

    photo_display.short_description = 'Photo'
