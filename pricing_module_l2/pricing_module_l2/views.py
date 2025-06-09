from django.http import HttpResponse


def index(req):
    return HttpResponse("Landing index page !")