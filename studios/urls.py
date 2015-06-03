from django.conf.urls import patterns, include, url
from django.contrib import admin
import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'onepass.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^services/$', views.ServiceDetails.as_view(), name = 'services'),
    #url(r'^search/$', views.SearchResults.as_view(), name = 'search'),
    url(r'^studio_profile/$', views.StudioProfileDetail.as_view(), name = 'studio_profile'),
    url(r'^studio_services/$', views.StudioServicesDetail.as_view(), name = 'studio_services'),



)