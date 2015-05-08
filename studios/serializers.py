#standard library imports


#third party imports
from rest_framework import serializers

#application imports
from models import *
from studios.serializers import SudioProfileSerizlier


class SudioProfileSerizlier(serializers.ModelSerializer):

	"""serializer to get  studio details"""
	class Meta:
		model = StudioProfile