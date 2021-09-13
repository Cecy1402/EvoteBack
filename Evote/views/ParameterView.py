from rest_framework import viewsets
from ..models import Parameter
from ..serializers import ParameterSerializer

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated
)

class ParameterViewSet(viewsets.ModelViewSet):
    queryset = Parameter.objects.filter(status = "1")
    serializer_class = ParameterSerializer


    def get_permissions(self):
        """Assign permissions based on action."""
        if self.action in ['list', ]:
            permissions = [AllowAny]
        else:
            permissions = [IsAuthenticated]
        return [p() for p in permissions]