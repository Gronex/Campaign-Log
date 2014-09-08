from django.shortcuts import render
from django.forms import ModelForm
from django.core.urlresolvers import reverse
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

#ERROR handeling
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

from Campaign_Log.models import Campaign, Log, Character, Location
from rest_framework import generics
from Campaign_Log.serializers import CampaignSerializer, LogSerializer, CharacterSerializer, LocationSerializer
# Create your views here.

class LoggedInMixin(object):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoggedInMixin, self).dispatch(*args, **kwargs)

class CampaignMemberMixin(object):
    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        pk = self.kwargs.get(self.pk_url_kwarg, None)
        queryset = queryset.filter(
            pk=pk,
            member = self.request.user,
        )

        try:
            obj = queryset.get()
        except ObjectDoesNotExist:
            raise Http404(u"No objects found matching the query")
        return obj

class LogMemberMixin(object):
    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        pk = self.kwargs.get(self.pk_url_kwarg, None)
        queryset = queryset.filter(
            pk=pk,
        )

        try:
            obj = queryset.select_related().get()

            # Make sure the user has access to the log by checking if the log is in a campaign the user can use
            Campaign.objects.filter(
            logs = obj,
            member = self.request.user,
            ).get()

        except ObjectDoesNotExist:
            raise Http404(u"No objects found matching the query")
        return obj

def index_view(request):
    #TODO: Make some kind of news blog
    response = {
        'logs': Log.objects.all(),
        'characters': Character.objects.all(),
        'locations': Location.objects.all(),
    }
    return render(request, 'index.html', response)

class CampaignAPIView(generics.ListCreateAPIView):
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



class CampaignView(LoggedInMixin, CampaignMemberMixin, DetailView):
    model = Campaign
    template_name = 'campaign.html'


class ListCampaignView(LoggedInMixin, ListView):
    model = Campaign
    template_name = 'campaignList.html'

    def get_queryset(self):
        return Campaign.objects.filter(member = self.request.user)

class CreateCampaignView(LoggedInMixin, CreateView):
    model = Campaign
    template_name = 'edit_campaign.html'

    def get_success_url(self):
        return reverse('campaign-list')

    def get_context_data(self, **kwargs):
        context = super(CreateCampaignView, self).get_context_data(**kwargs)
        context["action"] = reverse('campaign-new')
        return context

class CreateLogView(LoggedInMixin, CreateView):
    model = Log
    template_name = 'edit_log.html'
    def get_success_url(self):
        return reverse('campaign-list')#TODO: change to specific campaign

    def get_context_data(self, **kwargs):
        context = super(CreateLogView, self).get_context_data(**kwargs)
        context["action"] = reverse('log-new')
        return context

class UpdateLogView(LoggedInMixin,LogMemberMixin, UpdateView):
    model = Log
    template_name = 'edit_log.html'
    def get_success_url(self):
        return reverse('campaign-list')#TODO: change to specific campaign

    def get_context_data(self, **kwargs):
        context = super(UpdateLogView, self).get_context_data(**kwargs)
        context["action"] = reverse('log-edit', kwargs={'pk': self.get_object().id})
        return context

class DeleteLogView(LoggedInMixin, LogMemberMixin, DeleteView):
    model = Log
    template_name = 'delete_log.html'

    def get_success_url(self):
        return reverse('campaign-list')#TODO: change to specific campaign
