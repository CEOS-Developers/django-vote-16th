from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models import User
from partleads.models import Candidate
from partleads.serializer import CandidateSerializer

POSITION_DICT = {
    'Backend': 'BE',
    'Frontend': 'FE'
}

class CandidateView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        candidates = Candidate.objects.all()
        serializer = CandidateSerializer(candidates, many=True)
        return Response(serializer.data)

    def post(self, request):
        user = User.objects.filter(id=request.user.id)[0]

        # if(user.vote_part):
        #     return Response({'Message': 'No more vote count'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = CandidateSerializer(data=request.data)
        if(serializer.is_valid()):

            candidate = get_object_or_404(Candidate, id=request.data['id'])

            if (POSITION_DICT[request.user.part] != candidate.position):
                return Response({'Message': "You can only vote on the candidates from your part"},
                                status=status.HTTP_400_BAD_REQUEST)

            candidate.vote_count += 1
            candidate.save()
            serializer = CandidateSerializer(candidate)
            # user.vote_part = True
            # user.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response({'Message': 'Candidate not found'}, status=status.HTTP_404_NOT_FOUND)