from rest_framework import viewsets, status
from ..models import Period, VoteInfo
from ..serializers import PeriodSerializer
from rest_framework.response import Response
from rest_framework import filters


class PeriodViewSet(viewsets.ModelViewSet):
    queryset = Period.objects.filter(status="1")
    serializer_class = PeriodSerializer
    filter_backends = (filters.SearchFilter, )
    search_fields = ['startYear', 'endYear']

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid()
        serializer.save()
        data = serializer.data
        period = Period.objects.get(id=data['id'])
        VoteInfo.objects.create(period=period, whiteVotes=0, nullVotes=0)

        return Response(data, status=status.HTTP_201_CREATED)
