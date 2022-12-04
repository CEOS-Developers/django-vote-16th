from rest_framework import serializers

from demoday.models import Team


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['team_name', 'vote_count']