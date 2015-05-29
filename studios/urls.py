from django.conf.urls import patterns, include, url
from django.contrib import admin
import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'onepass.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^services/$', views.ServiceDetails.as_view(), name = 'services'),
    url(r'^search/$', views.SearchResults.as_view(), name = 'search'),



)
