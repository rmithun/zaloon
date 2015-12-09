
""" 
Views 
"""
#standard library imports
from datetime import timedelta, datetime
import operator
import logging
import traceback
from itertools import chain


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
from django.db.models import Min, Avg
from django.core.cache import cache


#application imports
from serializers import ServiceSerializer, StudioServicesSerializer,  \
StudioProfileSerializer, StudioReviewSerializer,StudioTypeSerializer,StudioSerializer,  \
StudioKindSerializer,ServiceTypeSerializer,StudioProfileDetailsSerialzier, \
AllStudiosSerializer
from models import *
from booking.models import BookingDetails,StudioReviews
from utils.permission_class import ReadWithoutAuthentication, PostWithoutAuthentication
from django.db.models import Q
from django.conf import settings
from utils import generic_utils,responses



logger_studios = logging.getLogger('log.studios')
logger_error = logging.getLogger('log.errors')

class ServiceMixin(object):
    permission_classes = (ReadWithoutAuthentication,)
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()

class ServiceDetails(ServiceMixin, ListAPIView):
    pass

class ServiceTypeDetails(ListAPIView):
    permission_classes = (ReadWithoutAuthentication,)
    serializer_class = ServiceTypeSerializer
    queryset = ServiceType.objects.all()


def get_studios(service_type,date=None):

    """function which filters the list of studios 
    based on location and services"""
    try:
        #location_set =  reduce(operator.__or__, [Q(area__icontains=query)  \
        #| Q(address_1__icontains=query) | Q(address_2__icontains=query  \
        #)for query in location])
        #closed_on_day = (datetime.today().date().weekday() + 1)
        #open_studios = StudioClosedDetails.objects.filter(~Q(closed_on = closed_on_day)).values('studio')
        if settings.DEBUG:
            #studios = StudioProfile.objects.filter(city = 'Chennai', is_closed = 0 ,  \
            #id__in = open_studios).values('id')
            services = Service.objects.filter(service_type_id  = services_type).values('id')
        else:
            #services_types = ServiceType.objects.filter(service_name__iregex = r'\y{0}\y'.format(service_type)).values('id')
            services = Service.objects.filter(service_type_id  = services_type).values('id')
            #studios = StudioProfile.objects.filter(area__iregex = r'\y{0}\y'.format(location), is_closed = 0 ,  \
            #id__in = open_studios).values('id')
        if len(services) > 0:
            filtered_studios =  StudioServices.objects.filter(service_id__in =   \
            services).values('studio_profile').distinct()
        else:
            #filtered_studios =  StudioServices.objects.all().distinct()
            filtered_studios =  []

        ##call for booking logic
    except Exception,e:
        logger_error.error(traceback.format_exc())
        return []
    else:
        logger_studios.info("Found - "+str(len(filtered_studios))+" studios")
        return filtered_studios


class StudioProfileMixin(object):
    permission_classes = (ReadWithoutAuthentication,)
    serializer_class = StudioProfileSerializer
    model = StudioProfile
    def get(self, request, *args, **kw):
        try:
            #city = self.request.GET['location'].split(',')
            ##add city to filter in future
            print datetime.now()
            location = self.request.GET['location']
            service = self.request.GET['service']
            cache_key = location.replace(" ","")+str(service)
            if cache.get(cache_key):
                print datetime.now()
                return Response(cache.get(cache_key))
            logger_studios.info("Search Query - "+str(self.request.GET))
            studios = StudioServiceTypes.objects.filter(service_type_id = service, is_active = 1).values('studio_profile_id')
            #chosen_studios = StudioProfile.objects.filter(Q(id__in = studios), 
            #    (Q(search_field_1 = location)|Q(search_field_2 = location))).select_related('studio_closed_details', \
            #    'pic_of_studio')
            chosen_studios = StudioProfile.objects.filter(Q(id__in = studios)).select_related('studio_closed_details', \
                'pic_of_studio')
            ser_data = StudioProfileSerializer(chosen_studios, many = True)
            data = ser_data.data
            for studio in data:
                min_price = StudioServices.objects.filter(studio_profile_id = studio['id'], is_active = 1  \
                   ,service_id__in = Service.objects.filter(service_type_id = service)).aggregate(Min('price'))
                avg_rating = StudioReviews.objects.filter(studio_profile_id = studio['id'], \
                    is_active = 1).aggregate(Avg('rating'))
                studio['min_price'] = min_price['price__min']
                if avg_rating['rating__avg'] is not None:
                    studio['avg_rating'] = round(float(avg_rating['rating__avg']))
                else:
                    studio['avg_rating'] = None
            now = datetime.now().time()
            expiration_sec = ((23 - now.hour)*60 +(59 - now.minute)*60)
            cache.set(cache_key, data, expiration_sec)
        except Exception ,e:
            logger_error.error(traceback.format_exc())
            return Response()
        else:
            print datetime.now()
            return Response(data)
        

class StudioProfileDetail(StudioProfileMixin, APIView):
    #import pdb;pdb.set_trace();
    pass    

class StudioDetailed(APIView):
    permission_classes = (ReadWithoutAuthentication,)
    serializer_class = StudioProfileDetailsSerialzier
    model = StudioProfile
    def get(self, request, *args, **kw):
        try:
            print datetime.now()
            studio_id = self.request.GET['id']
            cache_key = 'studio'+str(studio_id)
            if cache.get(cache_key):
                data = cache.get(cache_key)
                print datetime.now()
                return Response(data)
            studios_data = StudioProfile.objects.filter(id = studio_id).select_related('studio_detail_for_activity',  \
                'studio_review')
            ser_data = StudioProfileDetailsSerialzier(studios_data, many = True)
            data = ser_data.data
            now = datetime.now()
            #expiration_sec = ((23 - now.hour)*60 +(59 - now.minute)*60)
            expiration_sec = 1800
            cache.set(cache_key, data, expiration_sec)
        except Exception,e:
            logger_error.error(traceback.format_exc())
            return Response()
        else:
            print datetime.now()
            return Response(data)


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
            logger_studios.info("Studio registration data "+str(data))
            existing_email = StudioAddRequest.objects.filter(email = email)
            if not existing_email:
                studio_req = StudioAddRequest(email = email, area = area,  \
                    mobile_no = mobile_no,studio_name = studio_name)
                studio_req.save()
                studio = Studio(email = email, password = password)
                studio.save();
                studio_details = {'email':email,'studio_name':studio_name,'studio_pin':studio.id,  \
                'password':password}
                logger_studios.info("Studios details "+str(studio_details))
                message = get_template('emails/studio_req_register.html').render(Context(studio_details))
                studio_mail = email
                subject = responses.MAIL_SUBJECTS['STUDIO_REQ_REGISTER']
                try:
                    generic_utils.sendEmail(studio_mail,subject,message)
                except Exception,e:
                    transaction.rollback()
                    logger_error.error(traceback.format_exc())
                    return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)
            else:
                transaction.rollback()
                logger_studios.info("Studio already registered")
                return Response(status = status.HTTP_400_BAD_REQUEST)
        except Exception,e:
            logger_error.error(traceback.format_exc())
            transaction.rollback()
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            transaction.commit()
            return Response(status = status.HTTP_201_CREATED)
    

        
class StudioLogin(ListAPIView):
    permission_classes = (ReadWithoutAuthentication,)
    serializer_class = StudioSerializer

class AllStudios(ListAPIView):
    permission_classes = (ReadWithoutAuthentication,)
    serializer_class = AllStudiosSerializer
    queryset = StudioProfile.objects.all().order_by('-id')[:150]


