# serializers.py
from rest_framework import serializers
from agri.models.personae.person import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'mobile')
        extra_kwargs = {'password': {'write_only': True}}