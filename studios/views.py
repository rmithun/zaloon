
""" 
Views 
"""
#standard library imports
from datetime import timedelta, datetime
import operator

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
StudioProfileSerializer, StudioReviewSerializer,StudioTypeSerializer,StudioSerializer
from models import *
from booking.models import StudioReviews
from utils.permission_class import ReadWithoutAuthentication
from django.db.models import Q
from django.conf import settings
from utils import generic_utils


class ServiceMixin(object):
    permission_classes = (ReadWithoutAuthentication,)
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()

class ServiceDetails(ServiceMixin, ListAPIView):
	pass


def get_studios(location,service,date=None):

    """function which filters the list of studios 
    based on location and services"""
    try:
        #import pdb;pdb.set_trace();
        location_set =  reduce(operator.__or__, [Q(area__icontains=query)  \
        | Q(address_1__icontains=query) | Q(address_2__icontains=query  \
        )for query in location])
        closed_on_day = (datetime.today().date().weekday() + 1)
        open_studios = StudioClosedDetails.objects.filter(~Q(closed_on = closed_on_day)).values('studio')
        if settings.DB:
            studios = StudioProfile.objects.filter(location_set, is_closed = 0 ,  \
            studio__in = open_studios).values('id')
            services = Service.objects.filter(service_name__iregex = r'\b{0}\b'.format(service)).values('id')
        else:
            services = Service.objects.filter(service_name__iregex = r'\y{0}\y'.format(service)).values('id')
            studios = StudioProfile.objects.filter(area__iregex = r'\y{0}\y'.format(location), is_closed = 0 ,  \
            studio__in = open_studios).values('id')
        if len(service) > 0:
            filtered_studios =  StudioServices.objects.filter(service_id__in =   \
	        services, studio_profile_id__in = studios).values('studio_profile').distinct()
        else:
            filtered_studios =  StudioServices.objects.filter(studio_profile_id__in =   \
                studios).values('studio_profile').distinct()
        ##call for booking logic
    except Exception,e:
        print repr(e)
        return None
    else:
        return filtered_studios


class StudioProfileMixin(object):
    permission_classes = (ReadWithoutAuthentication,)
    serializer_class = StudioProfileSerializer
    model = StudioProfile
    def get_queryset(self):
        try:
            city = self.request.GET['location'].split(',')
            print city[-3]
            ##add city to filter in future
            locations = self.request.GET['location'].split()
            service = self.request.GET['service']
            studios_ = get_studios(locations,service)
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

class GetStudioKind(ListAPIView):
    permission_classes = (ReadWithoutAuthentication,)
    serializer_class = StudioKindSerializer
    def get_queryset(self):
        queryset = StudioKind.objects.filter(is_active = True)
        return queryset



class StudioRegistration(ListCreateAPIView):
    permission_classes = (ReadWithoutAuthentication,)
    serializer_class = StudioSerializer
    def create(self,request,*args,**kwards):
        try:
            data = self.request.DATA
            password = data['password']
            email = data['email']
            studio_name = data['name']
            #studio_group = data['studio_group']
            existing_email = Studio.objects.filter(email = email)
            if not existing_email:
                studio = Studio.objects.create_user(email = email ,password = password)
                studio.save()
                studio_details = {'studio_pin':studio.id,'password':password,'email':email}
                message = get_template('emails/merchant_registration.html').render(Context(studio_details))
                studio_mail = email
                subject = responses.MAIL_SUBJECTS['STUDIO_REGISTRATION']
                try:
                    generic_utils.sendEmail(studio_mail,subject,message)
                except Exception,e:
                    print repr(e)
            else:
                print "existing"  
        except Exception,e:
            print repr(e)
            return Response(status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(status.HTTP_201_CREATED)
    


        
class StudioLogin(ListAPIView):
    permission_classes = (ReadWithoutAuthentication,)
    serializer_class = StudioSerializer


@login_required
def getSlots(request):
    try:
        data = request.GET['data']
        studio = data['studio_id']
        date = data['date']
        services = data['services']
        bookings = BookingDetails.objects.filter(appointment_date = date, studio_id = studio,  \
            booking_status = 'BOOKED', status_code = 'B001', is_active = True)
        if len(bookings) > 0:
            generate_slots()
    except Exception,e:
        print repr(e)
        data = None
        return Response(data = data, status = status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return Response(data = data, status = status.HTTP_200_OK)