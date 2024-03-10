# views.py
from rest_framework import viewsets
from agri.models.personae.farmer import Farmer
from agri.serializers.personae.farmer import FarmerSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

class FarmerViewSet(viewsets.ModelViewSet):
    queryset = Farmer.objects.all()
    serializer_class = FarmerSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        # Override create to set the person field based on the current user
        user = self.request.user
        data = request.data.copy()
        data['person'] = user.id  # Set the person field to the current user's ID
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)