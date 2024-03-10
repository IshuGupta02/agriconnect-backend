# views.py
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from agri.models.personae.authority import Authority
from agri.models.personae.person import Person
from agri.serializers.personae.authority import AuthoritySerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action

import uuid

def generate_unique_referral_code():
    return str(uuid.uuid4().hex)[:20].upper()

class AuthorityViewSet(viewsets.ModelViewSet):
    queryset = Authority.objects.all()
    serializer_class = AuthoritySerializer
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

    def perform_create(self, serializer):
        user = self.request.user
        referral_code = self.request.data.get('referral_code')  # Get referral code from request data
        if referral_code:
            referred_authority = Authority.objects.filter(referral_code=referral_code).first()
            if referred_authority:
                serializer.save(person=user, report_to=referred_authority)
            else:
                return Response({'error': 'Referred authority not found'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Referral code not found'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'])
    def generate_referral_code(self, request):
        user = request.user
        authority = Authority.objects.get(person=user)
        
        if not authority.referral_code:
            referral_code = generate_unique_referral_code()
            authority.referral_code = referral_code
            authority.save()

            return Response({'referral_code': referral_code}, status=status.HTTP_200_OK)
        else:
            return Response({'referral_code': authority.referral_code}, status=status.HTTP_200_OK)
        
    def get_queryset(self):
        # Only allow authorities to see their own records
        user = self.request.user
        return Authority.objects.filter(person=user)
