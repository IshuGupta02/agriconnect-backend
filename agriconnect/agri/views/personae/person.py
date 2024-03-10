from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from agri.models.personae.authority import Authority
from agri.models.personae.farmer import Farmer
from agri.models.personae.person import Person
from agri.serializers.personae.person import PersonSerializer
from agri.serializers.personae.authority import AuthoritySerializer
from agri.serializers.personae.farmer import FarmerSerializer

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def perform_create(self, serializer):
        # Hash the password before saving the person
        password = self.request.data.get('password')
        person = serializer.save()
        person.set_password(password)
        person.save()

    @action(detail=True, methods=['get'])
    def get_authorities_and_farmers(self, request, pk=None):
        person = self.get_object()
        authorities = Authority.objects.filter(person=person)
        farmers = Farmer.objects.filter(person=person)

        authority_serializer = AuthoritySerializer(authorities, many=True)
        farmer_serializer = FarmerSerializer(farmers, many=True)

        print("Hey")

        data = {
            'authorities': authority_serializer.data,
            'farmers': farmer_serializer.data,
        }

        return Response(data)