from django.contrib import admin
from prc_mdl_app.models import Price


# Register your models here.
@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display  = ('distance_base_price', 'distance_additional_price', 'time_multiplier_factor', 'waiting_charge',
                 'created_at', 'updated_at', 'updated_by')
