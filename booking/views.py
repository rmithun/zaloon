
""" 
Views 
"""
#standard library imports
import random
import string
from datetime import timedelta, datetime
import simplejson

#third party imports
from django.shortcuts import get_object_or_404, render_to_response,redirect, \
render
from django.contrib.auth.decorators import login_required
from utils.generic_utils import *
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

#application imports
from serializers import *
from models import *
from utils.generic_utils import sendEmail, sendSMS
from utils import responses
from studios.models import StudioServices
from studios.serializers import StudioReviewSerializer



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


class NewBooking(CreateAPIView,UpdateAPIView):
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
            status_code = responses.BOOKING_CODES['BOOKING']
            promo_code = data['promo_code']
            ##set total duration for the booking taking all duration on the studio
            ##make entry in purchase table
            import pdb;pdb.set_trace();
            total_duration = StudioServices.objects.filter(service_id__in = services_chosen  \
                ).values('mins_takes').aggregate(Sum('mins_takes'))
            new_purchase = Purchase(customer = user,  \
                purchase_amount = purchase_amount, actual_amount = actual_amount,  \
                purchase_status = 'BOOKING', service_updated = 'new booking',  \
                status_code = status_code)
            new_purchase.save()
            appointment_start_time = datetime.strptime(appnt_time,'%H:%M')
            appointment_end_time = appointment_start_time + timedelta(minutes = total_duration['mins_takes__sum'])
            new_booking = BookingDetails(user = user, booked_date =
                datetime.now(), appointment_date = appnt_date,  \
                appointment_start_time = appointment_start_time, booking_code = booking_code,  \
                studio_id = studio_id, booking_status = 'BOOKING',  \
                service_updated = 'new booking', purchase = new_purchase,status_code = status_code,  \
                appointment_end_time = appointment_end_time, mobile_no = mobile_no)
            new_booking.save()
            sms_bms = BookedMessageSent(booking = new_booking, type_of_message = 'book',   \
                mode = 'sms', service_updated = 'new booking', message = '')
            sms_bms.save();
            for service in services_chosen:
                service_booked = BookingServices(booking = new_booking,service_id = service, service_updated = 'new booking')
                service_booked.save()
            #services_class = ActiveBookingSerializer(new_booking)
            response = {'booking_id':new_booking.id,'purchase_id':new_purchase.id}
            data = simplejson.dumps(response)
        except Exception,e:
            print repr(e)
            transaction.rollback()
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            transaction.commit()
            return Response(data = data, status = status.HTTP_201_CREATED)
    
    @transaction.commit_manually
    def put(self,request,*args,**kwargs):
        try:
            user = self.request.user
            data = self.request.DATA
            booking_status = data['booking_status']
            booking_id = data['booking_id']
            purchase_id = data['purchase_id']
            payment_status = data['payment_status']
            if booking_status == 'BOOKED':
                status_code = responses.BOOKING_CODES['BOOKED']
            else:
                status_code = responses.BOOKING_CODES['FAILED']
            BookingDetails.objects.filter(id = booking_id).update(booking_status =   \
            booking_status,service_updated = 'payment response', status_code = status_code,  \
            updated_date_time = datetime.now() )
            studio_id = BookingDetails.objects.get(id = booking_id)
            Purchase.objects.filter(id = purchase_id).update(\
            purchase_status =  payment_status, service_updated = 'payment response', \
            status_code = status_code, updated_date_time = datetime.now())
            if booking_status == 'BOOKED' and studio_id.notification_send == 0:
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
                    BookingDetails.objects.filter(id = booking_id).update(notification_send =   \
                    notification_send)
                except Exception, DBerr:
                    print (DBerr)
                    transaction.commit();
                    return Response(status = status.HTTP_304_NOT_MODIFIED)
                data = simplejson.dumps(booking_details)
        except Exception,e:
            transaction.rollback()
            print repr(e)
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            transaction.commit()
            return Response(data = data,status = status.HTTP_200_OK)


class CancelBooking(ActiveBookingMixin,UpdateAPIView):
    def get_queryset(self):
        booking_id = self.request.DATA['booking_id']
        data = BookingDetails.objects.filter(user = self.request.user,  \
            id = booking_id)
        return data

    @transaction.commit_manually
    def put(self,request,*args,**kwargs):
        try:
            booking_id = self.request.DATA
            user = self.request.user
            is_booking = BookingDetails.objects.filter(id = booking_id, user_id = user \
                , is_valid = True, booking_status = 'BOOKED').update(booking_status =  \
                'CANCELLED', service_updated = 'cancel booking',  \
                status_code = responses.BOOKING_CODES['CANCELLED'],  \
                updated_date_time = datetime.now(), is_valid = False)
            if is_booking:
                purchase = BookingDetails.objects.values('purchase_id').get(id = booking_id)
                Purchase.objects.filter(id = purchase['purchase_id']).update(purchase_status = 'REFUND_REQUESTED',  \
                status_code = responses.PAYMENT_CODES['REFUND_REQUESTED'],  \
                service_updated = 'cancel booking', updated_date_time = datetime.now())
            else:
                transaction.rollback()
                return Response(status = status.HTTP_304_NOT_MODIFIED)
        except Exception,e:
            transaction.rollback()
            print repr(e)
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            transaction.commit()
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
        data = BookingDetails.objects.filter(studio_id = studio_pin, booking_code =  \
        booking_code, booking_status = 'BOOKED', status_code ='B001', is_valid = True,  \
        appointment_date = today)
        return data
    
    @transaction.commit_manually
    def put(self,request,*args,**kwars):
        try:
            import pdb;pdb.set_trace();
            booking_code = self.request.DATA['booking_code']
            studio_pin = self.request.DATA['studio_pin']
            #studio = StudioProfile.objects.filter(studio_id = studio_pin)
            today = datetime.today().date()
            has_exists = BookingDetails.objects.filter(studio_id = studio_pin, booking_code =  \
            booking_code, booking_status = 'BOOKED', status_code ='B001',  \
            is_valid = True, appointment_date = today).update(booking_status = 'USED', status_code = 'B004',  \
            service_updated = 'booking used', updated_date_time = datetime.now(), is_valid = False)
            if not has_exists:
                transaction.rollback()
                return Response(status = status.HTTP_304_NOT_MODIFIED)
        except Exception,e:
            print repr(e)
            transaction.rollback()
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            transaction.commit()
            return Response(status = status.HTTP_200_OK)





class AddReviews(CreateAPIView):
    permission_classes = (OAuth2Authentication,)
    permission_classes = (TokenHasScope,)
    required_scopes = ['write','read']
    serializer_class = StudioReviewSerializer

    def create(self,request,*args,**kwargs):
        try:
            import pdb;pdb.set_trace();
            data = self.request.DATA
            booking_id = data['booking_id']
            comment = data['comment']
            rating = data['rating']
            user = self.request.user
            is_used = BookingDetails.objects.values('status_code','studio_id').get(id = booking_id)
            if is_used['status_code'] == responses.BOOKING_CODES['USED']:
                new_review = StudioReviews(studio_profile_id = is_used['studio_id'], booking_id = booking_id,  \
                comment = comment, rating = rating, user = user, service_updated = 'add review')
                new_review.save()
            else:
                return Response(status = status.HTTP_304_NOT_MODIFIED)
        except Exception,e:
            print repr(e)
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(status = status.HTTP_201_CREATED)





class  GetSlots(APIView):
    permission_classes = (OAuth2Authentication,)
    permission_classes = (TokenHasScope,)
    required_scopes = ['write','read']
    serializer_class = ActiveBookingSerializer
    def get(self,request,*args,**kwargs):
        try:
            data = request.GET['data']
            studio = data['studio_id']
            date = data['date']
            services = data['services']
            duration = data['duration']
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
            if start.minute != 0:
                slots[start] =  [slots[start].remove(i) for i in slots[start] if i < start.minute]
            if end.minute != 0:
                slots[end] =  [slots[end].remove(i) for i in slots[end] if i > end.minute]
            if closed_from.minute != 0:
                slots[closed_from] =  [slots[closed_from].remove(i) for i in   \
                slots[closed_from] if i > closed_from.minute]
            if closed_to.minute != 0:
                slots[closed_to] =  [slots[closed_to].remove(i) for i in   \
                slots[closed_to] if i < closed_to.minute]
            for j in range(0, int(start)):
                slots.pop(j,None)
            for k in range(int(end),24):
                slots.pop(k,None)
            for z in range(closed_from,closed_to):
                slots.pop(z,None)
            if len(bookings) > 0:
                for bks in bookings:
                    start_hour = bks.appointment_start_time.hour()
                    start_min = bks.appointment_start_time.minute()
                    end_hour = bks.appointment_end_time.hour()
                    end_min = bks.appointment_end_time.minute()
                    time_diff = end_hour-start_hour
                    if time_diff > 1:
                        for i in range((start_hour+1),(end_hour-1)):
                            slots.pop(i,None)
                    if time_diff == 0:
                        for mins in slots[start_hour]:
                            if mins >= start_min and mins < end_min:
                                slots[start_hour].remove[mins]
                    else:
                        for s_min in slots[start_hour]:
                            if s_min >= start_min:
                                slots[start_hour].remove(s_min)
                        for e_min in slots[end_hour]:    
                            if e_min < end_min:
                                slots[end_hour].remove[e_min]

        except Exception,e:
            print repr(e)
            data = None
            return Response(data = data, status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(data = data, status = status.HTTP_200_OK)


class ApplyCoupon(APIView):
    permission_classes = (OAuth2Authentication,)
    permission_classes = (TokenHasScope,)
    required_scopes = ['write','read']
    serializer_class = CouponSerializer
    def get(self,request,*args,**kwargs):
        try:
            import pdb;pdb.set_trace()
            data  = self.request.GET
            #services = data['services']
            coupon_code = data['coupon_code']
            #appnt_date = data['appnt_date']
            studio_id = data['studio_id']
            amount = int(data['amount'])
            user = request.user
            #check coupon code is there
            try:
                coupon_detail = Coupon.objects.get(coupon_code = coupon_code, is_active = 1,   \
                expiry_date__gte =  datetime.today().date())
            except Exception,e:
                print repr(e)
                response_to_ng = simplejson.dumps(responses.COUPON_RESPONSE['NO_COUPON'])
                return Response(data = response_to_ng, status = status.HTTP_400_BAD_REQUEST)
            else:
                if coupon_detail.for_all_studios != 1:
                    is_applicable = CouponForStudios.objects.filter(studio_id = studio_id,  \
                        coupon_id = coupon_detail.id, is_active = 1)
                    if len(is_applicable) != 1:
                        response_to_ng = simplejson.dumps(responses.COUPON_RESPONSE['NOT_APPLICABLE'])
                        return Response(data = response_to_ng, status = status.HTTP_400_BAD_REQUEST)
                if coupon_detail.is_one_time == 1:
                    ##change logic if usable only once a month
                    is_applied = BookingDetails.objects.filter(Q(coupon_id = coupon_detail.id, user = user),  \
                       ~Q(booking_status = 'CANCELLED'), ~Q(status_code = 'B003'))
                    if len(is_applied) > 0:
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
                if coupon_detail.coupon_type == 'PERCENT':
                    to_deduct = (amount * coupon_detail.discount_value)/100
                if coupon_detail.coupon_type == 'FLAT':
                    to_deduct = (amount -coupon_detail.discount_value)
                if to_deduct > coupon_detail.maximum_discount:
                    to_deduct = coupon_detail.maximum_discount
        except Exception,e:
            print repr(e)
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(data = to_deduct, status = status.HTTP_200_OK)

         