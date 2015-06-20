
#standard library imports
from datetime import datetime

#third party imports
from django.conf import settings
from django.db import models
from django.utils import timezone

#application imports
from user_accounts.models import User
from studios.models import StudioProfile, Service




class Purchase(models.Model):

	"""table holding details of all the purchases made"""
	customer = models.ForeignKey(User, related_name = "user_who_purchased")
	purchase_amount = models.FloatField()
	actual_amount = models.FloatField()
	purchase_status = models.CharField(max_length = 30)
	status_code = models.CharField(max_length = 10)
	service_updated = models.CharField(max_length = 25)
	updated_date_time = models.DateTimeField(default = datetime.now())


class Promo(models.Model):

	promo_code = models.CharField(max_length = 10)
	
class BookingDetails(models.Model):

	"""table holding all booking related infos"""
	user = models.ForeignKey(User, related_name = "booked_by_user")
	booked_date = models.DateTimeField()
	appointment_date = models.DateField()
	appointment_time = models.FloatField() # ex 13.15 14.30
	booking_code = models.CharField(max_length = 25)
	studio = models.ForeignKey(StudioProfile, related_name = "booked_on_studio")
	promo = models.ForeignKey(Promo, related_name = "applied_promo_code", null = True)
	status_code = models.CharField(max_length = 10)
	booking_status = models.CharField(max_length = 30)
	reminder_sent  = models.BooleanField(default = 0)
	is_valid = models.BooleanField(default = 1) #0- new 1-postponed
	purchase = models.ForeignKey(Purchase, related_name = "purchase_id", null = True)
	service_updated = models.CharField(max_length = 25)
	updated_date_time = models.DateTimeField(default = datetime.now())

class Refund(models.Model):

	"""table holding all refund data"""
	user = models.ForeignKey(User, related_name = "refund_to_user")
	purchase = models.ForeignKey(Purchase, related_name = "refund_from_purchase")
	booking = models.ForeignKey(BookingDetails, related_name = "refund_of_booking")
	status = models.CharField(max_length = 20)
	status_code = models.CharField(max_length = 20)
	amount_refunded = models.FloatField()
	initiated_date_time = models.DateTimeField(datetime.now())
	service_updated = models.CharField(max_length = 25)
	updated_date_time = models.DateTimeField(default = datetime.now())


class BookedMessageSend(models.Model):

	"""table holds whether booked/cancelled message sent to 
	mobile/email both for user and studio"""

	booking = models.ForeignKey(BookingDetails, related_name = "booking_id")
	message = models.TextField()
	mobile_no = models.CharField(max_length = 30)
	is_successful = models.BooleanField(default = 0)
	type_of_message = models.CharField(max_length = 25) ##book and cancel message
	mode = models.CharField(max_length = 25) ## mobile and email
	service_updated = models.CharField(max_length = 25)
	updated_date_time = models.DateTimeField(default = datetime.now())

class BookingServices(models.Model):

	"""table for services booked for a booking id"""
	booking = models.ForeignKey(BookingDetails, related_name = "service_booked_with")
	service = models.ForeignKey(Service, related_name = "service_booked")
	status = models.BooleanField(default = 1)
	service_updated = models.CharField(max_length = 25)
	updated_date_time = models.DateTimeField(default = datetime.now())

class Payments(models.Model):

	"""table holding all payment related infos"""
	amount_paid = models.FloatField()
	initiated_time = models.DateTimeField(default = datetime.now())
	confirmation_time = models.DateTimeField(default = datetime.now())
	payment_status = models.CharField(max_length = 30)
	purchase = models.ForeignKey(Purchase, related_name = "purchase_id_payment")


class StudioReviews(models.Model):

	"""reviews for studio"""
	studio_profile = models.ForeignKey(StudioProfile, related_name = "studio_review")
	user = models.ForeignKey(User, related_name = "reviewed_by_user")
	#booking = models.ForeignKey(BookingDetails, related_name = "reviewed_on_booking")
	service = models.ForeignKey(Service, related_name = "reviewed_the_service", null = True)
	rating = models.PositiveIntegerField()
	comments = models.TextField()
	is_active = models.BooleanField(default = 1)
	service_updated = models.CharField(max_length = 25)
	updated_date_time = models.DateTimeField(default = datetime.now())


class MerchantDailyReportStatus(models.Model):

	"""table holding all information status for reports sent to merchants"""
	studio = models.ForeignKey(StudioProfile, related_name = "studio_report")
	report_date = models.DateField(default = datetime.now().date())
	report = models.FileField(upload_to = 'reports/%Y/%m/%d')
	mail_sent = models.BooleanField(default = 0)
	service_updated = models.CharField(max_length = 25)
	updated_date_time = models.DateTimeField(default = datetime.now())


class DailyReminder(models.Model):

	"""table holding all daily booking reminders sent"""
	booking = models.ForeignKey(BookingDetails, related_name = "dr_for_booking")
	mobile_no = models.CharField(max_length = 30)
	status = models.BooleanField(default = 1)
	message = models.TextField()
	service_updated = models.CharField(max_length = 30)
	user = models.ForeignKey(User, related_name = "dr_for_user")
	updated_date_time = models.DateTimeField(default = datetime.now())



class HourlyReminder(models.Model):

	"""table holding all hourly booking reminders sent"""
	booking = models.ForeignKey(BookingDetails, related_name = "hr_reminder_for_booking")
	mobile_no = models.CharField(max_length = 30)
	status = models.BooleanField(default = 1)
	message = models.TextField()
	service_updated = models.CharField(max_length = 30)
	user = models.ForeignKey(User, related_name = "hr_for_user")
	updated_date_time = models.DateTimeField(default = datetime.now())


class ThanksMail(models.Model):

	"""table holding all details of thanks mail sent"""
	booking = models.ForeignKey(BookingDetails, related_name = "tm_for_booking")
	mobile_no = models.CharField(max_length = 30)
	status = models.BooleanField(default = 1)
	service_updated = models.CharField(max_length = 30)
	user = models.ForeignKey(User, related_name = "tm_for_user")
	updated_date_time = models.DateTimeField(default = datetime.now())
