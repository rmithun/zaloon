#standard library imports


#third party imports
from rest_framework import serializers

#application imports
from models import *
from booking.serializers import  ActivitySerializer, ActivityTypeSerializer,  \
BookingDetailsSerializer



class SudioProfileSerializer(serializers.ModelSerializer):

	"""serializer to get  studio details"""
	class Meta:
		model = StudioProfile
		fields = ('id', 'studio', 'name', 'address_1', 'address_2',  \
			'city', 'country', 'area', 'state', 'landline_no_1', 'landline_no_2', \
			'mobile_no_1', 'mobile_no_2', 'contact_person_1', 'contact_person_2',  \
			'opening_at', 'closing_at', 'is_active', 'is_closed',  \
			'daily_studio_closed_from', 'daily_studio_closed_till' )

class StudioActivityTypeSerializer(serializers.ModelSerializer):

	"""serializer to get studo and available activities 
	in the studio"""
	studio = StudioProfileSerializer()
	activity_type = ActivityTypeSerializer()
	class Meta:
		model = StudioActivityTypes
		fields = ('id', 'studio','activity_type','is_active')


class StudioActivitiesSerializer(serializers.ModelSerializer):

	"""activities available in the studio"""
	studio = StudioProfileSerializer()
	activity  = ActivitySerializer()
	class Meta:
		model = StudioActivities
		fields = ('id', 'studio', 'activity', 'is_active')


class PaymentModeSerializer(serializers.ModelSerializer):

	"""serializer to get list of available payment modes"""
	class Meta:
		model = PaymentModes
		fields = ('id', 'mode', 'description', 'is_active')


class StudioAccountDetailsSerializer(serializers.ModelSerializer):

	"""serializer to get the studio account details"""
	studio = StudioProfileSerializer()
	mode_of_payment = PaymentModeSerializer()
	class Meta:
		model = StudioAccountDetails
		fields = ('id', 'studio', 'mode_of_payment', 'bank_name', 'bank_branch',  \
			'bank_ifsc', 'bank_city', 'bank_acc_number', 'min_deposit', 'max_deposit'
			)

class StudioPaymentSerializer(serializers.ModelSerializer):
	
	"""serializer to get list of payments"""
    studio = StudioProfileSerializer()
	class Meta:
		model = StudioPayment
		fields = ('id', 'studio', 'mode_of_payment', 'amount_paid', 'paid_by', \
			'paid_date')

class StudioInvoicesSerializer(serializers.ModelSerializer):
	
	"""serializers to get list of invoices for the studio"""
	studio = StudioProfileSerializer()
	class Meta:
		model = StudioInvoices
		fields = ('id', 'studio', 'amount_to_be_paid', 'last_payment_amount', \
			'last_payment_date', 'payment_requested')


class PasswordResetSerializer(serializers.ModelSerializer):

	"""get list of password resets"""
	studio = StudioProfileSerializer()
	class Meta:
		model = StudioPasswordReset
		fields = ('studio', 'password_changed_date')


class StudioBlockedDetailsSerializer(serializers.ModelSerializer):

	"""studio blocked details"""
	booking = BookingDetailsSerializer()
	class Meta:
		model = StudioBlockedDetails
		fields = ('id', 'studio', 'booking', 'blocked_from', 'blocked_till')

class CloseDatesSerializer(serializers.ModelSerializer):

	"""list of closed dates"""
	class Meta:
		model  = CloseDates
		fields = ('id', 'closed_on_day', 'closed_on_desc')

class StudioClosedDetailsSerializer(serializers.ModelSerializer):

	"""studio closed on details"""
	class Meta:
		model = StudioClosedDetails
		fields = ('id', 'closed_on', 'studio', 'is_active')


class StudioClosedFromTillSerializer(serializers.ModelSerializer):

	"""serializer to get details of studio long closed"""
	class Meta:
		model = StudioClosedFromTill
		fields = ('id', 'studio', 'closed_from_date', 'closed_till_date',  \
			'is_active')