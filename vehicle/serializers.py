# vehicle/serializers.py
from rest_framework import serializers
from .models import Vehicle, History

class VehicleSerializer(serializers.ModelSerializer):
    last_parking = serializers.SerializerMethodField()
    class Meta:
        model = Vehicle
        fields = ('id', 'name', 'number', 'user','last_parking')

    def get_last_parking(self,obj):
        history = History.objects.filter(vehicle=obj)
        if history:
            return VehicleHistorySerializer(history[len(history)-1],many=False).data

class VehicleHistorySerializer(serializers.ModelSerializer):
    time_duration = serializers.SerializerMethodField()
    class Meta:
        model = History
        fields = "__all__"

    def get_time_duration(self,old):
        return old.slot.time_duration