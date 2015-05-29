
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
from serializers import ServiceSerializer, StudioServicesSerializer
from models import *
from utils.permission_class import ReadWithoutAuthentication


class ServiceMixin(object):
    permission_classes = (ReadWithoutAuthentication,)
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()

class ServiceDetails(ServiceMixin, ListAPIView):
	pass


class SearchResults(ListAPIView):
    permission_classes = (ReadWithoutAuthentication,)
    serializer_class = StudioServicesSerializer
    def get_queryset(self):
	    try:
			response = None
			#data = request.GET['data']
			#location = data['location']
			#from_time = data['from_time']
			#to_time = data['to_time']
			#service = data['service']
			service = 'hair cut'
			response = StudioServices.objects.filter(service_id = 1, is_active = True)
	    except Exception,err:
			print repr(err)
			return None
	    else:
			return response
