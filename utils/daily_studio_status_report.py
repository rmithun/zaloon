##script which sends daily status report to Studios
##for the  previous day. It will pick all the validated bookings
##and send the booking details, amount to be paid to Studios
###will send message only when booking is there for studio, 
##chnage the functionality to send empty PDF with no booking message in future



from datetime import datetime
import django
from booking.models import BookingDetails
from studios.models import StudioProfile
from utils import Responses
from django.contrib.auth.models import User


#get all validated bookings
##get the studio details
##make PDF for every studio
##send email
##make entry in daily status report table


def prepare_status_report():
	try:
	    today = datetime.today().date()
	    bookings = BookingDetails.objects.filter(appointment_date = today,   \
            booking_status = 'USED', booking_code = 'B004')
	    
