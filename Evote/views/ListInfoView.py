from rest_framework import status, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import F

from ..models import ListInfo, VoteInfo, Period, VoteStudent, Candidate
from ..serializers import ListInfoSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth import get_user_model
from rest_framework import filters
User = get_user_model()


class ListInfoViewSet(viewsets.ModelViewSet):
    queryset = ListInfo.objects.filter(status="1")
    serializer_class = ListInfoSerializer
    # filters
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filter_fields = ('period',)
    search_fields = ['name', 'slogan', ]

    def create(self, request, *args, **kwargs):
        candidates = request.data.pop('candidate_set')
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        listInfo = ListInfo.objects.get(id=serializer.data['id'])
        for candidate in candidates:
            candidate.pop('course')
            candidate.pop('degree')
            candidate.pop('name')
            user_id = candidate.pop('student')

            user_instance = User.objects.get(identificacion=user_id)

            candidate['listInfo'] = listInfo
            candidate['student'] = user_instance
            print("WTF", candidate)

            c = Candidate(**candidate)
            c.save()
        # candidates_serializer = CandidateSerializer(data=candidates, many=True)
        # candidates_serializer.is_valid(raise_exception=True)
        # candidates_serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        candidates = request.data.pop('candidate_set')
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        for candidate in candidates:
            if "id" in candidate:
                if candidate['id'] is not None:
                    c = Candidate.objects.get(id=candidate['id'])
                    user_instance = User.objects.get(
                        identificacion=candidate['student'])
                    listInfo = ListInfo.objects.get(
                        id=candidate['listInfo']['id'])
                    c.student = user_instance
                    c.position = candidate['position']
                    c.listInfo = listInfo
                    c.foto = candidate['foto']

                    c.save()
        serializer.save()
        return Response(serializer.data)

    def get_response(self, status, code, dev, user):
        data = {}
        data['status'] = status
        data['code'] = code
        data['dev_message'] = dev
        data['user_message'] = user
        return data

    def save_vote(self, list_id):
        try:
            list_info = self.get_queryset().get(id=list_id)
            list_info.votes = F('votes') + 1
            list_info.save()

            return self.get_response(
                "Authorized",
                "001",
                "Vote saved successfully",
                "Voto guardato correctamente"
            )
        except ListInfo.DoesNotExist:
            return self.get_response(
                "Error",
                "002",
                "The list was not found in the database",
                "Lo sentimos no pudimos procesar su voto, comuniquese con el administrador"
            )

    def save_invalid_vote(self, period, is_null_vote, is_white_vote):
        try:
            vote_info = VoteInfo.objects.get(period=period)

            if is_null_vote:
                vote_info.nullVotes = F('nullVotes') + 1
            elif is_white_vote:
                vote_info.whiteVotes = F('whiteVotes') + 1
            else:
                return self.get_response(
                    "Error",
                    "002",
                    "The null_vote or white_vote is None",
                    "Lo sentimos no pudimos procesar su voto, comuniquese con el administrador"
                )

            vote_info.save()
            return self.get_response(
                "Authorized",
                "001",
                "Vote saved successfully",
                "Voto guardado correctamente"
            )
        except VoteInfo.DoesNotExist:
            return self.get_response(
                "Error",
                "002",
                "The VoteInfo was not found in the database",
                "Lo sentimos no pudimos procesar su voto, comuniquese con el administrador"
            )

    def save_vote_student(self, period, student):
        VoteStudent.objects.create(period=period, student=student)

    @action(detail=False, methods=['post'])
    def vote_for_list(self, request):
        """Add a new vote to the list by your ID """
        list_id = request.data.get("list_id", None)
        is_null_vote = request.data.get("null_vote", None)
        is_white_vote = request.data.get("white_vote", None)
        student_id = request.data.get("student", None)

        period = Period.objects.get(periodPresent=True)
        response = {}

        try:
            if student_id is not None:
                student = User.objects.get(identificacion=student_id)

                if list_id is not None:
                    response = self.save_vote(list_id)
                else:
                    response = self.save_invalid_vote(
                        period, is_null_vote, is_white_vote)
                if response['code'] == "002":
                    pass
                else:
                    self.save_vote_student(period, student)
            else:
                response = self.get_response(
                    "Error",
                    "002",
                    "the Student is None",
                    "Lo sentimos no pudimos procesar su voto, comuniquese con el administrador"
                )

        except User.DoesNotExist:
            response = self.get_response(
                "Error",
                "002",
                "Usuario no exite",
                "Lo sentimos no pudimos procesar su voto, comuniquese con el administrador"
            )

        return Response(response, status=status.HTTP_200_OK)

    def perform_destroy(self, instance):
        """Disable List."""
        instance.status = '0'
        instance.save()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        data = {
            'status': "Autorizado",
            'message': "Lista de Candidatos eliminada con exito"
        }
        return Response(data, status=status.HTTP_200_OK)
