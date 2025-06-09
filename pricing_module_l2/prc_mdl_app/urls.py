from django.urls import path
from .views import rederHome, calculatePrice, updatePriceConfig, deletePriceConfig, disablePriceConfig, \
    renderPriceCalculator

urlpatterns = [
    path('home/', rederHome, name='rederHome'),
    path('price-calculator/', renderPriceCalculator, name='renderPriceCalculator'),
    path("update-config/", updatePriceConfig, name='updatePriceConfig'),
    path("disable-config/<id>", disablePriceConfig, name='disablePriceConfig'),
    path("delete-config/<id>", deletePriceConfig, name='deletePriceConfig'),
    path('v1/', calculatePrice, name='calculatePrice')
]
