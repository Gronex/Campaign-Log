from django.shortcuts import render
from django.forms import ModelForm
from django.core.urlresolvers import reverse
from django.views.generic import CreateView, UpdateView, DeleteView

from Campaign_Log.models import Campaign, Log, Character, Location
from rest_framework import generics
from Campaign_Log.serializers import CampaignSerializer, LogSerializer, CharacterSerializer, LocationSerializer
# Create your views here.

def index_view(request):
    #TODO: Make some kind of news blog
    response = {
        'logs': Log.objects.all(),
        'characters': Character.objects.all(),
        'locations': Location.objects.all(),
    }
    return render(request, 'index.html', response)

def campaignListView(request):
    response = {
        'campaigns': Campaign.objects.all(),
    }
    return render(request, 'campaignList.html', response)

def myCampaignView(request, pk):
    campaign = Campaign.objects.get(pk=pk)
    response = {
        'campaign': campaign,
        'logs': Log.objects.filter(campaign=campaign),
        'characters': Character.objects.filter(campaign=campaign),
        'locations': Location.objects.filter(campaign=campaign),
    }
    return render(request, 'campaign.html', response)

def myLogView(request, campaignkey, logkey):
    campaign = Campaign.objects.get(pk=campaignkey)
    log = Log.objects.get(pk=logkey)

    logform = LogForm
    response = {
        'campaign': campaign,
        'log': log,
        'logform': logform,
    }
    return render(request, 'update-log.html', response)

class LogForm(ModelForm):
    class Meta:
        model = Log
        fields = ('title', 'content')


class CampaignForm(ModelForm):
    class Meta:
        model = Campaign
        fields = ('title',)

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



class CreateLogView(CreateView):
    model = Log
    template_name = 'edit_log.html'
    def get_success_url(self):
        return reverse('my-campaign-list')

    def get_context_data(self, **kwargs):
        context = super(CreateLogView, self).get_context_data(**kwargs)
        context["action"] = reverse('log-new')
        return context

class UpdateLogView(UpdateView):
    model = Log
    template_name = 'edit_log.html'
    def get_success_url(self):
        return reverse('my-campaign-list')#TODO: change to specific campaign

    def get_context_data(self, **kwargs):
        context = super(UpdateLogView, self).get_context_data(**kwargs)
        context["action"] = reverse('log-edit', kwargs={'pk': self.get_object().id})
        return context

class DeleteLogView(DeleteView):
    model = Log
    template_name = 'delete_log.html'
