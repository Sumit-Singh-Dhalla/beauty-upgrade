# Create your views here.
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.template.loader import render_to_string

from newApp.models import Offer, Gallery
from newApp.serializers import ReservationSerializer


class IndexViewSet(APIView):
    def get(self, request):
        images_qs = Gallery.objects.all()
        return render(request, template_name='index.html', context={'images_qs': images_qs})


class MakeReservation(APIView):
    def post(self, request):
        serializer = ReservationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("ok")


class OfferViewSet(APIView):
    def get(self, request):
        offer_qs = Offer.objects.filter(is_active=True)
        data = render_to_string('offer_table.html', {'offer_qs': offer_qs})
        return Response(data)