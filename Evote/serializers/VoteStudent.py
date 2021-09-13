from rest_framework import serializers
from ..models import VoteStudent


class VoteStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = VoteStudent
        fields = '__all__'
        depth = 1
