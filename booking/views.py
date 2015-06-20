
""" 
Views 
"""
#standard library imports
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
			##make entry in purchase table
			new_purchase = Purchase(customer = user,  \
				purchase_amount = purchase_amount, actual_amount = actual_amount,  \
				purchase_status = 'payment pending', service_updated = 'new booking',  \
				status_code = 'NBS01')
			new_purchase.save()
			new_booking = BookingDetails(user = user, booked_date = 
				datetime.now(), appointment_date = appnt_date,  \
				appointment_time = appnt_time, booking_code = booking_code,  \
				studio_id = data['studio'], booking_status = 'payment pending',  \
				service_updated = 'new booking', purchase = purchase,status_code = 'NBS01')
			new_booking.save()
			for service in services_chosen:
			    service_booked = BookingServices(booking = new_booking,  \
			    	service_id = service, service_updated = 'new booking')
			    service_booked.save()
		except Exception,e:
			print repr(e)
			return Response(status.HTTP_500_INTERNAL_SERVER_ERROR)
		else:
			data = new_booking
			return Response(data, status.HTTP_201_CREATED)
    
    @transaction.commit_manually
    def put(self,request,*args,**kwargs):
		try:
			user = self.request.user
			data = self.request.DATA
			booking_status = data['booking_status']
			booking_id = data['booking_id']
			payment_status = data['payment_status']
			reminder_sent = 0
			status_code = 'PF01'
			if booking_status == 'booked':
				reminder_sent = sendReminder(booking_id,'booked')
				status_code = 'PS01'
			BookingDetails.objects.filter(id = booking_id).update(booking_status =   \
				booking_status, reminder_sent = reminder_sent, \
				service_updated = 'payment response', status_code = status_code,  \
				updated_date_time = datetime.now() )
			purchase_id = BookingDetails.objects.filter(id = booking_id).values('purchase_id')
			Purchase.objects.filter(id = purchase_id).update(  \
				purchase_status =  payment_status, service_updated = 'payment response', \
				status_code = status_code, updated_date_time = datetime.now())
		except Exception,e:
			print repr(e)
			return Response(status.HTTP_500_INTERNAL_SERVER_ERROR)
		else:
			return Response(status.HTTP_200_OK)


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
    			'cancelled', service_updated = 'cancel booking',  \
    			status_code = 'CSBUK03', updated_date_time = datetime.now())
    	except Exception,e:
    		print repr(e)
    		return Response(HTTP_500_INTERNAL_SERVER_ERROR)
    	else:
    		return Response(status.HTTP_200_OK)

class ValidateBookingCode(RetrieveUpdateAPIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = (TokenHasScope,)
    required_scopes = ['write','read']
    serializer_class = ActiveBookingSerializer
    def get_queryset(self):
        booking_code = self.request.DATA['booking_code']
        studio = self.request.DATA['studio']
        data = BookingDetails.objects.filter(studio_id = studio, booking_code =  \
	 	booking_code, booking_status = 'BOOKED', status_code ='B001', is_valid = True)
        return data
    
    @transaction.commit_manually
    def put(self,request,*args,**kwars):
        try:
            booking_code = self.request.DATA['booking_code']
            studio = self.request.DATA['studio']
            BookingDetails.objects.filter(studio_id = studio, booking_code =  \
		    booking_code, booking_status = 'BOOKED', status_code ='B001',  \
		    is_valid = True).update(booking_status = 'USED', status_code = 'B004',  \
		    service_updated = 'booking used', updated_date_time = datetime.now())
        except Exception,e:
			print repr(e)
			return Response(status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
			return Response(status.HTTP_200_OK)



		

