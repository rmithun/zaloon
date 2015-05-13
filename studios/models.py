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


class StudioProfile(models.Model):

	"""studio basic details"""
	#studio = models.ForeignKey(StudioLogin, related_name = "studio_detail")
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
	contact_person_1 = models.CharField(max_length = 75)
	contact_person_2 = models.CharField(max_length = 75, null = True)
	opening_at = models.PositiveSmallIntegerField()
	closing_at = models.PositiveSmallIntegerField()
	is_active = models.BooleanField(default  = 1)
	contract_start_date = models.DateTimeField()
	contract_end_date = models.DateTimeField()
	last_login = models.DateTimeField(default = datetime.now())
	first_login = models.DateTimeField(default = datetime.now())
	is_closed = models.BooleanField(default = 1)
	daily_studio_closed_from = models.PositiveSmallIntegerField()
	daily_studio_closed_till = models.PositiveSmallIntegerField()
	#studio_close_timing = models.PositiveSmallIntegerField()
	service_updated = models.CharField(max_length = 25)
	updated_date_time = models.DateTimeField(default = datetime.now())


class StudioActivityTypes(models.Model):

	"""list of available activity type in studio"""
	#studio = models.ForeignKey(StudioLogin, related_name = "studio_detail_for_type")
	activity_type = models.ForeignKey(ActivityType, related_name = "type_of_activity_in_studio")
	is_active = models.BooleanField(default = 1)
	service_updated = models.CharField(max_length = 25)
	updated_date_time = models.DateTimeField(default = datetime.now())


class StudioActivities(models.Model):

	"""list of available activities in studio"""

	#studio = models.ForeignKey(StudioLogin, related_name = "studio_detail_for_activity")
	activity = models.ForeignKey(Activity, related_name = "activity_in_studio")
	is_active = models.BooleanField(default = 1)
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

class StudioBlockedDetails(models.Model):

	"""all booking details for studio"""

	#studio = models.ForeignKey(StudioLogin, related_name = "studio_booked_details")
	activity = models.ForeignKey(Activity, related_name = "activity_blocked_in_studio")
	booking = models.ForeignKey(BookingDetails, related_name = "booking_id_for_studio")
	blocked_from = models.DateTimeField()
	blocked_till = models.DateTimeField()
	is_active = models.BooleanField(default = 1)
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


class StudioDailyInvoice(models.Model):

	"""daily booked details for a studio"""
	#studio = models.ForeignKey(StudioLogin, related_name = "studio_daily_invoice")
	booked_date = models.DateTimeField()
	activity_booked = models.ForeignKey(Activity, related_name = "daily_invoice_booked_activity")
	count_booked = models.PositiveIntegerField()
	booking = models.ForeignKey(BookingDetails, related_name = "booking_for_daily_invoice")
	is_filled = models.NullBooleanField()
	service_updated = models.CharField(max_length = 25)
	updated_date_time = models.DateTimeField(default = datetime.now())
















