from django.contrib.auth import get_user_model
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated
)
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework import mixins, status, viewsets
# from apps_com_teedii_core.users.serializers import UserSerializer
from django_filters.rest_framework import DjangoFilterBackend

from ..serializers import (
    UserSerializer,
    UserLoginSerializer

)


# models

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):

    serializer_class = UserSerializer
    queryset = User.objects.all()

    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('identificacion',)

    def get_permissions(self):
        """Assign permissions based on action."""
        if self.action in ['login', ]:
            permissions = [AllowAny]
        elif self.action in ['retrieve', 'update', 'partial_update', ]:
            permissions = [IsAuthenticated]
        else:
            permissions = [IsAuthenticated]
        return [p() for p in permissions]

    @action(detail=False, methods=['post'])
    def login(self, request):
        """User sign in."""

        serializer = UserLoginSerializer(data=request.data)

        is_valid = serializer.is_valid()

        # un jemplo se puede mejorar esto
        # https://stackoverflow.com/questions/29731013/django-rest-framework-cannot-call-is-valid-as-no-data-keyword-argument/29731923
        if(is_valid):

            user, token = serializer.save()
            user = UserSerializer(user).data

            data = {
                'user': user,
                'access_token': token
            }

        else:
            data = {
                'error': '001',
                'message': 'Usuario o contraseña incorrecto'
            }

        return Response(data, status=status.HTTP_201_CREATED)
