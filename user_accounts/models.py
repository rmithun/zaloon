
#standard library imports
from datetime import datetime

#third party imports
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

#application imports
from booking.models import ActivityType, Activity



class Plan(models.Model):

	"""type of available plans"""
	name = models.CharField(max_length = 25)
	description = models.TextField()
	is_active = models.BooleanField(default = 1)
	active_till_date = models.DateTimeField(null = True)
	price = models.IntegerField()
	service_updated = models.CharField(max_length = 25)
	updated_date_time = models.DateTimeField(default = datetime.now())

class UserProfile(models.Model):

	"""table holding user related basic infos"""
	user_acc = models.OneToOneField(User, blank=True, null=True, unique=True)
	dob = models.DateField(null = True)
	sex = models.CharField(max_length = 10) # 1 - female 0 -male
	#country = models.CharField(max_length = 40, null = True)
	city_state = models.CharField(max_length = 60, null = True)
	area = models.CharField(max_length = 40, null = True)
	facebook_id = models.CharField(max_length = 50, blank = True)
	plan = models.ForeignKey(Plan, related_name = "user_in_plan", null = True)
	mobile = models.CharField(max_length = 25, null = True)
	#relationship = models.CharField(max_length = 25, null = True)
	service_updated = models.CharField(max_length = 25, null = True)
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


class PlanDetails(models.Model):

	"""plan description and avialble activities"""
	plan = models.ForeignKey(Plan, related_name = "plan_details")
	activity_type = models.ForeignKey(ActivityType, related_name = "type_of_activity_in_plan")
	activity = models.ForeignKey(Activity, related_name = "activity_in_plan")
	count_in_plan = models.IntegerField()
	service_updated = models.CharField(max_length = 25)
	updated_date_time = models.DateTimeField(default = datetime.now())


