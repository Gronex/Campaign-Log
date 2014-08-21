from django.shortcuts import render

#from django.http import HttpResponse
#from django.views.decorators.csrf import csrf_exempt
#from rest_framework.renderers import JSONRenderer
#from rest_framework.parsers import JSONParser
from Campaign_Log.models import Campaign, Log, Character, Location
from rest_framework import generics
from Campaign_Log.serializers import CampaignSerializer, LogSerializer, CharacterSerializer, LocationSerializer
# Create your views here.


class CampaignView(generics.ListAPIView):
    model = Campaign
    serializer_class = CampaignSerializer

class LogView(generics.ListAPIView):
    model = Log
    serializer_class = LogSerializer

class CharacterView(generics.ListAPIView):
    model = Character
    serializer_class = CharacterSerializer

class LocationView(generics.ListAPIView):
    model = Location
    serializer_class = LocationSerializer


class CampaignInstanceView(generics.RetrieveAPIView):
    model = Campaign
    serializer_class = CampaignSerializer
