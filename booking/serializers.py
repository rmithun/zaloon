#standard library imports


#third party imports
from rest_framework import serializers

#application imports
from models import *
#from studios.serializers import StudioProfileSerializer
from user_accounts.serializers import UserNameOnlySerializer
from studios.serializers import StudioProfileSerializer, ServiceSerializer

class ServicesBooked(serializers.ModelSerializer):

    service = ServiceSerializer()
    class Meta:
		model = BookingServices
		fields = ('service',)

class ActiveBookingSerializer(serializers.ModelSerializer):

	"""list of available active bookings for user"""
	#studio = StudioProfileSerializer(many = True)
	service_booked_with = ServicesBooked(many = True)
	class Meta:
		model = BookingDetails
		fields = ('id', 'user', 'booked_date', 'appointment_date', 'apoointment_time',  \
			'booking_code','studio','booking_status','reminder_sent','booking_type',  \
			'service_booked_with')