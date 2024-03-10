# serializers.py
from rest_framework import serializers
from agri.models.personae.person import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'username', 'mobile', 'name', 'id_card_type', 'id_card_number', 'verified')
        extra_kwargs = {'password': {'write_only': True}}
