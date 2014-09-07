from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from rest_framework import routers
from Campaign_Log import views

from django.contrib import admin
admin.autodiscover()

router = routers.SimpleRouter()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'RPG_Campaign_Log.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),


    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index_view, name='index_view'),
    # url(r'^', include('Campaign_Log.urls')),
    url(r'^api/campaigns/$', views.CampaignAPIView.as_view(), name = 'api-campaign-list'),
    url(r'^api/logs/$', views.LogView.as_view(), name = 'api-log-list'),
    url(r'^api/characters/$', views.CharacterView.as_view(), name = 'api-character-list'),
    url(r'^api/locations/$', views.LocationView.as_view(), name = 'api-location-list'),

    url(r'^api/campaigns/(?P<pk>[\d]+)/$',views.CampaignInstanceView.as_view(), name='api-campaign-instance'),
    url(r'^api/logs/(?P<pk>[\d]+)/$',views.LogInstanceView.as_view(), name='api-log-instance'),
    url(r'^api/characters/(?P<pk>[\d]+)/$',views.CharacterInstanceView.as_view(), name='api-character-instance'),
    url(r'^api/locations/(?P<pk>[\d]+)/$',views.LocationInstanceView.as_view(), name='api-location-instance'),

#   nonAPI sites

    url(r'^campaigns/$', views.ListCampaignView.as_view(), name='campaign-list'),
    url(r'^campaigns/new$', views.CreateCampaignView.as_view(), name='campaign-new',),
    url(r'^campaigns/(?P<pk>\d+)/$', views.CampaignView.as_view(), name='campaign',),

    url(r'^logs/new$', views.CreateLogView.as_view(), name='log-new',),
    url(r'^logs/edit/(?P<pk>\d+)/$', views.UpdateLogView.as_view(), name='log-edit',),
    url(r'^logs/delete/(?P<pk>\d+)/$', views.DeleteLogView.as_view(), name='log-delete',),
)

urlpatterns += staticfiles_urlpatterns()
