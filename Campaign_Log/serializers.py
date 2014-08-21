from rest_framework import serializers
from django.contrib.auth.models import User
from Campaign_Log.models import Campaign, Log, Character, Location


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id','username', 'email')
        # campaigns = CampaignSerializer(many=True)

class LogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Log
        fields = ('id','created', 'title', 'content')


class CharacterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Character
        fields = ('id', 'name', 'description', 'assosiatedLocation')

class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'name', 'description', 'locationType')

class CampaignSerializer(serializers.HyperlinkedModelSerializer):
    logs = LogSerializer(many=True)
    characters = CharacterSerializer(many=True)
    locations = LocationSerializer(many=True)
    # users = UserSerializer(many=True)

    class Meta:
        model = Campaign
        fields = ('id', 'title', 'logs', 'characters', 'locations')
