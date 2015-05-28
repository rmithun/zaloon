#standard library imports
from datetime import datetime

#third party imports
from django.conf import settings
from django.db import models
from django.utils import timezone

#application imports
#from user_accounts.models import UserProfile
from booking.models import ActivityType,Activity, BookingDetails	

#class StudioLogin(models.Model):

#	"""studio login details"""
#	email = 


class StudioType(models.Model):

	"""type of studios"""
	type_desc = models.CharField(max_length = 50)
	is_active = models.BooleanField(default = 1)
	service_updated = models.CharField(max_length = 25)
	updated_date_time = models.DateTimeField(default = datetime.now())


class StudioGroup(models.Model):

	"""table for holding studio groups"""
	group_name = models.CharField(max_length = 50)
	studio_type = models.ForeignKey(StudioType, related_name = "studio_group_type")
	address = models.TextField()
	city = models.CharField(max_length = 40)
	country = models.CharField(max_length = 40)
	landline_no_1 = models.CharField(max_length = 40, null = True)
	landline_no_2 = models.CharField(max_length = 40, null = True)
	mobile_no_1 = models.CharField(max_length = 40)
	mobile_no_2 = models.CharField(max_length = 40, null = True)
	contact_person_1 = models.CharField(max_length = 75)
	contact_person_2 = models.CharField(max_length = 75, null = True)
	primary_email  = models.CharField(max_length = 50)
	secondary_email = models.CharField(max_length = 50)
	total_branches = models.PositiveIntegerField()
	service_updated = models.CharField(max_length = 25)
	updated_date_time = models.DateTimeField(default = datetime.now())
	


class StudioProfile(models.Model):

	"""studio basic details"""
	#studio = models.ForeignKey(StudioLogin, related_name = "studio_detail")
	studio_group = models.ForeignKey(StudioGroup, related_name = "studio_of_group")
	name = models.CharField(max_length = 120)
	address_1 = models.CharField(max_length = 200)
	address_2 = models.CharField(max_length = 200)
	city = models.CharField(max_length = 40)
	country = models.CharField(max_length = 40)
	area = models.CharField(max_length = 40)
	state = models.CharField(max_length = 40)
	landline_no_1 = models.CharField(max_length = 40, null = True)
	landline_no_2 = models.CharField(max_length = 40, null = True)
	mobile_no_1 = models.CharField(max_length = 40)
	mobile_no_2 = models.CharField(max_length = 40, null = True)
	in_charge_person = models.CharField(max_length = 75)
	contact_person  = models.CharField(max_length = 75, null = True)
	opening_at = models.PositiveSmallIntegerField()
	closing_at = models.PositiveSmallIntegerField()
	is_active = models.BooleanField(default  = 1)
	#contract_start_date = models.DateTimeField()
	#contract_end_date = models.DateTimeField()
	is_closed = models.BooleanField(default = 1)
	daily_studio_closed_from = models.PositiveSmallIntegerField()
	daily_studio_closed_till = models.PositiveSmallIntegerField()
	service_updated = models.CharField(max_length = 25)
	updated_date_time = models.DateTimeField(default = datetime.now())


class StudioServices(models.Model):

	"""list of available activities in studio"""

	studio_profile = models.ForeignKey(StudioProfile, related_name = "studio_detail_for_activity")
	activity = models.ForeignKey(Activity, related_name = "activity_in_studio")
	is_active = models.BooleanField(default = 1)
	mins_takes = models.PositiveIntegerField()
	price = models.FloatField()
	service_updated = models.CharField(max_length = 25)
	updated_date_time = models.DateTimeField(default = datetime.now())


class StudioStaffCounts(models.Model):

	"""table holding studio staff count on normal day and holiday day"""
	studio_profile = models.ForeignKey(StudioProfile, related_name = "studio_staff_count")
	normal_day = models.PositiveIntegerField()
	holiday = models.PositiveIntegerField()
	festive_season = models.PositiveIntegerField()
	service_updated = models.CharField(max_length = 25)
	updated_date_time = models.DateTimeField(default = datetime.now())
	

class PaymentModes(models.Model):

	"""payment modes available"""

	mode = models.CharField(max_length = 40)
	description = models.CharField(max_length = 75)
	is_active = models.BooleanField(default = 1)
	service_updated = models.CharField(max_length = 25)
	updated_date_time = models.DateTimeField(default = datetime.now())

class StudioAccountDetails(models.Model):

	"""studio bank and payment details"""
	#studio = models.ForeignKey(StudioLogin, related_name = "studio_account_detail")
	mode_of_payment = models.ForeignKey(PaymentModes, related_name = "payment_mode_for_studio_account")
	bank_name = models.CharField(max_length = 120)
	bank_branch = models.CharField(max_length = 120)
	bank_ifsc = models.CharField(max_length = 25)
	bank_city = models.CharField(max_length = 40)
	bank_acc_number = models.CharField(max_length = 120)
	min_deposit = models.PositiveIntegerField()
	max_deposit = models.PositiveIntegerField()
	service_updated = models.CharField(max_length = 25)
	updated_date_time = models.DateTimeField(default = datetime.now())


class StudioPayment(models.Model):

	"""all payement details for a studio"""
	#studio = models.ForeignKey(StudioLogin, related_name = "studio_payment_detail")
	mode_of_payment = models.ForeignKey(PaymentModes, related_name = "payment_mode_for_studio_payments")
	amount_paid = models.PositiveIntegerField()
	paid_by = models.CharField(max_length = 120) ##has to be foreign key in future
	paid_date = models.DateTimeField(default = datetime.now())
	service_updated = models.CharField(max_length = 25)
	updated_date_time = models.DateTimeField(default = datetime.now())


class StudioInvoices(models.Model):

	"""all invoice details for studio"""
	#studio = models.ForeignKey(StudioLogin, related_name = "studio_invoice_detail")
	amount_to_be_paid = models.PositiveIntegerField()
	last_payment_amount = models.PositiveIntegerField()
	last_payment_date = models.DateTimeField()
	payment_requested = models.BooleanField(default = 0)
	service_updated = models.CharField(max_length = 25)
	updated_date_time = models.DateTimeField(default = datetime.now())

class StudioPasswordReset(models.Model):

	"""all password resets for studio"""

	#studio = models.ForeignKey(StudioLogin, related_name = "studio_pwd_reset")
	password_changed_date = models.DateTimeField(default = datetime.now())
	service_updated = models.CharField(max_length = 25)
	updated_date_time = models.DateTimeField(default = datetime.now())


class CloseDates(models.Model):

	"""general closed days for studios"""
	closed_on_day = models.CharField(max_length = 25)
	closed_on_desc = models.CharField(max_length = 50)
	service_updated = models.CharField(max_length = 25)
	updated_date_time = models.DateTimeField(default = datetime.now())


class StudioClosedDetails(models.Model):

	"""days on which the studio is closed"""
	#studio = models.ForeignKey(StudioLogin, related_name = "studio_closed_details")
	closed_on = models.ForeignKey(CloseDates, related_name = "studio_close_dates")
	is_active = models.BooleanField(default = 1)
	service_updated = models.CharField(max_length = 25)
	updated_date_time = models.DateTimeField(default = datetime.now())


class StudioClosedFromTill(models.Model):

	"""if studio is closed for to many days"""
	#studio = models.ForeignKey(StudioLogin, related_name = "studio_long_closed_details")
	closed_from_date = models.DateField()
	closed_till_date = models.DateField()
	is_active = models.BooleanField(default = 1)
	service_updated = models.CharField(max_length = 25)
	updated_date_time = models.DateTimeField(default = datetime.now())


















