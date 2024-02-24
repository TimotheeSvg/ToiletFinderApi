from django.views.generic import View
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest

class ToiletView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('This is GET request')