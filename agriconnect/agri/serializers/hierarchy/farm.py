# serializers.py
from rest_framework import serializers
from agri.models.hierarchy.farm import Farm

class FarmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farm
        fields = '__all__'
