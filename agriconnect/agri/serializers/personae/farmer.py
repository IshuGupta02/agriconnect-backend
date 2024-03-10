# serializers.py
from rest_framework import serializers
from agri.models.personae.farmer import Farmer

class FarmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmer
        fields = '__all__'