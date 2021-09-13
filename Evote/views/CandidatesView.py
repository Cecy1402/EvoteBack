from rest_framework import viewsets
from ..models import Candidate
from ..serializers import CandidateSerializer

class CandidatesViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.filter(status = "1")
    serializer_class = CandidateSerializer
