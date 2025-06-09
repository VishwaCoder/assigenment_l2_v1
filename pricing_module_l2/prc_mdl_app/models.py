from django.db import models
from django.utils import timezone


# Create your models here.
class Price(models.Model):
    distance_base_price = models.IntegerField()
    distance_additional_price = models.IntegerField()
    time_multiplier_factor = models.FloatField()
    waiting_charge = models.IntegerField()
    is_enabled = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.EmailField(max_length=225, default="asus.gmail.com")
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.EmailField(max_length=225, blank=True, null=True)
