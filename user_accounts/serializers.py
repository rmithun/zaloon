#standard library imports


#third party imports
from rest_framework import serializers

#application imports
from models import *

class UserProfileSerializer(serializers.ModelSerializer):
	
	""" UserProfile table serializer."""
	
	class Meta:
		model = UserProfile
		fields = ('id', 'date_of_birth', 'sex', \
			'country', 'city', 'area','facebook_id', 'plan', 'mobile',  \
			'relationship', 'last_login','user_acc')

class UserNameOnlySerializer(serializers.ModelSerializer):

	"""serializer to get only name and id of the user"""
	class Meta:
		model = UserProfile
		fields = ('id','first_name', 'last_name')

