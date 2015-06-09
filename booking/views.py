
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

	def create(self,request,*args,**kwards):
		try:
			user = self.request.user
			data = self.request.DATA
			appnt_date = datetime.strptime(data['appnt_date'],'%Y-%m-%d')
			appnt_time = data['appnt_time']
			chars=string.ascii_uppercase + string.digits
			booking_code = ''.join(random.choice(chars) for _ in range(6))	
			##make entry in purchase table
			new_booking = BookingDetails(user = user, booked_date = 
				datetime.today().date(), appointment_date = appnt_date,  \
				appointment_time = appnt_time, booking_code = booking_code,  \
				studio_id = data['studio'], booking_status = 'payment pending',  \
				service_updated = 'new booking' )
			new_booking.save()
		except Exception,e:
			print repr(e)
			return Response(status.HTTP_500_INTERNAL_SERVER_ERROR)
		else:
			data = new_booking
			return Response(data, status.HTTP_201_CREATED)

	def put(self,request,*args,**kwargs):
		try:
			user = self.request.user
			data = self.request.DATA
			booking_status = 'booked'
			booking_id = data['booking_id']
			reminder_sent = sendReminder(booking_id)
			BookingDetails.objects.filter(id = booking_id).update(booking_status =   \
				booking_status, reminder_sent = reminder_sent)
		except Exception,e:
			print repr(e)
			return Response(status.HTTP_500_INTERNAL_SERVER_ERROR)
		else:
			return Response(status.HTTP_200_OK)

