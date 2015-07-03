
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
from rest_framework.generics import ListAPIView,RetrieveUpdateAPIView, ListCreateAPIView,  \
CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from rest_framework import status
from oauth2_provider.ext.rest_framework import OAuth2Authentication, TokenHasScope, TokenHasReadWriteScope
from django.template.loader import get_template
from django.template import Context
from django.db import transaction


#application imports
from serializers import ServiceSerializer, StudioServicesSerializer,  \
StudioProfileSerializer, StudioReviewSerializer,StudioTypeSerializer,StudioSerializer,  \
StudioKindSerializer
from models import *
from booking.models import BookingDetails
from booking.models import StudioReviews
from utils.permission_class import ReadWithoutAuthentication, PostWithoutAuthentication
from django.db.models import Q
from django.conf import settings
from utils import generic_utils,responses


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

class GetStudioKinds(ListAPIView):
    permission_classes = (ReadWithoutAuthentication,)
    serializer_class = StudioKindSerializer
    def get_queryset(self):
        queryset = StudioKind.objects.filter(is_active = True)
        return queryset



class StudioRegistration(CreateAPIView):
    permission_classes = (PostWithoutAuthentication,)
    serializer_class = StudioSerializer
    @transaction.commit_manually
    def create(self,request,*args,**kwards):
        try:
            data = self.request.DATA
            email = data['email']
            mobile_no = data['mobile_no']
            studio_name = data['name']
            area = data['area']
            password = data['password']
            #studio_group = data['studio_group']
            existing_email = StudioAddRequest.objects.filter(email = email)
            if not existing_email:
                studio_req = StudioAddRequest(email = email, area = area,  \
                    mobile_no = mobile_no,studio_name = studio_name)
                studio_req.save()
                studio = Studio(email = email, password = password)
                studio.save();
                studio_details = {'email':email,'studio_name':studio_name,'studio_pin':studio.id,  \
                'password':password}
                message = get_template('emails/studio_req_register.html').render(Context(studio_details))
                studio_mail = email
                subject = responses.MAIL_SUBJECTS['STUDIO_REQ_REGISTER']
                try:
                    generic_utils.sendEmail(studio_mail,subject,message)
                except Exception,e:
                    transaction.rollback()
                    print repr(e)
                    return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)
            else:
                transaction.rollback()
                return Response(status = status.HTTP_400_BAD_REQUEST)
        except Exception,e:
            print repr(e)
            transaction.rollback()
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            transaction.commit()
            return Response(status = status.HTTP_201_CREATED)
    

        
class StudioLogin(ListAPIView):
    permission_classes = (ReadWithoutAuthentication,)
    serializer_class = StudioSerializer


def return_availablity(closed_from,closing_till):
    all_hours = responses.HOURS_DICT
    all_hours.pop(closed_from)
    all_hours.pop(closing_till)




@login_required
def getSlots(request):
    try:
        data = request.GET['data']
        studio = data['studio_id']
        date = data['date']
        services = data['services']
        bookings = BookingDetails.objects.filter(appointment_date = date, studio_id = studio,  \
            booking_status = 'BOOKED', status_code = 'B001', is_active = True)
        #get studio start and end time
        studio_time = StudioProfile.objects.filter(id = studio).values('opening_at',  \
            'closing_at','daily_studio_closed_from','daily_studio_closed_till')
        #check whether studio is closed on that day
        start = studio_time['opening_at']
        end = studio_time['closing_at']
        closed_from = studio_time['daily_studio_closed_from']
        closed_to = studio_time['daily_studio_closed_till']
        slots = responses.HOURS_DICT
        #check  total duration not to cross closed hours or other bookings
        if len(bookings) > 0:
            for bks in bookings:
                start_hour = bks.appointment_start_time.hour()
                start_min = bks.appointment_start_time.minute()
                end_hour = bks.appointment_end_time.hour()
                end_min = bks.appointment_end_time.minute()
                slots.pop()

                    
    except Exception,e:
        print repr(e)
        data = None
        return Response(data = data, status = status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return Response(data = data, status = status.HTTP_200_OK)



@login_required
def  Coupon_Logic(request):
    try:
        data  = request.GET['data']
        services = data['services']
        coupon_code = data['coupon_code']
        appnt_date = data['appnt_date']
        studio_id = data['studio_id']
        amount = data['amount']
        user = request.user
        #check coupon code is there
        if len(coupon_code) != 1:
            response_to_ng = simplejson.dumps(responses.COUPON_RESPONSE['no_coupon'])
            return Response(data = response_to_ng, status = status.HTTP_400_BAD_REQUEST)
        else:
            if coupon['expiry_date'] > datetime.today().date:
                response_to_ng = simplejson.dumps(responses.COUPON_RESPONSE['expiry_date'])
                return Response(data = response_to_ng, status = status.HTTP_400_BAD_REQUEST)
            if coupon['services_coupon'] == 1:
                #get coupon services 
                for serv in services:
                    if serv.id in for_services:
                        new_amount = new_amount = serv.amount
                if new_amount == 0:
                    response_to_ng = simplejson.dumps(responses.COUPON_RESPONSE['no_applicable_service'])
                    return Response(data = response_to_ng, status = status.HTTP_400_BAD_REQUEST)
            if coupon['applicable'] != 1:
                #check whether coupon is applicable in the studio
                is_applicable = Coupon_Studios.objects.filter(coupon_id = coupon.id, studio_id = studio_id,  \
                    is_active= True)
                if len(is_applicable) == 1:
                    if  coupon['one_time'] == 1:
                        ##check whether the user already used the coupon
                        if used:
                            response_to_ng =  simplejson.dumps(responses.COUPON_RESPONSE['coupon_used'])
                            return Response(data = response_to_ng, status = status.HTTP_400_BAD_REQUEST)


