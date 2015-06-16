##script which send reports to all merchants about the booking
##they had previous day.The script should run every day 6AM


from datetime import datetime
import django
from booking.models import BookingDetails,BookingServices
from studios.models import StudioProfile
from utils import Responses
from django.contrib.auth.models import User

------------------------------------------------------------------------------------------------------
Name | Booking id | Services Booked | Offer code | Booking amount | Actual amount | To pay 
------------------------------------------------------------------------------------------------------

------------------------------------------------------------------------------------------------------
Total Bookings -  Total Booking amount  - Total Amount after offer - Total to pay 
------------------------------------------------------------------------------------------------------

def daily_merchant_report():
	try:
		##get all used booking for the day
        today = datetime.today().date()
        bookings = BookingDetails.objects.filter(appointment_date = today,  \
            booking_status = 'USED', status_code = '', is_valid = True)
        studios_visited = []
        to_be_print = {}
        for stud in booking:
            if stud not in studios_visited:
                studios_visited.append(stud['id'])
                services_booked = BookingServices.objects.filter(booking_id = stud['id'])
                services = []
                for sun in services_booked:
                    services.append(sun['service'].service_name)
                obx = {}
                obx['studio_id'] =  stud['studio_id']
                obx['data'] = []
                obj = {}
                obj['studio_name'] = stud['studio'].name 
                obj['booking_id'] = stud['id']
                obj['services_booked'] = services[:]
                obj['offer_code'] = stud['promo'].promo_code
                obj['booking_amount'] = stud['purchase'].purchase_amount
                obj['actual_amount'] = stud['purchase'].actual_amount
                obj['amount_to_pay'] = (obj['booking_amount'] - (obj['booking_amount']/10))
                obx['data'].append(obj)
                to_print[stud['studio_id']] = obx
            else:
                to_print['']



