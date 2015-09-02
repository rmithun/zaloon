from django.conf.urls import patterns, include, url
from django.contrib import admin
import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'onepass.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^services/$', views.ServiceDetails.as_view(), name = 'services'),
    url(r'^service_types/$', views.ServiceTypeDetails.as_view(), name = 'service_types'),
    #url(r'^search/$', views.SearchResults.as_view(), name = 'search'),
    url(r'^studio_profile/$', views.StudioProfileDetail.as_view(), name = 'studio_profile'),
    url(r'^studio_services/$', views.StudioServicesDetail.as_view(), name = 'studio_services'),
    url(r'^booking_review/$', views.StudioReviewDetails.as_view(), name = 'booking_review'),
    url(r'^studio_type/$', views.GetStudioTypes.as_view(), name = 'studio_type'),
    url(r'^studio_kind/$', views.GetStudioKinds.as_view(), name = 'studio_kind'),
    url(r'^studio_register/$', views.StudioRegistration.as_view(), name = 'studio_register'),



)
