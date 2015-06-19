#standard library imports


#third party imports
from rest_framework import serializers

#application imports
from models import *
from booking.models import StudioReviews


class StudioSerializer(serializers.ModelSerializer):
	class Meta:
		models = Studio
		fields = ('email', 'is_active')

class ServiceTypeSerializer(serializers.ModelSerializer):

	"""list of available service type serializer"""
	class Meta:
		model = ServiceType
		fields = ('id', 'service_type_name', 'description', 'is_active')

class ServiceSerializer(serializers.ModelSerializer):

	"""list of available activities serializer"""
	service_type = ServiceTypeSerializer()
	class Meta:
		model = Service
		fields = ('id', 'service_type', 'service_name', 'min_duration', \
		'is_active')

class StudioTypeSerializer(serializers.ModelSerializer):

	"""serializers for getting studio types"""
	class Meta:
		model = StudioType
		fields = ('type_desc',)

class StudioGroupSerializer(serializers.ModelSerializer):

	"""serializers to get studio group details"""
	class Meta:
		model = StudioGroup
		fields = ('group_name', 'address', 'city', 'country')

class StudioServicesSerializer(serializers.ModelSerializer):

	"""studio and its services details"""
	#studio_profile = StudioProfileSerializer()
	service = ServiceSerializer()
	class Meta:
		model = StudioServices
		fields = ('service','price','is_active','mins_takes')

class StudioPictureSerializer(serializers.ModelSerializer):

	class Meta:
		model = StudioPicture
		fields = ('picture',)

class StudioReviewSerializer(serializers.ModelSerializer):

	class Meta:
		model = StudioReviews
		fields = ('user','service','rating','comments','is_active')

class AmenitiesSerializer(serializers.ModelSerializer):
	class Meta:
		model = Amenities
		fields = ('amenity_name', 'is_active')

class StudioAmenitiesSerializer(serializers.ModelSerializer):

	amenity = AmenitiesSerializer()
	class Meta:
		model = StudioAmenities
		fields = ('studio_profile', 'amenity','is_active')

class StudioKindSerialier(serializers.ModelSerializer):
	class Meta:
		model = StudioKind
		fields = ('kind_desc',)

class StudioProfileSerializer(serializers.ModelSerializer):

	"""serializer to get  studio details"""
	studio_group = StudioGroupSerializer()
	studio_detail_for_activity = StudioServicesSerializer(many = True)
	studio_review = StudioReviewSerializer(many = True)
	pic_of_studio = StudioPictureSerializer(many = True)
	studio_amenities = StudioAmenitiesSerializer(many = True)
	studio_type = StudioTypeSerializer()
	studio_kind = StudioKindSerialier()
	class Meta:
		model = StudioProfile
		fields = ('id', 'studio_group','studio_type', 'name', 'address_1', 'address_2',  \
			'city', 'country', 'area', 'state', 'landline_no_1', 'landline_no_2', \
			'mobile_no_1', 'mobile_no_2', 'in_charge_person', 'contact_person',  \
			'opening_at', 'closing_at', 'is_active', 'is_closed',  \
			'daily_studio_closed_from', 'daily_studio_closed_till',   \
			'studio_detail_for_activity', 'studio_review','pic_of_studio',  \
			'studio_amenities','latitude','longitude','studio_kind')

class StudioActivitiesSerializer(serializers.ModelSerializer):

	"""activities available in the studio"""
	studio = StudioProfileSerializer()
	activity  = ServiceSerializer()
	class Meta:
		model = StudioServices
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


