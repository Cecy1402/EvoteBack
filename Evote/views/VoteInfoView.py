from rest_framework import viewsets
from ..models import VoteInfo
from ..serializers import VoteInfoSerializer
from django_filters.rest_framework import DjangoFilterBackend


class VoteInfoViewSet(viewsets.ModelViewSet):
    queryset = VoteInfo.objects.filter(status="1")
    serializer_class = VoteInfoSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('period',)
