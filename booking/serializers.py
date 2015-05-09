#standard library imports


#third party imports
from rest_framework import serializers

#application imports
from models import *
from studios.serializers import SudioProfileSerizlier
from user_accounts.serializers import UserNameOnlySerializer

class ActivityTypeSerializer(serializers.ModelSerializer):

	"""list of available activity type serializer"""
	class Meta:
		model = Activity
		fields = ('id', 'activity_type_name', 'description', 'is_active')

class ActivitySerializer(serializers.ModelSerializer):

	"""list of available activities serializer"""
	activity_type = ActivityTypeSerializer()
	class Meta:
		model = Activity
		fields = ('id', 'activity_type', 'activity_name', 'min_duration', \
		'is_active', 'unit_price')

class BookingDetailsSerializer(serializers.ModelSerializer):

	"""serializer for booked details"""
	studio = SudioProfileSerizlier()
	user = UserNameOnlySerializer()
	class Meta:
		model = BookingDetails
		fields = ('user', 'activity', 'count_booked', 'scheduled_at',  \
			'booking_code', 'expires_on', 'studio', 'promo_code',  \
			'booking_status', 'reminder_sent')

class MessageSentSerializer(serializers.ModelSerializer):

	"""serializer for message send check"""
	class Meta:
		model = BookedMessageSend
		fields = ('booking', 'message', 'is_successful', 'type_of_message',  \
			'mode')