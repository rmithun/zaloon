#standard library imports


#third party imports
from rest_framework import serializers

#application imports
from models import *
from booking.serializers import  ActivitySerializer, ActivityTypeSerializer

class UserProfileSerializer(serializers.ModelSerializer):
	
	""" UserProfile table serializer."""
	
	class Meta:
		model = UserProfile
		fields = ('id','first_name', 'last_name', 'date_of_birth', 'sex', \
			'country', 'city', 'area', 'email', 'plan', 'mobile',  \
			'relationship', 'last_login')


class UserActivitySerializer(serializers.ModelSerializer):

	"""list of activities available for user"""
	activity = ActivitySerializer()
	activity_type = ActivityTypeSerializer()
	user = UserProfileSerializer()
	class Meta:
		model = UserActivitiesList
		fields = ('id', 'activity', 'activity_type', 'user', 'count_available', \
			'count_used', 'total_count', 'expires_on', 'is_active')

class PlanSerializer(serializers.ModelSerializer):

	"""list of available plans"""
	class Meta:
		model = Plan
		fields = ('name', 'description', 'is_active', 'active_till_date',  \
			'price')

class PlanDetailsSerializer(serializers.ModelSerializer):

	"""plan details"""
	plan = PlanSerializer()
	activity = ActivitySerializer()
	activity_type = ActivityTypeSerializer()
	class Meta:
		model = PlanDetails
		fields = ('plan', 'activity_type', 'activity', 'count_in_plan')
