# Create your views here.
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from newApp.serializers import ReservationSerializer


def index(request):
    return render(request, template_name='index.html', context={})


class MakeReservation(APIView):
    def post(self, request):
        serializer = ReservationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("ok")
