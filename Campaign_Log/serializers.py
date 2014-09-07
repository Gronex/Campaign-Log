from rest_framework import serializers
from django.contrib.auth.models import User
from Campaign_Log.models import Campaign, Log, Character, Location


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id','username', 'email')
        # campaigns = CampaignSerializer(many=True)

class LogSerializer(serializers.HyperlinkedModelSerializer):
    campaign = serializers.HyperlinkedRelatedField(read_only=False, view_name='api-campaign-instance')
    class Meta:
        model = Log
        fields = ('campaign','created', 'title', 'content')

class CharacterSerializer(serializers.HyperlinkedModelSerializer):
    campaign = serializers.HyperlinkedRelatedField(read_only=False, view_name='api-campaign-instance')
    assosiatedLocation = serializers.HyperlinkedRelatedField(read_only=False, view_name='api-location-instance')
    class Meta:
        model = Character
        fields = ('campaign', 'name', 'description', 'assosiatedLocation')

class LocationSerializer(serializers.HyperlinkedModelSerializer):
    campaign = serializers.HyperlinkedRelatedField(read_only=False, view_name='api-campaign-instance')
    class Meta:
        model = Location
        fields = ('campaign', 'name', 'description', 'locationType')

class CampaignSerializer(serializers.HyperlinkedModelSerializer):
    logs = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='api-log-instance')
    characters = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='api-character-instance')
    locations = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='api-location-instance')
    member = UserSerializer(many=True)

    class Meta:
        model = Campaign
        fields = ('title', 'logs', 'characters', 'locations', 'member')
