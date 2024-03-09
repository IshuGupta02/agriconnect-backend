from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from agri.views.personae.person import PersonViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'person', PersonViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('agri-token-auth/', obtain_auth_token, name='api_token_auth'),
    # path('check/', check, name='check_login'),
    # path('success/', success, name='success'),
]