from rest_framework import viewsets
from agri.models.personae.person import Person
from agri.serializers.personae.person import PersonSerializer

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def perform_create(self, serializer):
        # Hash the password before saving the person
        password = self.request.data.get('password')
        person = serializer.save()
        person.set_password(password)
        person.save()