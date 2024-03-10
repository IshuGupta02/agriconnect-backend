from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from agri.models.personae.authority import Authority
from agri.models.personae.farmer import Farmer
from agri.models.personae.person import Person
from agri.serializers.personae.person import PersonSerializer
from agri.serializers.personae.authority import AuthoritySerializer
from agri.serializers.personae.farmer import FarmerSerializer
from rest_framework import status

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def perform_create(self, serializer):
        # Hash the password before saving the person
        password = self.request.data.get('password')
        person = serializer.save()
        person.set_password(password)
        person.save()

    @action(detail=False, methods=['post'])
    def get_person_id_from_token(self, request):
        token = request.data.get('token')

        if not token:
            return Response({'error': 'Token parameter is required'}, status=status.HTTP_400_BAD_REQUEST)

        User = Person

        try:
            user = User.objects.get(auth_token__key=token)
        except User.DoesNotExist:
            return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)

        person_id = user.id

        return Response({'person_id': person_id}, status=status.HTTP_200_OK)

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