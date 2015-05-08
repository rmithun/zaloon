
#standard library imports
from datetime import datetime

#third party imports
from django.conf import settings
from django.db import models
from django.utils import timezone

#application imports
from booking.models import Activity,ActivityType


class UserProfile(models.Model):

	"""table holding user related basic infos"""
	first_name = models.CharField(max_length = 70)
	last_name = models.CharField(max_length = 70, null = True)
	date_of_birth = models.DateField(null = True)
	sex = models.NullBooleanField()
	country = models.CharField(max_length = 40, null = True)
	city = models.CharField(max_length = 40, null = True)
	area = models.CharField(max_length = 40, null = True)
	email = models.CharField(max_length = 120)
	plan = models.ForeignKey(Plan, related_name = "user_in_plan")
	mobile = models.CharField(max_length = 25, null = True)
	relation_ship = models.CharField(max_length = 25, null = True)
	signup_date = models.DateTimeField(default = datetime.now())
	last_login = models.DateTimeField(default = datetime.now())
	service_updated = models.CharField(max_length = 25)
	updated_date_time = models.DateTimeField(default = datetime.now())


class UserActivitiesList(models.Model):

	"""table holding user activity availablity details"""
	user = models.ForeignKey(UserProfile, related_name = "user_activity_availablilty")
	activity = models.ForeignKey(Activity, related_name = "activity_available_for_user")
	activity_type = models.ForeignKey(ActivityType, related_name = "type_of_activity_available_for_user")
	count_available = models.IntegerField()
	count_used = models.IntegerField()
	total_count  = models.IntegerField()
	expires_on =  models.DateTimeField()
	service_updated = models.CharField(max_length = 25)
	updated_date_time = models.DateTimeField(default = datetime.now())
	is_active = models.BooleanField(default = 1)


class Plan(models.Model):

	"""type of available plans"""
	name = models.CharField(max_length = 25)
	description = models.TextField()
	is_active = models.BooleanField(default = 1)
	active_till_date = models.DateTimeField(null = True)
	price = models.IntegerField()
	service_updated = models.CharField(max_length = 25)
	updated_date_time = models.DateTimeField(default = datetime.now())


class PlanDetails(models.Model):

	"""plan description and avialble activities"""
	plan = models.ForeignKey(Plan, related_name = "plan_details")
	activity_type = models.ForeignKey(ActivityType, related_name = "type_of_activity_in_plan")
	activity = models.ForeignKey(Activity, related_name = "activity_in_plan")
	count_in_plan = models.IntegerField()
	service_updated = models.CharField(max_length = 25)
	updated_date_time = models.DateTimeField(default = datetime.now())
	







