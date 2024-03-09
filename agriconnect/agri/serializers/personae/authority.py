from rest_framework import serializers
from agri.models.personae.authority import Authority

class AuthoritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Authority
        fields = ('id', 'person', 'report_to', 'farms')