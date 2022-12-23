from rest_framework import serializers

from partleads.models import Candidate


class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        read_only_fields = ['name', 'vote_count', 'position']
        model = Candidate
        fields = ['id', 'name', 'vote_count', 'position']