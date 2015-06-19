
""" 
Views 
"""
#standard library imports
from datetime import timedelta, datetime

#third party imports
from django.shortcuts import get_object_or_404, render_to_response,redirect, \
render
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.http import HttpResponseRedirect, HttpResponse
#from permissions import IsUserThenReadPatch, ReadOnlyAuthentication
from rest_framework.generics import ListAPIView,RetrieveUpdateAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from oauth2_provider.ext.rest_framework import OAuth2Authentication, TokenHasScope, TokenHasReadWriteScope
#application imports
from serializers import ServiceSerializer, StudioServicesSerializer,  \
StudioProfileSerializer, StudioReviewSerializer,StudioTypeSerializer
from models import *
from booking.models import StudioReviews
from utils.permission_class import ReadWithoutAuthentication
from django.db.models import Q


class ServiceMixin(object):
    permission_classes = (ReadWithoutAuthentication,)
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()

class ServiceDetails(ServiceMixin, ListAPIView):
	pass


def get_studios(location,services,date=None):

    """function which filters the list of studios 
    based on location and services"""
    import pdb;pdb.set_trace();

    closed_on_day = (datetime.today().date().weekday() + 1)
    open_studios = StudioClosedDetails.objects.filter(~Q(closed_on = closed_on_day)).values('studio')
    studios = StudioProfile.objects.filter(city__contains = location, is_closed = 0	,  \
    	studio__in = open_studios).values('id')
    filtered_studios =  StudioServices.objects.filter(service_id__in =   \
	services, studio_profile_id__in = studios).values('studio_profile').distinct()
    ##call for booking logic
    return filtered_studios


class StudioProfileMixin(object):
    permission_classes = (ReadWithoutAuthentication,)
    serializer_class = StudioProfileSerializer
    model = StudioProfile
    def get_queryset(self):
        try:
            location = self.request.GET['location']
            services = self.request.GET['services']
            studios_ = get_studios(location,services)
            queryset = self.model.objects.filter(id__in = studios_)
        except Exception ,e:
            print repr(e)
        return queryset
		

class StudioProfileDetail(StudioProfileMixin, ListAPIView):
    #import pdb;pdb.set_trace();
    pass	

class StudioServicesDetail(ListAPIView):
	permission_classes = (ReadWithoutAuthentication,)
	serializer_class = StudioServicesSerializer
	queryset = StudioServices.objects.filter(studio_profile_id = 1)


class StudioReviewMixin(object):
    authentication_classes = [OAuth2Authentication]
    permission_classes = (TokenHasScope,)
    required_scopes = ['write','read']
    serializer_class = StudioReviewSerializer
    model = StudioReviews
    def get_queryset(self):
        queryset = self.model.objects.filter(user = self.request.user)
        return queryset

class StudioReviewDetails(StudioReviewMixin,ListCreateAPIView):
	pass


class GetStudioTypes(ListAPIView):
    permission_classes = (ReadWithoutAuthentication,)
    serializer_class = StudioTypeSerializer
    def get_queryset(self):
        queryset = StudioType.objects.filter(is_active = True)
        return queryset

