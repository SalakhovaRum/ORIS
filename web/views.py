
from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from web.models import Orders


# Create your views here.

class MainView(APIView):
    def get(self, request):
        return Response({'Хорошо?': 'Хорошо'})


class OrderView(APIView):
    def get(self, request):
        orders_obj = Orders.objects.get(thing=1)
        return Response(model_to_dict(orders_obj))

    def post(self, request):
        orders_obj = Orders.objects.get(thing=1)
        if request.data:
            orders_obj = request.data['count']
        else:
            orders_obj.count += 1
        orders_obj.save()

        return Response(model_to_dict(orders_obj))