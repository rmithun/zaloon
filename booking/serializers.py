#standard library imports


#third party imports
from rest_framework import serializers

#application imports
from models import *
from studios.serializers import SudioProfileSerizlier
from user_accounts.serializers import UserNameOnlySerializer



class ServiceTypeSerializer(serializers.ModelSerializer):

	"""list of available service type serializer"""
	class Meta:
		model = SerivceType
		fields = ('id', 'service_type_name', 'description', 'is_active')

class ServiceSerializer(serializers.ModelSerializer):

	"""list of available activities serializer"""
	service_type = ServiceTypeSerializer()
	class Meta:
		model = Service
		fields = ('id', 'service_type', 'service_name', 'min_duration', \
		'is_active')



class BookingDetailsSerializer(serializers.ModelSerializer):

	"""serializer for booked details"""
	studio = SudioProfileSerizlier()
	user = UserNameOnlySerializer()
	class Meta:
		model = BookingDetails
		fields = ('user', 'booked_date', 'appointment_date',  \
			'booking_code', 'apoointment_time', 'studio', 'booking_status',  \
			'booking_type', 'reminder_sent','id')


class ServiceBookedSerializer(serializers.ModelSerializer):

	"""serializer for getting the services booked"""
	booking = BookingDetailsSerializer()
	service = ServiceSerializer()
	class Meta:
		model = BookingServices
		fields = ('booking', 'service', 'status')


class MessageSentSerializer(serializers.ModelSerializer):

	"""serializer for message send check"""
	class Meta:
		model = BookedMessageSend
		fields = ('booking', 'message', 'is_successful', 'type_of_message',  \
			'mode')