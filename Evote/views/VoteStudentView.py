from Evote.models.CandidatesModel import User
from rest_framework import viewsets, status
from ..models import VoteStudent, Period
from ..serializers import VoteStudentSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated
)
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend

User = get_user_model()
class VoteStudentViewSet(viewsets.ModelViewSet):
    queryset = VoteStudent.objects.filter(status="1")
    serializer_class = VoteStudentSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('period',)


    def get_permissions(self):
        """Assign permissions based on action."""
        if self.action in ['ya_voto', ]:
            permissions = [AllowAny]
        elif self.action in ['retrieve', 'update', 'partial_update', ]:
            permissions = [IsAuthenticated]
        else:
            permissions = [IsAuthenticated]
        return [p() for p in permissions]

    @action(detail=False, methods=['post'])
    def ya_voto(self, request):
        id_student = request.data.get("id", None)
        id_period = Period.objects.get(periodPresent=True)
        try:
            student = User.objects.get(identificacion= id_student)
            vote = VoteStudent.objects.get(student=student, period=id_period)
            data = {
                'vote': True,
                'code': vote.id
            }

        except ObjectDoesNotExist:

            data = {
                'vote': False
            }

        return Response(data, status=status.HTTP_200_OK)
