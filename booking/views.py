
""" 
Views 
"""
#standard library imports
import random
import string
from datetime import timedelta, datetime

#third party imports
from django.shortcuts import get_object_or_404, render_to_response,redirect, \
render
from django.contrib.auth.decorators import login_required
from utils.generic_utils import *
#from permissions import IsUserThenReadPatch, ReadOnlyAuthentication
from rest_framework.generics import ListAPIView,RetrieveUpdateAPIView,ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from oauth2_provider.ext.rest_framework import OAuth2Authentication, TokenHasScope, TokenHasReadWriteScope
from rest_framework.response import Response
from django.db import transaction
from rest_framework import status
#application imports
from serializers import *
from models import *
from utils.generic_utils import sendEmail
from utils import responses



class ActiveBookingMixin(object):
    authentication_classes = [OAuth2Authentication]
    permission_classes = (TokenHasScope,)
    required_scopes = ['write','read']
    serializer_class = ActiveBookingSerializer
    def get_queryset(self):
        data = BookingDetails.objects.filter(user = self.request.user)
        return data

class GetActiveBookings(ActiveBookingMixin, ListAPIView):
    pass


class NewBooking(ListCreateAPIView,RetrieveUpdateAPIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = (TokenHasScope,)
    required_scopes = ['write','read']
    serializer_class = ActiveBookingSerializer
    
    @transaction.commit_manually
    def create(self,request,*args,**kwards):
        try:
            user = self.request.user
            data = self.request.DATA
            appnt_date = datetime.strptime(data['appnt_date'],'%Y-%m-%d')
            appnt_time = data['appnt_time']
            chars=string.ascii_uppercase + string.digits
            booking_code = ''.join(random.choice(chars) for _ in range(6))
            actual_amount = data['actual_amount']
            purchase_amount = data['purchase_amount']
            mobile_no = data['mobile_no']
            services_chosen = data['services']
            studio_id = data['studio']
            status_code = responses.BOOKING_CODES['BOOKING']
            ##set total duration for the booking taking all duration on the studio
            ##make entry in purchase table
            new_purchase = Purchase(customer = user,  \
                purchase_amount = purchase_amount, actual_amount = actual_amount,  \
                purchase_status = 'BOOKING', service_updated = 'new booking',  \
                status_code = status_code)
            new_purchase.save()
            new_booking = BookingDetails(user = user, booked_date =
                datetime.now(), appointment_date = appnt_date,  \
                appointment_time = appnt_time, booking_code = booking_code,  \
                studio_id = studio_id, booking_status = 'BOOKING',  \
                service_updated = 'new booking', purchase = new_purchase,status_code = status_code)
            new_booking.save()
            for service in services_chosen:
                service_booked = BookingServices(booking = new_booking,service_id = service, service_updated = 'new booking')
                service_booked.save()
        except Exception,e:
            print repr(e)
            transaction.rollback()
            return Response(status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            data = new_booking
            transaction.commit()
            return Response(data, status.HTTP_201_CREATED)
    
@transaction.commit_manually
def put(self,request,*args,**kwargs):
    try:
        user = self.request.user
        data = self.request.DATA
        booking_status = data['booking_status']
        booking_id = data['booking_id']
        payment_status = data['payment_status']
        if booking_status == 'BOOKED':
            status_code = responses.BOOKING_CODES['BOOKED']
        else:
            status_code = responses.BOOKING_CODES['FAILED']
            BookingDetails.objects.filter(id = booking_id).update(booking_status =   \
            booking_status, \
            service_updated = 'payment response', status_code = status_code,  \
            updated_date_time = datetime.now() )
            #purchase_id = BookingDetails.objects.filter(id = booking_id).values('purchase_id','studio_id')
            Purchase.objects.filter(id = purchase_id['purchase_id']).update(\
            purchase_status =  payment_status, service_updated = 'payment response', \
            status_code = status_code, updated_date_time = datetime.now())
        if booking_status == 'BOOKED':
            user = User.objects.filter(email = user).values('first_name','email')
            studio = StudioProfile.objects.filter(id = purchase_id['studio_id']).values('name','address_1', \
            'address_2','area','in_charge_person','contact_person','contact_mobile_no',  \
            'in_charge_mobile_no','city')
            contacts = {'in_charge_person':{'name':studio['in_charge_person'],'mobile_no': \
            studio['in_charge_mobile_no']},'contact_person':{'name':studio['contact_person'],\
            'mobile_no':studio['contact_mobile_no']}}
            studio_address = {'address_1':studio['address_1'],'address_2':studio['address_2'],  \
            'area':studio['area'],'city':studio['city']}
            booking_details = {'first_name':user['first_name'],'code':booking_code,  \
            'date':appnt_date, 'appnt_time':appnt_time,'services':services,  \
            'studio':studio['name'],'studio_address':studio_address,  \
            'contact':contacts}
            message = get_template('emails/booking_mail.html').render(Context(booking_details))
            to_user = user['email']
            subject = responses.MAIL_SUBJECTS['BOOKING_EMAIL']
            sms_template = responses.SMS_TEMPLATES['BOOKING_SMS']
            sms_message = sms_template%(user['first_name'],studio['name'],studio['area'],appointment_date,appointment_time)
            email = sendEmail(to_user,subject,message)
            sms = sendSMS(mobile_no,sms_message)
            try:
                email_bms = BookedMessageSent(booking = new_booking, email = to_user, \
                is_successful = email,type_of_message = 'book', mode = 'email', service_updated =  \
                'new booking')
                sms_bms = BookedMessageSent(booking = new_booking, mobile_no = mobile_no, \
                is_successful = sms_bms, type_of_message = 'book', mode = 'sms', service_updated =  \
                'new booking', message = sms_message)
                email_bms.save()
                sms_bms.save()
                notification_send = 1
                BookingDetails.objects.filter(id = booking_id).update(notification_send =   \
                notification_send)
            except Exception, DBerr:
                print (DBerr)
            else:
                return Response(status = status.HTTP_304_NOT_MODIFIED)
    except Exception,e:
        print repr(e)
        return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        data = booking_details
        return Response(data = data,status = status.HTTP_200_OK)


class CancelBooking(ActiveBookingMixin):
    def get_queryset(self):
        booking_id = self.request.DATA['booking_id']
        data = BookingDetails.objects.filter(user = self.request.user,  \
            id = booking_id)
        return data

    @transaction.commit_manually
    def put(self,request,*args,**kwargs):
        try:
            booking_id = self.request.DATA['booking_id']
            user = self.request.user
            BookingDetails.objects.filter(id = booking_id).update(booking_status =  \
                'CANCELLED', service_updated = 'cancel booking',  \
                status_code = responses.BOOKING_CODES['CANCELLED'],  \
                updated_date_time = datetime.now())
            purchase_id = BookingDetails.objects.get(id = booking_id).values('purchase_id')
            Purchase.objects.filter(id = purchase_id).update(purchase_status = 'REFUND_REQUESTED',  \
                status_code = responses.BOOKING_CODES['REFUND_REQUESTED'])
        except Exception,e:
            transaction.rollback()
            print repr(e)
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            transaction.commit()
            return Response(status = status.HTTP_200_OK)

class ValidateBookingCode(RetrieveUpdateAPIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = (TokenHasScope,)
    required_scopes = ['write','read']
    serializer_class = ActiveBookingSerializer
    def get_queryset(self):
        booking_code = self.request.DATA['booking_code']
        studio_pin = self.request.DATA['studio_pin']
        data = BookingDetails.objects.filter(studio_id = studio_pin, booking_code =  \
        booking_code, booking_status = 'BOOKED', status_code ='B001', is_valid = True)
        return data
    
    @transaction.commit_manually
    def put(self,request,*args,**kwars):
        try:
            booking_code = self.request.DATA['booking_code']
            studio_pin = self.request.DATA['studio_pin']
            #studio = StudioProfile.objects.filter(studio_id = studio_pin)
            BookingDetails.objects.filter(studio_id = studio_pin, booking_code =  \
            booking_code, booking_status = 'BOOKED', status_code ='B001',  \
            is_valid = True).update(booking_status = 'USED', status_code = 'B004',  \
            service_updated = 'booking used', updated_date_time = datetime.now())
        except Exception,e:
            print repr(e)
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(status = status.HTTP_200_OK)





