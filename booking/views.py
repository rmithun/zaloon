
""" 
Views 
"""
#standard library imports
import random
import string
from datetime import timedelta, datetime
import datetime as dt
import simplejson
import logging
import traceback
import copy
import requests

#third party imports
from django.shortcuts import get_object_or_404, render_to_response,redirect, \
render
from django.contrib.auth.decorators import login_required
#from permissions import IsUserThenReadPatch, ReadOnlyAuthentication
from rest_framework.generics import ListAPIView,RetrieveUpdateAPIView,ListCreateAPIView, \
CreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from oauth2_provider.ext.rest_framework import OAuth2Authentication, TokenHasScope, TokenHasReadWriteScope
from rest_framework.response import Response
from django.db import transaction
from rest_framework import status
from django.db.models import Sum, Q
from django.template.loader import get_template
from django.template import Context
from rest_framework.pagination import PageNumberPagination

#application imports
from serializers import *
from models import *
from user_accounts.models import UserProfile
from utils.generic_utils import sendEmail, sendSMS, uniquekey_generator, getIframeFromPG
from utils import responses
from studios.models import StudioServices
from studios.serializers import StudioReviewSerializer
from utils.permission_class import ReadWithoutAuthentication, PostWithoutAuthentication


logger_booking = logging.getLogger('log.booking')
logger_error = logging.getLogger('log.errors')

@login_required
def booking_page(request):
    """returns booking page html"""
    return render(request,'user_accounts/payment.html',{})



class CustomPagination(PageNumberPagination):
    def get_paginated_response(self, data):
        return Response({
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'count': self.page.paginator.count,
            'results': data
        })

class LargeResultsSetPagination(CustomPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 10



class ActiveBookingMixin(object):
    authentication_classes = [OAuth2Authentication]
    permission_classes = (TokenHasScope,)
    required_scopes = ['write','read']
    serializer_class = ActiveBookingSerializer
    pagination_class = LargeResultsSetPagination
    def get_queryset(self):
        try:
            #import pdb;pdb.set_trace();
            active = self.request.GET['active']
            logger_booking.info("User - "+str(self.request.user))
            if int(active):
                data = BookingDetails.objects.filter(user = self.request.user, status_code = 'B001').order_by('id').reverse()
            else:
                data = BookingDetails.objects.filter(Q(user = self.request.user), ~Q(status_code = 'B001')).order_by('id').reverse()
            logger_booking.info("Active Booking Mixin data - "+str(data))
        except Exception,e:
            logger_error.error(traceback.format_exc())
            return None
        return data

class GetActiveBookings(ActiveBookingMixin, ListAPIView):
    pass


class NewBookingRZP(CreateAPIView,UpdateAPIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = (TokenHasScope,)
    required_scopes = ['write','read']
    serializer_class = ActiveBookingSerializer


    @transaction.commit_manually
    def create(self,request,*args,**kwargs):
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
            rzp_payment_id = data['razorpay_payment_id']
            promo_amount = data['discount']
            promo_code = None
            payment_success = 0
            service_tax = data['service_tax']
            if data.has_key('promo_code'):
                promo_code = data['promo_code']
                if promo_code:
                    coupon_detail = Coupon.objects.get(coupon_code__iexact = promo_code, is_active = 1,  \
                            expiry_date__gte =  datetime.today().date())
            ##check purchase amount is not changed
            ##set total duration for the booking taking all duration on the studio
            ##make entry in purchase table
            logger_booking.info("User - "+str(user))
            try:
                studio = StudioProfile.objects.values('name','address_1', \
                    'address_2','area','in_charge_person','contact_person','contact_mobile_no',  \
                    'incharge_mobile_no','city','has_online_payment','landmark').get(id = studio_id, \
                    is_active = 1)
            except Exception,e:
                logger_error.error(traceback.format_exc())
                logger_error.error(rzp_payment_id)
                url = ('https://api.razorpay.com/v1/payments/%s/refund')%(rzp_payment_id)
                ##change refund amount if neede in future
                resp = requests.post(url, auth=(settings.RZP_KEY_ID,settings.RZP_SECRET_KEY))
                transaction.rollback()
                logger_error.error("Studio not available/active - %s"%(studio_id))
                return Response(data = data, status = status.HTTP_500_INTERNAL_SERVER_ERROR)
            if studio['has_online_payment'] is False:
                logger_error.error("No online payment")
                logger_error.error(rzp_payment_id)
                data = None
                url = ('https://api.razorpay.com/v1/payments/%s/refund')%(rzp_payment_id)
                ##change refund amount if neede in future
                resp = requests.post(url, auth=(settings.RZP_KEY_ID,settings.RZP_SECRET_KEY))
                transaction.rollback()
                return Response(data = data, status = status.HTTP_500_INTERNAL_SERVER_ERROR)
            appointment_start_time = datetime.strptime(appnt_time,'%H:%M')
            if appnt_date.date() < datetime.today().date():
                logger_error.error(rzp_payment_id)
                url = ('https://api.razorpay.com/v1/payments/%s/refund')%(rzp_payment_id)
                ##change refund amount if neede in future
                resp = requests.post(url, auth=(settings.RZP_KEY_ID,settings.RZP_SECRET_KEY))
                data  = {'data':responses.BOOKING_RESPONSES['DATE_EXPIRED']}
                logger_error.error(rzp_payment_id)
                return Response(data = data, status = status.HTTP_400_BAD_REQUEST)
            if appnt_date.date() == datetime.today().date():
                if appointment_start_time.hour < datetime.now().hour:
                        logger_error.error(rzp_payment_id)
                        url = ('https://api.razorpay.com/v1/payments/%s/refund')%(rzp_payment_id)
                        ##change refund amount if neede in future
                        resp = requests.post(url, auth=(settings.RZP_KEY_ID,settings.RZP_SECRET_KEY))
                        data  = {'data':responses.BOOKING_RESPONSES['DATE_EXPIRED']}
                        logger_error.error(rzp_payment_id)
                        data  = {'data':responses.BOOKING_RESPONSES['TIME_EXPIRED']}
                        return Response(data = data, status = status.HTTP_400_BAD_REQUEST)
                else:
                    if appointment_start_time.hour == datetime.now().hour:
                        if appointment_start_time.minute < datetime.now().minute:
                            logger_error.error(rzp_payment_id)
                            url = ('https://api.razorpay.com/v1/payments/%s/refund')%(rzp_payment_id)
                            ##change refund amount if neede in future
                            resp = requests.post(url, auth=(settings.RZP_KEY_ID,settings.RZP_SECRET_KEY))
                            data  = {'data':responses.BOOKING_RESPONSES['DATE_EXPIRED']}
                            logger_error.error(rzp_payment_id)
                            data  = {'data':responses.BOOKING_RESPONSES['TIME_EXPIRED']}
                            return Response(data = data, status = status.HTTP_400_BAD_REQUEST)
            logger_booking.info("New booking - "+str(data))
            total_duration = StudioServices.objects.filter(service_id__in = services_chosen,  \
                studio_profile_id = studio_id).values('mins_takes').aggregate(Sum('mins_takes'))
            service_details = StudioServices.objects.filter(service_id__in = services_chosen,  \
                studio_profile_id = studio_id)
            ##capture payment in razor pay
            if rzp_payment_id:
                #capture payment from razor pay
                url = ('https://api.razorpay.com/v1/payments/%s/capture')%(rzp_payment_id)
                resp = requests.post(url, data={'amount':int(purchase_amount)*100}, auth=(settings.RZP_KEY_ID,settings.RZP_SECRET_KEY))
                print resp
                if resp.status_code == 200:
                    payment_success = 1
            if payment_success == 1:
                status_code = responses.BOOKING_CODES['BOOKED']
            else:
                status_code = responses.BOOKING_CODES['FAILED']
                transaction.rollback();
                return Response(data = None, status = status.HTTP_400_BAD_REQUEST)
            new_purchase = Purchase(customer = user,  \
                purchase_amount = purchase_amount, actual_amount = actual_amount,  \
                purchase_status = 'BOOKED', service_updated = 'new booking',  \
                status_code = status_code, service_tax = service_tax)
            new_purchase.save()
            logger_booking.info("New purchase id - "+str(new_purchase.id))
            appointment_end_time = appointment_start_time + timedelta(minutes = total_duration['mins_takes__sum'])
            ##check has slots available by passing start time with duration
            new_booking = BookingDetails(user = user, booked_date =
                datetime.now(), appointment_date = appnt_date,  \
                appointment_start_time = appointment_start_time, booking_code = booking_code,  \
                studio_id = studio_id, booking_status = 'BOOKED',  \
                service_updated = 'new booking', purchase = new_purchase,status_code = status_code,  \
                appointment_end_time = appointment_end_time, mobile_no = mobile_no)
            new_booking.save()
            logger_booking.info("New booking id - "+str(new_booking.id))
            sms_bms = BookedMessageSent(booking = new_booking, type_of_message = 'book',   \
                mode = 'sms', service_updated = 'new booking', message = '')
            sms_bms.save();
            rzp_pay = RZPayment(purchase = new_purchase, rzp_payment_id = rzp_payment_id,  \
                rzp_status = 'CAPTURE', service_updated = 'new booking')
            rzp_pay.save()
            logger_booking.info("New bookmessage send id - "+str(sms_bms.id))
            for service in services_chosen:
                service_booked = BookingServices(booking = new_booking,service_id = service, service_updated = 'new booking')
                service_booked.save()
            ##services_class = ActiveBookingSerializer(new_booking)
            booking_id = new_booking.id
            studio_id = BookingDetails.objects.get(id = booking_id)
            if payment_success == 1 and studio_id.notification_send == 0:
                UserProfile.objects.filter(user_acc = user).update(mobile = mobile_no )
                services_booked = BookingServices.objects.filter(booking_id = booking_id)
                services_booked_list = [(ser.service.service_name,ser.mins_takes,ser.price) for ser in service_details]
                user = User.objects.values('first_name','email').get(email = user.email)
                contacts = {'in_charge_person':{'name':studio['in_charge_person'],'mobile_no': \
                studio['incharge_mobile_no']},'contact_person':{'name':studio['contact_person'],\
                'mobile_no':studio['contact_mobile_no']}}
                studio_address = {'address_1':studio['address_1'],'address_2':studio['address_2'],  \
                'area':studio['area'],'city':studio['city'],'landmark':studio['landmark']}
                appnt_time =  studio_id.appointment_start_time.strftime('%I:%M %p' )
                appnt_date = studio_id.appointment_date.strftime('%d-%m-%Y')
                booking_details = {'first_name':user['first_name'],'code':studio_id.booking_code,  \
                'date':appnt_date, 'appnt_time':appnt_time,  \
                'services':services_booked_list,  \
                'studio':studio['name'],'studio_address':studio_address,  \
                'contact':contacts,'total':purchase_amount,'discount':promo_amount,'service_tax':service_tax, \
                'mobile_no':mobile_no}
                logger_booking.info("Booking email data - "+str(booking_details))
                message = get_template('emails/booking.html').render(Context(booking_details))
                studio_msg = get_template('emails/studio_booking.html').render(Context(booking_details))
                to_user = user['email']
                if promo_code:
                    if not coupon_detail:
                        logger_error.error("Invalid promo code")
                        logger_error.error(rzp_payment_id)
                        url = ('https://api.razorpay.com/v1/payments/%s/refund')%(rzp_payment_id)
                        ##change refund amount if neede in future
                        resp = requests.post(url, auth=(settings.RZP_KEY_ID,settings.RZP_SECRET_KEY))
                        transaction.rollback()
                        return Response(data = None,status = status.HTTP_406_NOT_ACCEPTABLE)
                    if coupon_detail.user_based == 1:
                        CouponForUsers.objects.filter(user = user, coupon = coupon_detail,  \
                        is_active = 1, expiry_date__gte = datetime.today().date()).update(is_active = 0,  \
                        expiry_date = datetime.today().date(),service_updated = 'new booking',  \
                        updated_date_time = datetime.now())
                subject = responses.MAIL_SUBJECTS['BOOKING_EMAIL']
                sms_template = responses.SMS_TEMPLATES['BOOKING_SMS']
                sms_message = sms_template%(user['first_name'],studio['name'],appnt_date,appnt_time,studio_id.booking_code)
                email = sendEmail(to_user,subject,message)
                studio_email = StudioProfile.objects.get(id = studio_id.studio.id)
                studio_subject = (responses.MAIL_SUBJECTS['STUDIO_BOOKING_EMAIL'])%(user['first_name'])
                studio_email.studio.email = 'vbnetmithun@gmail.com' ##comment in production
                mail_to_studio = sendEmail(studio_email.studio.email,studio_subject,
                    studio_msg)
                #sms = sendSMS(studio_id.mobile_no,sms_message)
                #email = 1
                sms = 1
                review_key = uniquekey_generator()
                new_link = ReviewLink(booking_id = booking_id, link_code = review_key,  \
                    service_updated = "booking confirmed")
                new_link.save()
                try:
                    email_bms = BookedMessageSent(booking_id = booking_id,is_successful = email,  \
                        type_of_message = 'book', mode = 'email', service_updated =  \
                    'new booking')
                    sms_bms = BookedMessageSent.objects.filter(booking_id = booking_id, is_successful = 0,   \
                    type_of_message = 'book', mode = 'sms', service_updated =  \
                    'new booking', message = '').update(is_successful = sms,  \
                    service_updated = 'booking confirmed')
                    email_bms.save()
                    #sms_bms.save()
                    notification_send = 1
                    logger_booking.info("Notification sent - "+str(notification_send))
                    BookingDetails.objects.filter(id = booking_id).update(notification_send =   \
                    notification_send)
                except Exception, DBerr:
                    logger_error.error(traceback.format_exc())
                    transaction.commit();
                    return Response(data = None, status = status.HTTP_200_OK)
                data = simplejson.dumps(booking_details)
        except Exception,e:
            logger_error.error(traceback.format_exc())
            logger_error.error(rzp_payment_id)
            url = ('https://api.razorpay.com/v1/payments/%s/refund')%(rzp_payment_id)
            ##change refund amount if neede in future
            resp = requests.post(url, auth=(settings.RZP_KEY_ID,settings.RZP_SECRET_KEY))
            transaction.rollback()
            return Response(data = None,status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            transaction.commit()
            return Response(data = data, status = status.HTTP_201_CREATED)

class CancelBooking(ActiveBookingMixin,UpdateAPIView):
    def get_queryset(self):
        booking_id = self.request.DATA['booking_id']
        logger_booking.info("Cancel booking id - "+str(booking_id))
        data = BookingDetails.objects.filter(user = self.request.user,  \
            id = booking_id)
        return data

    @transaction.commit_manually
    def put(self,request,*args,**kwargs):
        try:
            booking_id = self.request.DATA
            user = self.request.user
            ##chk cancellation not happening on the same day after sending confirmation
            is_booking = BookingDetails.objects.filter(id = booking_id, user_id = user \
                , is_valid = True, booking_status = 'BOOKED').update(booking_status =  \
                'CANCELLED', service_updated = 'cancel booking',  \
                status_code = responses.BOOKING_CODES['CANCELLED'],  \
                updated_date_time = datetime.now(), is_valid = False)
            rzp_payment_id = None
            today = datetime.now()
            if is_booking:
                purchase = BookingDetails.objects.values('purchase_id','appointment_date',  \
                    'appointment_start_time','studio','booking_code').get(id = booking_id)
                studio = StudioProfile.objects.get(id = purchase['studio'])
                appnt_time =  purchase['appointment_start_time'].strftime('%I:%M %p' )
                refund_amt = Purchase.objects.values('purchase_amount').get(id = purchase['purchase_id'])
                booking_details = {'name':user.first_name,'studio':studio.name,'date':purchase['appointment_date'],  \
                'appnt_time':appnt_time,'amount':refund_amt['purchase_amount'],'booking_code':purchase['booking_code']}
                message = get_template('emails/cancelled.html').render(Context(booking_details))
                studio_message = get_template('emails/studio_cancelled.html').render(Context(booking_details))
                if today.date() == purchase['appointment_date']:
                    if today.hour < 5 and purchase['appointment_start_time'].hour < 13:
                        pass
                    elif today.hour < 12 and purchase['appointment_start_time'].hour >= 13:
                        pass
                    else:
                        transaction.rollback()
                        logger_booking.info("appointment_date and time passed"+str(booking_id))
                        return Response(status = status.HTTP_406_NOT_ACCEPTABLE)
                Purchase.objects.filter(id = purchase['purchase_id']).update(purchase_status = 'REFUND_REQUESTED',  \
                status_code = responses.PAYMENT_CODES['REFUND_REQUESTED'],  \
                service_updated = 'cancel booking', updated_date_time = datetime.now())
                rzr_pay = RZPayment.objects.values('rzp_payment_id').get(purchase_id =  \
                    purchase['purchase_id'])
                rzp_payment_id = rzr_pay['rzp_payment_id']
                if rzp_payment_id:
                    #capture payment from razor pay
                    url = ('https://api.razorpay.com/v1/payments/%s/refund')%(rzp_payment_id)
                    ##change refund amount if neede in future
                    resp = requests.post(url, auth=(settings.RZP_KEY_ID,settings.RZP_SECRET_KEY))
                    if resp.status_code == 200:
                        dat = eval(resp.text)
                        refund_id = dat['id']
                        update = RZPayment.objects.filter(purchase_id = purchase['purchase_id']).update(  \
                            rzp_status = 'REFUND_INI',refund_id = refund_id, updated_date_time = \
                            datetime.now(),service_updated = 'cancel booking')
                        refund = Refund(user = user, purchase_id = purchase['purchase_id'], \
                        booking_id = booking_id, status = 'REFUND_INI', status_code = 'REF200',  \
                        amount_refunded = refund_amt['purchase_amount'], initiated_date_time = datetime.now(), \
                        service_updated = 'cancel booking') 
                        if not update:
                            transaction.rollback()
                            logger_booking.info("Refund failed - "+str(is_booking))
                            return Response(status = status.HTTP_304_NOT_MODIFIED)
                    else:
                        transaction.rollback()
                        logger_booking.info("Refund failed - "+str(is_booking))
                        return Response(status = status.HTTP_304_NOT_MODIFIED)
                    old_link = ReviewLink.objects.get(booking_id = booking_id)
                    old_link.delete()
                    subject = responses.MAIL_SUBJECTS['CANCEL_EMAIL']
                    email = sendEmail(user.email,subject,message)
                    studio_subject = responses.MAIL_SUBJECTS['STUDIO_CANCEL_EMAIL']%(purchase['booking_code'])
                    studio.studio.email = 'vbnetmithun@gmail.com' ##comment in production
                    studio_email = sendEmail(studio.studio.email,studio_subject,studio_message)
            else:
                transaction.rollback()
                logger_booking.info("No booking with booking id - "+str(is_booking))
                return Response(status = status.HTTP_304_NOT_MODIFIED)
        except Exception,e:
            transaction.rollback()
            logger_error.error(traceback.format_exc())
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            transaction.commit()
            logger_booking.info("Booking Cancelled")
            return Response(status = status.HTTP_200_OK)


class ValidateBookingCode(UpdateAPIView, ListAPIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = (TokenHasScope,)
    required_scopes = ['write','read']
    serializer_class = ActiveBookingSerializer

    def get_queryset(self):
        booking_code = self.request.GET['booking_code']
        studio_pin = self.request.GET['studio_pin']
        today = datetime.today().date()
        logger_booking.info("validate booking code - "+str(self.request.GET))
        data = BookingDetails.objects.filter(studio_id = studio_pin, booking_code =  \
        booking_code, booking_status = 'BOOKED', status_code ='B001', is_valid = True,  \
        appointment_date = today)
        return data
    
    @transaction.commit_manually
    def put(self,request,*args,**kwars):
        try:
            #import pdb;pdb.set_trace();
            booking_code = self.request.DATA['booking_code']
            studio_pin = self.request.DATA['studio_pin']
            #studio = StudioProfile.objects.filter(studio_id = studio_pin)
            today = datetime.today().date()
            logger_booking.info("Update booking - "+str(self.request.GET))
            has_exists = BookingDetails.objects.filter(studio_id = studio_pin, booking_code =  \
            booking_code, booking_status = 'BOOKED', status_code ='B001',  \
            is_valid = True, appointment_date = today)
            if has_exists:
                BookingDetails.objects.filter(id = has_exists[0].booking_id).update(booking_status = 'USED', status_code = 'B004',  \
                service_updated = 'booking used', updated_date_time = datetime.now(), is_valid = False)
                review_key = uniquekey_generator()
                new_link = ReviewLink(booking_id = has_exists[0].booking_id, link_code = review_key,  \
                    service_updated = "booking code validated")
                new_link.save()
            if not has_exists:
                transaction.rollback()
                logger_booking.info("No booking with booking code")
                return Response(status = status.HTTP_304_NOT_MODIFIED)
        except Exception,e:
            transaction.rollback()
            logger_error.error(traceback.format_exc())
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            transaction.commit()
            return Response(status = status.HTTP_200_OK)





class AddReviews(CreateAPIView):
    authentication_classes = (OAuth2Authentication,)
    permission_classes = (TokenHasScope,)
    required_scopes = ['write','read']
    serializer_class = StudioReviewSerializer

    def create(self,request,*args,**kwargs):
        try:
            #import pdb;pdb .set_trace();
            data = self.request.DATA
            booking_id = data['booking_id']
            comment = data['comment']
            rating = data['rate']
            user = self.request.user
            logger_booking.info("Review data by user- "+ user.email +" -- " +str(data))
            is_used = BookingDetails.objects.values('status_code','studio_id','is_reviewed').get(Q(id = booking_id),  \
                ~Q(is_reviewed = 1), Q(status_code = 'B004'))
            if is_used['status_code'] == responses.BOOKING_CODES['USED'] and   \
            is_used['is_reviewed'] == 0:
                new_review = StudioReviews(studio_profile_id = is_used['studio_id'], booking_id = booking_id,  \
                comment = comment, rating = rating, user = user, service_updated = 'add review')
                new_review.save()
                ReviewLink.objects.filter(booking_id = booking_id).update(is_reviewed = 1)
                BookingDetails.objects.filter(id = booking_id).update(is_reviewed = 1)
            else:
                logger_booking.info("Review not added")
                return Response(status = status.HTTP_304_NOT_MODIFIED)
        except Exception,e:
            logger_error.error(traceback.format_exc())
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            logger_booking.info("Review added")
            return Response(status = status.HTTP_201_CREATED)


class ReviewFromEmail(CreateAPIView):
    permission_classes = (PostWithoutAuthentication,)
    serializer_class = StudioReviewSerializer
    @transaction.commit_manually
    def create(self,request,*args,**kwargs):
        try:
            data = self.request.DATA
            review_code = data['review_key'].split('&&')[0].split('=')[1]
            booking_id = data['review_key'].split('&&')[1].split('=')[1]
            comment = data['comment']
            rating = data['rating']
            is_used = BookingDetails.objects.values('status_code','studio_id','user','is_reviewed').get(Q(id = booking_id),  \
                ~Q(is_reviewed = 1), Q(status_code = 'B004'))
            if is_used['status_code'] == responses.BOOKING_CODES['USED'] and   \
            is_used['is_reviewed'] == 0:
                new_review = StudioReviews(studio_profile_id = is_used['studio_id'], booking_id = booking_id,  \
                comment = comment, rating = rating, user_id = is_used['user'], service_updated = 'review from email')
                new_review.save()
                ReviewLink.objects.filter(booking_id = booking_id).update(is_reviewed = 1)
                BookingDetails.objects.filter(id = booking_id).update(is_reviewed = 1)
            else:
                transaction.rollback()
                logger_booking.info("Review not added")
                return Response(status = status.HTTP_304_NOT_MODIFIED)
        except Exception,e:
            transaction.rollback()
            logger_error.error(traceback.format_exc())
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            transaction.commit()
            logger_booking.info("Review added")
            return Response(status = status.HTTP_201_CREATED)

class  GetSlots(APIView):
    authentication_classes = (OAuth2Authentication,)
    permission_classes = (TokenHasScope,)
    required_scopes = ['write','read']
    serializer_class = ActiveBookingSerializer
    def get(self,request,*args,**kwargs):
        try:
            data = self.request.GET
            studio = data['studio_id']
            date = data['date']
            services = data['services']
            duration = int(data['duration'])
            logger_booking.info("Get slots for - " +str(data))
            bookings = BookingDetails.objects.filter(appointment_date = date, studio_id = studio,  \
                booking_status = 'BOOKED', status_code = 'B001', is_valid = True)
            #get studio start and end time
            studio_time = StudioProfile.objects.values('opening_at',  \
                'closing_at','daily_studio_closed_from','daily_studio_closed_till',  \
                'has_online_payment').get(id = studio)
            if studio_time['has_online_payment'] is False:
                logger_error.error("No online payment")
                data = None
                return Response(data = data, status = status.HTTP_500_INTERNAL_SERVER_ERROR)
            #check whether studio is closed on that day
            start = studio_time['opening_at']
            end = studio_time['closing_at']
            closed_from = studio_time['daily_studio_closed_from']
            closed_to = studio_time['daily_studio_closed_till']
            if closed_from is None:
                closed_from = datetime.strptime('22:00:00','%H:%M:%S')
            if closed_to is None:
                closed_to = datetime.strptime('23:00:00','%H:%M:%S')
            slots = copy.deepcopy(responses.HOURS_DICT)
            #logger_booking.info("Studio time details - "+ str(start),str(end),str(closed_from),str(closed_to))
            #check  total duration not to cross closed hours or other bookings
            #import pdb;pdb.set_trace();
            if start.minute != 0:
                slots[start.hour] =  [i for i in slots[start.hour] if i >= start.minute]
            cl_end_hour = end.hour
            if end.minute != 0:
                cl_end_hour = cl_end_hour + 1
                slots[end.hour] =  [i for i in slots[end.hour] if i < end.minute]
            cl_start_hour = closed_from.hour
            if closed_from.minute != 0:
                cl_start_hour = cl_start_hour + 1
                slots[closed_from.hour] =  [i for i in   \
                slots[closed_from.hour] if i < closed_from.minute]
            if closed_to.minute != 0:
                slots[closed_to.hour] =  [i for i in   \
                slots[closed_to.hour] if i >= closed_to.minute]
            for j in range(0, start.hour):
                slots.pop(j,None)
            for k in range(cl_end_hour,24):
                slots.pop(k,None)
            for z in range(cl_start_hour,closed_to.hour):
                slots.pop(z,None)
            if len(bookings) > 0:
                for bks in bookings:
                    start_hour = bks.appointment_start_time.hour
                    start_min = bks.appointment_start_time.minute
                    end_hour = bks.appointment_end_time.hour
                    end_min = bks.appointment_end_time.minute
                    time_diff = end_hour-start_hour
                    if time_diff > 1:
                        for i in range((start_hour+1),  \
                            (end_hour)):
                            slots[i] = []
                        se_  = [s_min for s_min in slots[start_hour] if s_min  < start_min]
                        if slots.has_key(end_hour):
                            ef_  = [e_min for e_min in slots[end_hour] if e_min  >= end_min]
                            slots[end_hour] = ef_
                        slots[start_hour] = se_
                    if time_diff == 1:
                        s_  = [mins for mins in slots[start_hour] if mins  < start_min]
                        slots[start_hour] = s_
                        if slots.has_key(end_hour):
                            ef_  = [e_min for e_min in slots[end_hour] if e_min  >= end_min]
                            slots[end_hour] = ef_
                    if time_diff == 0:
                        s_  = [mins for mins in slots[start_hour] if mins  >= end_min]
                        slots[start_hour] = s_
                        
            obj = {}
            needed_slots = duration / 15
            for key, values in  slots.iteritems():
                obj[key] = []
                for val in values:
                    slot_lens = 0
                    btwn_lens = 0
                    start_ = []
                    end_ = []
                    start_time = datetime.combine(datetime.today(),dt.time(key,val))
                    end_time = start_time + timedelta(minutes = (duration - 15))
                    start_hr = start_time.time().hour
                    start_min = start_time.time().minute
                    end_hr = end_time.hour
                    end_min = end_time.minute
                    difference = end_hr- start_hr
                    start_ = [s for s in slots[start_hr] if s>= start_min]
                    if difference == 0:
                        start_ = [s for s in start_ if s <= end_min]
                    else:
                        if slots.has_key(end_hr):
                            end_ = [f for f in slots[end_hr] if f <= end_min]
                        else:
                            obj[key].append(val)
                    slot_lens = slot_lens + len(start_)  + len(end_)
                    if difference > 1:
                        for i in range((start_time.hour+1),(end_hr)):
                            if slots.has_key(i):
                                btwn_lens = btwn_lens + len(slots[i])
                    slot_lens = btwn_lens + slot_lens
                    if slot_lens != needed_slots and val not in obj[key]:
                        obj[key].append(val)
            for key, values in obj.iteritems():
                if len(values) > 0 and slots.has_key(key):
                    slots[key] = [s for s in slots[key] if s not in values]
            #import pdb;pdb.set_trace();
            if datetime.strptime(date,'%Y-%m-%d').date() == datetime.today().date():
                td_hr = datetime.now().time().hour
                td_min = datetime.now().time().minute
                for i in range(0, td_hr):
                    if i in slots:
                        slots.pop(i,None)
                if td_hr in slots:
                    new_slot = [i for i in slots[td_hr] if td_min < i]
                slots[td_hr] = new_slot
        except Exception,e:
            logger_error.error(traceback.format_exc())
            data = None
            return Response(data = data, status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            logger_booking.info("Available slots - "+str(slots))
            print slots
            data = slots
            return Response(data = data, status = status.HTTP_200_OK)


class ApplyCoupon(APIView):
    authentication_classes = (OAuth2Authentication,)
    permission_classes = (TokenHasScope,)
    required_scopes = ['write','read']
    serializer_class = CouponSerializer
    def get(self,request,*args,**kwargs):
        try:
            #import pdb;pdb.set_trace()
            data  = self.request.GET
            #services = data['services']
            coupon_code = data['coupon_code']
            #appnt_date = data['appnt_date']
            studio_id = data['studio_id']
            amount = int(data['amount'])
            user = request.user
            #check coupon code is there
            logger_booking.info("Coupon request -" +str(data))
            try:
                coupon_detail = Coupon.objects.get(coupon_code__iexact= coupon_code,is_active = 1)
            except:
                response_to_ng = simplejson.dumps(responses.COUPON_RESPONSE['INVALID_COUPON'])
                return Response(data = response_to_ng, status = status.HTTP_400_BAD_REQUEST)
            try:
                coupon_detail = Coupon.objects.get(coupon_code__iexact = coupon_code, is_active = 1,   \
                expiry_date__gte =  datetime.today().date())
            except Exception,e:
                logger_error.info(traceback.format_exc())
                response_to_ng = simplejson.dumps(responses.COUPON_RESPONSE['NO_COUPON'])
                return Response(data = response_to_ng, status = status.HTTP_400_BAD_REQUEST)
            else:
                if coupon_detail.user_based == 1:
                    is_valid = CouponForUsers.objects.filter(user = user, coupon = coupon_detail,  \
                        is_active = 1, expiry_date__gte = datetime.today().date())
                    if not is_valid:
                        response_to_ng = simplejson.dumps(responses.COUPON_RESPONSE['COUPON_EXPIRED_USED'])
                        return Response(data = response_to_ng, status = status.HTTP_400_BAD_REQUEST)
                if coupon_detail.for_all_studios != 1:
                    is_applicable = CouponForStudios.objects.filter(studio_id = studio_id,  \
                        coupon_id = coupon_detail.id, is_active = 1)
                    if len(is_applicable) != 1:
                        logger_booking.info("Coupon code not applicable")
                        response_to_ng = simplejson.dumps(responses.COUPON_RESPONSE['NOT_APPLICABLE'])
                        return Response(data = response_to_ng, status = status.HTTP_400_BAD_REQUEST)
                if coupon_detail.is_one_time == 1:
                    ##change logic if usable only once a month
                    is_applied = BookingDetails.objects.filter(Q(coupon_id = coupon_detail.id, user = user),  \
                       ~Q(booking_status = 'CANCELLED'), ~Q(status_code = 'B003'))
                    if len(is_applied) > 0:
                        logger_booking.info("Coupon code already used")
                        response_to_ng = simplejson.dumps(responses.COUPON_RESPONSE['COUPON_USED'])
                        return Response(data = response_to_ng, status = status.HTTP_400_BAD_REQUEST)
                """if coupon['services_coupon'] == 1:
                    #get coupon services 
                    for serv in services:
                        if serv.id in for_services:
                            new_amount = new_amount = serv.amount
                    if new_amount == 0:
                        response_to_ng = simplejson.dumps(responses.COUPON_RESPONSE['no_applicable_service'])
                        return Response(data = response_to_ng, status = status.HTTP_400_BAD_REQUEST)
                """
                to_deduct = 0
                if coupon_detail.min_booking_amount > 0:
                    if amount < coupon_detail.min_booking_amount:
                        logger_booking.info("Minimum booking amount not reached")
                        response_to_ng = simplejson.dumps(responses.COUPON_RESPONSE['COUPON_MIN_AMOUNT'])%(coupon_detail.min_booking_amount)
                        return Response(data = response_to_ng, status = status.HTTP_400_BAD_REQUEST)
                if coupon_detail.coupon_type == 'PERCENT' or coupon_detail.coupon_type == 'percent':
                    logger_booking.info("Coupon type is PERCENT")
                    to_deduct = (amount * coupon_detail.discount_value)/100
                if coupon_detail.coupon_type == 'FLAT' or coupon_detail.coupon_type == 'flat':
                    logger_booking.info("Coupon type is FLAT")
                    to_deduct = (amount -coupon_detail.discount_value)
                if to_deduct > coupon_detail.maximum_discount:
                    logger_booking.info("Coupon discount greater than maximum_discount")
                    to_deduct = coupon_detail.maximum_discount
        except Exception,e:
            logger_error.error(traceback.format_exc())
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            logger_booking.info("To deduct"+str(to_deduct))
            return Response(data = to_deduct, status = status.HTTP_200_OK)


class ReviewLinkValidate(APIView):
    """class which validates the review link and returns html for enter review if true else
    error message"""
    permission_classes = (ReadWithoutAuthentication,)
    serializer_class = EmailReviewLinkSerializer
    def get(self,request,*args,**kwargs):
        try:
            data = self.request.GET
            booking_id = data['booking_id']
            review_code = data['review_key']
            data = ReviewLink.objects.filter(booking_id = booking_id, link_code = review_code,  \
                is_reviewed = 0)
            if data:
                #return html
                return render(request, 'user_accounts/rating.html',{'can_review':1})
            else:
                #return error message
                return render(request, 'user_accounts/rating.html',{'can_review':0})
        except Exception,e:
            print repr(e)
            return render(request, 'user_accounts/rating.html',{'can_review':0})





"""
class NewBooking(CreateAPIView,UpdateAPIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = (TokenHasScope,)
    required_scopes = ['write','read']
    serializer_class = ActiveBookingSerializer
    
    @transaction.commit_manually
    def create(self,request,*args,**kwargs):
        try:
            import pdb;pdb.set_trace();
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
            promo_code = None
            if data.has_key('promo_code'):
                promo_code = data['promo_code']
            ##check purchase amount is not changed
            ##set total duration for the booking taking all duration on the studio
            ##make entry in purchase table
            appointment_start_time = datetime.strptime(appnt_time,'%H:%M')
            if appnt_date.date() < datetime.today().date():
                data  = {'data':responses.BOOKING_RESPONSES['DATE_EXPIRED']}
                return Response(data = data, status = status.HTTP_400_BAD_REQUEST)
            if appnt_date.date() == datetime.today().date():
                if datetime.now().hour > 5:
                    if appointment_start_time.hour < 12:
                        data  = {'data':responses.BOOKING_RESPONSES['TIME_EXPIRED']}
                        return Response(data = data, status = status.HTTP_400_BAD_REQUEST)
                    else:
                        if datetime.now().hour > 12:
                            data  = {'data':responses.BOOKING_RESPONSES['TIME_EXPIRED']}
                            return Response(data = data, status = status.HTTP_400_BAD_REQUEST)
            logger_booking.info("New booking - "+str(data))
            total_duration = StudioServices.objects.filter(service_id__in = services_chosen,  \
                studio_profile_id = studio_id).values('mins_takes').aggregate(Sum('mins_takes'))
            new_purchase = Purchase(customer = user,  \
                purchase_amount = purchase_amount, actual_amount = actual_amount,  \
                purchase_status = 'BOOKING', service_updated = 'new booking',  \
                status_code = status_code)
            new_purchase.save()
            logger_booking.info("New purchase id - "+str(new_purchase.id))
            appointment_end_time = appointment_start_time + timedelta(minutes = total_duration['mins_takes__sum'])
            ##check has slots available by passing start time with duration
            new_booking = BookingDetails(user = user, booked_date =
                datetime.now(), appointment_date = appnt_date,  \
                appointment_start_time = appointment_start_time, booking_code = booking_code,  \
                studio_id = studio_id, booking_status = 'BOOKING',  \
                service_updated = 'new booking', purchase = new_purchase,status_code = status_code,  \
                appointment_end_time = appointment_end_time, mobile_no = mobile_no)
            new_booking.save()
            logger_booking.info("New booking id - "+str(new_booking.id))
            sms_bms = BookedMessageSent(booking = new_booking, type_of_message = 'book',   \
                mode = 'sms', service_updated = 'new booking', message = '')
            sms_bms.save();
            logger_booking.info("New bookmessage send id - "+str(sms_bms.id))
            for service in services_chosen:
                service_booked = BookingServices(booking = new_booking,service_id = service, service_updated = 'new booking')
                service_booked.save()
            services_class = ActiveBookingSerializer(new_booking)
        except Exception,e:
            logger_error.error(traceback.format_exc())
            transaction.rollback()
            return Response(data = None,status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            transaction.commit()
            return Response(data = None, status = status.HTTP_201_CREATED)
    
    @transaction.commit_manually
    def put(self,request,*args,**kwargs):
        try:
            user = self.request.user
            data = self.request.DATA
            booking_status = data['booking_status']
            booking_id = data['booking_id']
            purchase_id = data['purchase_id']
            rzp_payment_id = rzp_data['razorpay_payment_id']
            payment_success = 0
            ##payment_status = data['payment_status']
            amt_paid = Purchase.objects.values('purchase_amount').get(id = Purchase)
            purchase_amount = int(amt_paid['purchase_amount']) * 100 ##only for razor pay
            logger_booking.info("Updated booking data - "+str(data))
            if rzp_payment_id:
                #capture payment from razor pay
                url = ('https://api.razorpay.com/v1/payments/%s/capture')%(rzp_payment_id)
                resp = requests.post(url, data={'amount':purchase_amount}, auth=(settings.RZP_KEY_ID,settings.RZP_SECRET_KEY))
                print resp
                if resp == 'OK':
                    payment_success = 1
            if payment_success == 1:
                status_code = responses.BOOKING_CODES['BOOKED']
            else:
                status_code = responses.BOOKING_CODES['FAILED']
                transaction.rollback();
                return Response(data = None, status = status.HTTP_400_BAD_REQUEST)
            BookingDetails.objects.filter(id = booking_id).update(booking_status =   \
            'BOOKED',service_updated = 'rzp payment capture', status_code = status_code,  \
            updated_date_time = datetime.now() )
            payment_status_code = responses.PAYMENT_CODES['PAID']

            studio_id = BookingDetails.objects.get(id = booking_id)
            Purchase.objects.filter(id = purchase_id).update(\
            purchase_status =  'PAID', service_updated = 'rzp payment capture', \
            status_code = payment_status_code, updated_date_time = datetime.now())
            if payment_success == 1 and studio_id.notification_send == 0:
                services_booked = BookingServices.objects.filter(booking_id = booking_id)
                services_booked_list = [ser.service.service_name for ser in services_booked]
                user = User.objects.values('first_name','email').get(email = user)
                studio = StudioProfile.objects.values('name','address_1', \
                'address_2','area','in_charge_person','contact_person','contact_mobile_no',  \
                'incharge_mobile_no','city').get(id = studio_id.studio.id)
                contacts = {'in_charge_person':{'name':studio['in_charge_person'],'mobile_no': \
                studio['incharge_mobile_no']},'contact_person':{'name':studio['contact_person'],\
                'mobile_no':studio['contact_mobile_no']}}
                studio_address = {'address_1':studio['address_1'],'address_2':studio['address_2'],  \
                'area':studio['area'],'city':studio['city']}
                appnt_time =  studio_id.appointment_start_time.strftime('%H:%M')
                appnt_date = studio_id.appointment_date.strftime('%d-%m-%Y')
                booking_details = {'first_name':user['first_name'],'code':studio_id.booking_code,  \
                'date':appnt_date, 'appnt_time':appnt_time,  \
                'services':services_booked_list,  \
                'studio':studio['name'],'studio_address':studio_address,  \
                'contact':contacts}
                logger_booking.info("Booking email data - "+str(booking_details))
                message = get_template('emails/booking.html').render(Context(booking_details))
                to_user = user['email']
                subject = responses.MAIL_SUBJECTS['BOOKING_EMAIL']
                sms_template = responses.SMS_TEMPLATES['BOOKING_SMS']
                sms_message = sms_template%(user['first_name'],studio['name'],studio['area'],appnt_date,appnt_time)
                #email = sendEmail(to_user,subject,message)
                #sms = sendSMS(studio_id.mobile_no,sms_message)
                email = 1
                sms_bms = 1
                try:
                    email_bms = BookedMessageSent(booking_id = booking_id,is_successful = email,  \
                        type_of_message = 'book', mode = 'email', service_updated =  \
                    'new booking')
                    sms_bms = BookedMessageSent.objects.filter(booking_id = booking_id, is_successful = 0,   \
                    type_of_message = 'book', mode = 'sms', service_updated =  \
                    'new booking', message = '').update(is_successful = sms_bms,  \
                    service_updated = 'booking confirmed')
                    email_bms.save()
                    notification_send = 1
                    logger_booking.info("Notification sent - "+str(notification_send))
                    BookingDetails.objects.filter(id = booking_id).update(notification_send =   \
                    notification_send)
                except Exception, DBerr:
                    logger_error.error(traceback.format_exc())
                    transaction.commit();
                    return Response(data = None, status = status.HTTP_200_OK)
                data = simplejson.dumps(booking_details)
        except Exception,e:
            transaction.rollback()
            logger_error.error(traceback.format_exc())
            return Response(data = None,status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            transaction.commit()
            return Response(data = data,status = status.HTTP_200_OK)"""

