from django.conf.urls import patterns, include, url

from rest_framework.urlpatterns import format_suffix_patterns

from Campaign_Log import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'RPG_Campaign_Log.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index_view, name='index_view'),
    # url(r'^', include('Campaign_Log.urls')),
    url(r'^campaigns/$', views.CampaignView.as_view(), name = 'campaign - list'),
    url(r'^logs/$', views.LogView.as_view(), name = 'log - list'),
    url(r'^campaigns/(?P<pk>[\d]+)/$',views.CampaignInstanceView.as_view(), name='Campaign - Page')
)

urlpatterns = format_suffix_patterns(urlpatterns)
