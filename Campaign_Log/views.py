from django.shortcuts import render

from Campaign_Log.models import Campaign, Log, Character, Location
from rest_framework import generics
from Campaign_Log.serializers import CampaignSerializer, LogSerializer, CharacterSerializer, LocationSerializer
# Create your views here.

def index_view(request):
    response = {
        'campaigns': Campaign.objects.all(),
        'logs': Log.objects.all(),
        'characters': Character.objects.all(),
        'locations': Location.objects.all(),
    }

    return render(request, 'index.html', response)


class CampaignView(generics.ListCreateAPIView):
    model = Campaign
    serializer_class = CampaignSerializer

class LogView(generics.ListCreateAPIView):
    model = Log
    serializer_class = LogSerializer

class CharacterView(generics.ListCreateAPIView):
    model = Character
    serializer_class = CharacterSerializer

class LocationView(generics.ListCreateAPIView):
    model = Location
    serializer_class = LocationSerializer

class CampaignInstanceView(generics.RetrieveUpdateAPIView):
    model = Campaign
    serializer_class = CampaignSerializer

class LogInstanceView(generics.RetrieveUpdateAPIView):
    model = Log
    serializer_class = LogSerializer

class CharacterInstanceView(generics.RetrieveUpdateAPIView):
    model = Character
    serializer_class = CharacterSerializer

class LocationInstanceView(generics.RetrieveUpdateAPIView):
    model = Location
    serializer_class = LocationSerializer
