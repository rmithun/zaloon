##script which send reminder notification for all the booked users
##for the day. This differes from every hour notification script
##this runs every day at 7 AM



from datetime import datetime
import django
from booking.models import BookingDetails
from studios.models import StudioProfile
from utils import Responses
from django.contrib.auth.models import User


##get all active bookings for the day
##get the code,date, time, studio, services
#get mobile number from BookedMessageSend
##get SMS template 
##send SMS
##Make an entry in daily_reminder table with status	


##need to integrate with thread que system when the count overflows in future
def get_Bookings_for_day():
	try:
	    today = datetime.today().date()
            bookings = BookingDetails.objects.filter(appointment_date = today,   \
            booking_status = 'booked', booking_code = 'SBUK01')
            ##log code starting
            for every_book in bookings:
        	code = every_book['booking_code']
        	studio_name = StudioProfile.objects.filter(id = every_book['studio']).values('name')
        	user_name = User.objects.filter(id = every_book['user']).values('first_name')
        	date = today
                time = datetime.strptime(str(every_book['appointment_time']), "%H.%M").strftime("%I:%M %p")
        	mobile_no = BookedMessageSend.objects.filter(booking_id = every_book['id']).values('mobile_no')
        	sms_template = (Responses.daily_reminder['sms_template'])%(user_name, studio_name, date, time,code)
        	try:
        	    sendSMS(mobile_no,sms_template)
        	    status = True
        	except Exception,smserr:
        		print repr(smserr)
        		status = False
        		daily_reminder = DailyReminder(booking_id = every_book['id'], mobile_no = mobile_no,  \
        	    	status = status, service_updated = "daily reminder", message = "sms_template",  \
        	    	)
        	else:
        		daily_reminder = DailyReminder(booking_id = every_book['id'], mobile_no = mobile_no,  \
        	    	status = status, service_updated = "daily reminder", message = "sms_template",  \
        	    	)
        ###log code end stats
        except Exception,error:
                print error
        else:
                print len(bookings)
        ###log code end stats


get_Bookings_for_day()



