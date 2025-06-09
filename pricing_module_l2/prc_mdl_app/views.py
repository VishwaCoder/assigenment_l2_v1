import json
from datetime import datetime

from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from prc_mdl_app.models import Price


# Create your views here

def rederHome(req):
    try:
        raw_data = Price.objects.all()
        conf_data = json.loads(serializers.serialize("json", raw_data))
        final_payload = []
        for config in conf_data:
            final_payload.append(
                {
                    'key': config['pk'],
                    'distance_base_price': config['fields']['distance_base_price'],
                    'distance_additional_price': config['fields']['distance_additional_price'],
                    'time_multiplier_factor': config['fields']['time_multiplier_factor'],
                    'waiting_charge': config['fields']['waiting_charge'],
                    'is_enabled': "Enabled" if config['fields']['is_enabled'] == True else "Disabled",
                    'created_at': config['fields']['created_at'],
                    'created_by': config['fields']['created_by'],
                    'updated_at': config['fields']['updated_at'] if config['fields'][
                                                                        'updated_at'] is not None else "NA",
                    'updated_by': config['fields']['updated_by'] if config['fields']['updated_by'] is not None else "NA"
                }
            )
        return render(request=req, template_name='prc_mdl_app/index.html', context={'config_list': final_payload})
    except Exception as e:
        return HttpResponse(f"Server error {str(e)}")


def updatePriceConfig(req):
    try:
        if req.method == "POST":
            key = req.POST.get("key")
            distance_base_price = req.POST.get("distance_base_price")
            distance_additional_price = req.POST.get("distance_additional_price")
            time_multiplier_factor = req.POST.get("time_multiplier_factor")
            waiting_charge = req.POST.get("waiting_charge")
            updated_at = datetime.now()
            updated_by = req.user.email

            target_obj = Price.objects.get(pk=int(key))
            target_obj.distance_base_price = distance_base_price
            target_obj.distance_additional_price = distance_additional_price
            target_obj.time_multiplier_factor = time_multiplier_factor
            target_obj.waiting_charge = waiting_charge
            target_obj.updated_by = updated_by
            target_obj.updated_at = updated_at
            target_obj.save()
            return redirect("rederHome")
        return HttpResponse("Method not allowed !")
    except Exception as e:
        return HttpResponse(f"Server error {str(e)}")


def disablePriceConfig(req, id):
    try:
        if req.method == "GET":
            updated_at = datetime.now()
            updated_by = req.user.email

            target_obj = Price.objects.get(pk=int(id))
            target_obj.is_enabled = False if target_obj.is_enabled == True else True
            target_obj.updated_by = updated_by
            target_obj.updated_at = updated_at
            target_obj.save()
            return redirect("rederHome")
        return HttpResponse("Method not allowed !")
    except Exception as e:
        return HttpResponse(f"Server error {str(e)}")


def deletePriceConfig(req, id):
    try:
        if req.method == "GET":
            target_obj = Price.objects.get(pk=int(id))
            target_obj.delete()
            return redirect("rederHome")
        return HttpResponse("Method not allowed !")
    except Exception as e:
        return HttpResponse(f"Server error {str(e)}")


def renderPriceCalculator(req):
    return render(request=req, template_name='prc_mdl_app/price_calculator.html')


@csrf_exempt
def calculatePrice(req):
    try:
        if req.method == "POST":
            body = json.loads(req.body.decode("utf-8"))
            distance_traveled = float(body.get("distance_traveled"))
            time_duration = float(body.get("time_duration"))
            active_config = Price.objects.get(is_enabled=True)

            if active_config:
                price = (int(active_config.distance_base_price) + (
                        distance_traveled * int(active_config.distance_additional_price))) + (
                                time_duration * float(active_config.time_multiplier_factor)) + int(
                    active_config.waiting_charge)

                return JsonResponse({"total_price": price}, status=200)
            return JsonResponse({"message": "No active configuration found"}, status=404)
        return JsonResponse({"message": "Method not allowed"}, status=400)
    except Exception as e:
        return JsonResponse({"message": f"Server error {str(e)}"}, status=500)
