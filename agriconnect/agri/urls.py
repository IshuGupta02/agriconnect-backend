from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from agri.views.personae.person import PersonViewSet
from rest_framework.authtoken.views import obtain_auth_token
from agri.views.personae.authority import AuthorityViewSet
from agri.views.personae.farmer import FarmerViewSet

router = routers.DefaultRouter()
router.register(r'person', PersonViewSet)
router.register(r'authorities', AuthorityViewSet)
router.register(r'farmers', FarmerViewSet, basename='farmer')

urlpatterns = [
    path('', include(router.urls)),
    path('agri-token-auth/', obtain_auth_token, name='api_token_auth'),
]