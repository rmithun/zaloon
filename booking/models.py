
#standard library imports
from datetime import datetime

#third party imports
from django.conf import settings
from django.db import models
from django.utils import timezone

#application imports
#from user_accounts.models import UserProfile


class ActivityType(models.Model):

	"""type of activities available"""
	activity_type_name = models.CharField(max_length = 25)
	description = models.TextField()
	is_active = models.BooleanField(default = 1)
	service_updated = models.CharField(max_length = 25)
	updated_date_time = models.DateTimeField(default = datetime.now())

class Activity(models.Model):

	"""table holding all list of activities"""

	activity_name = models.CharField(max_length = 25)
	activity_type = models.ForeignKey(ActivityType, related_name = "type_of_activity")
	#is_dependent = models.BooleanField(default = 0)
	min_duration = models.IntegerField() ##duration in mins
	is_active = models.BooleanField(default = 1)
	unit_price = models.IntegerField()
	service_updated = models.CharField(max_length = 25)
	updated_date_time = models.DateTimeField(default = datetime.now())

class BookingDetails(models.Model):

	"""table holding all booking related infos"""
	#user = models.ForeignKey(UserProfile, related_name = "booked_by_user")
	activity = models.ForeignKey(Activity, related_name = "activity_booked")
	count_booked = models.IntegerField()
	scheduled_at = models.DateTimeField()
	booking_code = models.CharField(max_length = 25)
	expires_on = models.DateTimeField()
	#studio = models.ForeignKey(StudioProfile, related_name = "booked_on_studio")
	#promo_code = models.ForeignKey(Promo, related_name = "applied_promo_code", null = True)
	booking_status = models.BooleanField(default = 1) 
	reminder_sent  = models.BooleanField(default = 0)
	user_arrived = models.BooleanField(default = 0)
	service_updated = models.CharField(max_length = 25)
	updated_date_time = models.DateTimeField(default = datetime.now())

class BookedMessageSend(models.Model):

	"""table holds whether booked/cancelled message sent to 
	mobile/email both for user and studio"""

	booking = models.ForeignKey(BookingDetails, related_name = "booking_id")
	message = models.TextField()
	is_successful = models.BooleanField(default = 0)
	type_of_message = models.CharField(max_length = 25) ##book and cancel message
	mode = models.CharField(max_length = 25) ## mobile and email
	service_updated = models.CharField(max_length = 25)
	updated_date_time = models.DateTimeField(default = datetime.now())
