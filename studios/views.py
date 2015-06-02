
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
from rest_framework.generics import ListAPIView,RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

#application imports
from serializers import ServiceSerializer, StudioServicesSerializer,  \
StudioProfileSerializer
from models import *
from utils.permission_class import ReadWithoutAuthentication


class ServiceMixin(object):
    permission_classes = (ReadWithoutAuthentication,)
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()

class ServiceDetails(ServiceMixin, ListAPIView):
	pass


def get_studios(location,services):

    """function which filters the list of studios 
    based on location and services"""
    studios = StudioProfile.objects.filter(city__contains = location).values('id')
    filtered_studios =  StudioServices.objects.filter(service_id__in =   \
	services, studio_profile_id__in = studios).values('studio_profile').distinct()
    ##call for booking logic
    return filtered_studios


class StudioProfileMixin(object):
	permission_classes = (ReadWithoutAuthentication,)
	serializer_class = StudioProfileSerializer
	model = StudioProfile
	def get_queryset(self):
		#get studio id having location get ids related to it
		#get studio id having services
		#location = self.request.DATA['location']
		#service = self.request.DATA['services']
		location = 'karaikudi'
		services = [1,2]
		studios_ = get_studios(location,services)
		queryset = self.model.objects.filter(id__in = studios_)
		return queryset
		

class StudioProfileDetail(StudioProfileMixin, ListAPIView):
    pass	

class StudioServicesDetail(ListAPIView):
	permission_classes = (ReadWithoutAuthentication,)
	serializer_class = StudioServicesSerializer
	queryset = StudioServices.objects.filter(studio_profile_id = 1)
