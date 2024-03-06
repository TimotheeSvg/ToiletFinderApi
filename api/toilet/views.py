from django.views.generic import View
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from toilet.models import Toilet, ToiletSerializer

def verify_params(key, params):
    return key in params and len(params[key]) > 0 and params[key][0]

class ToiletView(View):
    def get(self, request, *args, **kwargs):
        paramsRequest = request.GET

        paramsSql = {}
        print(paramsRequest)

        if verify_params('latitude', paramsRequest):
            paramsSql['toiletLatitude'] = float(paramsRequest['latitude'])

        if verify_params('longitude', paramsRequest):
            paramsSql['toiletLongitude'] = float(paramsRequest['longitude'])

        if verify_params('country', paramsRequest):
            paramsSql['toiletCountry'] = paramsRequest['country']

        if verify_params('name', paramsRequest):
            paramsSql['toiletName__contains'] = paramsRequest['name']

        if verify_params('city', paramsRequest):
            paramsSql['toiletCity'] = paramsRequest['city']

        toilets = Toilet.objects.filter(**paramsSql)
        toiletSeria = ToiletSerializer(toilets, many=True)

        return JsonResponse(toiletSeria.data, safe=False)


class index(View):
    def get(self, request):
        return HttpResponse("Up")