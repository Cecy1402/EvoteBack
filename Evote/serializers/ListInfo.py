from rest_framework import serializers
from ..models import ListInfo
from ..serializers import CandidateSerializer
class ListInfoSerializer(serializers.ModelSerializer):
    candidate_set = CandidateSerializer(many=True, read_only=True)

    class Meta:
        model = ListInfo
        fields = ("id", "name", "number", "slogan",
                  "period", "created", "votes","foto" ,"candidate_set")

