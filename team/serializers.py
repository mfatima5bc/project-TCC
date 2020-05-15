from rest_framework import serializers

from .models import Team, Membership
from account.models import CustomUser
from account.serializers import CustomUserSerializer

class TeamSerializer(serializers.ModelSerializer):
    members = serializers.StringRelatedField(many=True)

    class Meta:
        model = Team
        fields = [
            'name',
            'members'
        ]

class MembershipSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=True)
    team = serializers.StringRelatedField(many=True)

    class Meta:
        model = Membership
        fields = [
            'team',
            'user'
        ]
        