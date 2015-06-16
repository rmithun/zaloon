##script which send reports to all merchants about the booking
##they had previous day.The script should run every day 6AM


from datetime import datetime
import django
from booking.models import BookingDetails,BookingServices
from studios.models import StudioProfile
from utils import Responses
from django.contrib.auth.models import User

------------------------------------------------------------------------------------------------------
Name | Booking id | Services Booked | Offer code | Booking amount | Offer amount | To pay 
------------------------------------------------------------------------------------------------------

------------------------------------------------------------------------------------------------------
Total Bookings -  Total Booking amount  - Total Amount after offer - Total to pay 
------------------------------------------------------------------------------------------------------

def daily_merchant_report():
	try:
		##get all used booking for the day
		from django.db import connection
        cursor = connection.cursor()
        today = datetime.today().date()
        all_data = cursor.execute('''select * from booking_bookingdetails db join booking_bookingservices  \
        bs on bd.id = bs.booking_id where  appointment_date = %s and booking_status = %s  \
         and  is_valid = 1''' %(today,'USED'))
        rows = cursor.fetchall()
        for every in rows:
        	services = cursor.execute('''select * from booking_bookingservices where  \
        		booking_id = %s'''%(every.id))
