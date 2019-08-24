from rest_framework import serializers

from newApp.models import Reservation


class ReservationSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True, max_length=200)
    email = serializers.EmailField(required=True, max_length=200)
    phone = serializers.CharField(required=True, max_length=200)
    description = serializers.CharField(required=False, max_length=500)
    date = serializers.CharField(required=True, max_length=20)
    time = serializers.CharField(required=True, max_length=10)

    class Meta:
        model = Reservation
        fields = ('name', 'email', 'phone', 'date', 'time', 'description')

    def create(self, validated_data):
        return Reservation.objects.create(**validated_data)