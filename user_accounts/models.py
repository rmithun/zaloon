
#standard library imports
from datetime import datetime

#third party imports
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

#application imports

class UserProfile(models.Model):

	"""table holding user related basic infos"""
	user_acc = models.OneToOneField(User, blank=True, null=True, unique=True)
	dob = models.DateField(null = True)
	sex = models.CharField(max_length = 10) # 1 - female 0 -male
	city_state = models.CharField(max_length = 60, null = True)
	area = models.CharField(max_length = 40, null = True)
	facebook_id = models.CharField(max_length = 50, blank = True)
	mobile = models.CharField(max_length = 25, null = True)
	service_updated = models.CharField(max_length = 25, null = True)
	updated_date_time = models.DateTimeField(default = datetime.now())


