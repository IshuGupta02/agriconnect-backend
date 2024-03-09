# views.py
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from agri.models.personae.authority import Authority
from agri.models.personae.person import Person
from agri.serializers.personae.authority import AuthoritySerializer
from rest_framework.permissions import IsAuthenticated

class AuthorityViewSet(viewsets.ModelViewSet):
    queryset = Authority.objects.all()
    serializer_class = AuthoritySerializer
    # permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Get the currently logged-in user (assuming you are using TokenAuthentication)
        authority_id = self.request.data.get('authority_id')
        person_id = self.request.data.get('person_id')
        user = self.request.user

        try:
            person = Person.objects.get(id = person_id)
        except:
            return Response({"detail": "Invalid person ID."}, status=status.HTTP_403_FORBIDDEN)
        
        # Create a new Authority linked to the logged-in user
        authority = serializer.save(person=person)

        # Set the 'report_to' field to the Authority creating this Authority
        try:
            authority_creator = Authority.objects.get(person=user, id=authority_id)
        except Authority.DoesNotExist:
            # Handle the case where the user is not an authority
            return Response({"detail": "You are not authorized to create such authorities."}, status=status.HTTP_403_FORBIDDEN)
        
        authority.report_to = authority_creator
        authority.save()

    def get_queryset(self):
        # Only allow authorities to see their own records
        user = self.request.user
        print(user)
        return Authority.objects.filter(person=user)
