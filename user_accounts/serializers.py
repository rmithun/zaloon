#standard library imports


#third party imports
from rest_framework import serializers

#application imports
from models import *
from django.contrib.auth.models import User

class UserNameOnlySerializer(serializers.ModelSerializer):

	"""serializer to get only name and id of the user"""
	class Meta:
		model = User
		fields = ('id','first_name', 'last_name')


class UserSerializer(serializers.ModelSerializer):

	"""serializer to get only name and id of the user"""
	class Meta:
		model = User
		fields = ('id','first_name', 'last_name','email')

class UserProfileSerializer(serializers.ModelSerializer):
	
	""" UserProfile table serializer."""
	user_acc = UserSerializer()
	class Meta:
		model = UserProfile
		fields = ('id', 'dob', 'sex', \
			'city_state', 'area', 'mobile',  \
			'user_acc')

class InviteUserSerializer(serializers.ModelSerializer):

	"""user invite table serializer"""
	class Meta:
		model = UserInvites
		fields = ('email',)