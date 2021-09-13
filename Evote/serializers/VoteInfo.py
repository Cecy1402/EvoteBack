from rest_framework import serializers
from ..models import VoteInfo


class VoteInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = VoteInfo
        fields = '__all__'
