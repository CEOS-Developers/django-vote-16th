from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.
from accounts.models import User
from demoday.models import Team
from demoday.serializer import TeamSerializer


class TeamView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        teams = Team.objects.all()
        serializer = TeamSerializer(teams, many=True)
        return Response(serializer.data)

    def post(self, request):
        user = User.objects.filter(id=request.user.id)[0]

        # if user.vote_demoday:
        #     return Response({'Message': 'No more vote count'}, status=status.HTTP_400_BAD_REQUEST)

        if(request.data['team_name'] == request.user.team):
            return Response({'Message': 'You are not allowed to vote on your own team'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid():
            team = get_object_or_404(Team, team_name=serializer.data['team_name'])
            team.vote_count += 1
            team.save()
            serializer = TeamSerializer(team)
            # user.vote_demoday = True
            # user.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'Message': 'Team not found'}, status=status.HTTP_404_NOT_FOUND)