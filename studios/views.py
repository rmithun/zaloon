
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
			#
			#service = data['service']
			service = 'hair cut'
			response = StudioServices.objects.filter(service_id = 1, is_active = True)
	    except Exception,err:
			print repr(err)
			return None
	    else:
			return response


class StudioBookingSlots(APIView):
	permission_classes = (ReadWithoutAuthentication,)
	def get(self, request, *args, **kwargs):
		try:
			response = None
			studio = self.request.GET['studio']
			from_time = self.request.GET['from_time']
			to_time = self.request.GET['to_time']
			date = self.request.GET['date']
			services = self.request.GET['services']
			#booking logic function
			response = bookingLogic(studio,from_time,to_time,date,services)
		except Exception,e:
			print repr(e)
			#add log
			return Response(response,status.HTTP_500_INTERNAL_SERVER_ERROR)
		else:
			return Response(response, status.HTTP_200_OK)


class StudioPictures(ListAPIView):
	permission_classes = (ReadWithoutAuthentication,)
	serializer_class = StudioPicturesSerializer
	def get_queryset(self):
		try:
			response = None
			studio = self.request.GET['studio']
			response = StudioPicture.objects.filter(studio_profile_id = studio)
		except Exception,e:
			print repr(e)
			return response
		else:
			return response

class StudioReviews(ListAPIView):
	permission_classes = (ReadWithoutAuthentication,)
	serializer_class = StudioReviewSerializer
	def get_queryset(self):
		try:
			response = None
			studio = self.request.GET['studio']
			response = StudioReviews.objects.filter(studio_profile_id = studio, is_active = 1)
		except Exception,e:
			print repr(e)
			return response
		else:
			return response


class StudioServices(ListAPIView):
	permission_classes = (ReadWithoutAuthentication,)
	serializer_class = StudioServicesSerializer
	def get_queryset(self):
		try:
			response = None
			studio = self.request.GET['studio']
			response = StudioServices.objects.filter(studio_profile_id = studio, is_active = 1)
		except Exception,e:
			print repr(e)
			return response
		else:
			return response