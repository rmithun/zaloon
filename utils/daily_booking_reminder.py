##script which send reminder notification for all the booked users
##for the day. This differes from every hour notification script
##this runs every day at 7 AM


import os,sys
import django
sys.path.append(os.path.join(os.path.dirname(__file__), 'onepass'))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..')))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "onepass.settings")
django.setup()


from datetime import datetime
import logging
import traceback
from booking.models import BookingDetails,DailyReminder
from studios.models import StudioProfile
from utils import responses, generic_utils
from django.contrib.auth.models import User

logger_booking = logging.getLogger('log.daily_scripts')
logger_error = logging.getLogger('log.errors')


#application imports
##get all active bookings for the day
##get the code,date, time, studio, services
#get mobile number from BookedMessageSend
##get SMS template 
##send SMS
##Make an entry in daily_reminder table with status	


today = datetime.today().date()
buks = None
##need to integrate with thread queue system when the count overflows in datetime.date(2015, 7, 1) future
def get_Bookings_for_day():
    try:
        bookings = BookingDetails.objects.filter(appointment_date = today,   \
            booking_status = 'BOOKED', status_code = 'B001', is_valid = True)
        ##log code starting
        for every_book in bookings:
            has_sent  = DailyReminder.objects.filter(booking_id = every_book.id, status = True)
            if len(has_sent) is 0:
                code = every_book.booking_code
                #studio_name = StudioProfile.objects.values('name','area').get(id = every_book.studio.id)
                #user_name = User.objects.values('first_name','id','email').get(id = every_book.user.id)
                date = today
                time = datetime.strptime(str(every_book.appointment_start_time), "%H:%M:%S").strftime("%I:%M %p")
                ##get sms template
                mobile_no = every_book.mobile_no
                sms_template = (responses.SMS_TEMPLATES['DLY_REM'])%(every_book.user.first_name,  \
                every_book.studio.name,every_book.studio.area, date, time,code)
                logger_booking.info("sms message - "+str(sms_template))
                try:
                    ##remove email and set to sms
                    ##status = generic_utils.sendSMS(mobile_no,sms_template) uncomment while sending sms
                    status = generic_utils.sendEmail(every_book.user.email, 'Booking confirmation SMS', sms_template)
                except Exception,smserr:
                    logger_error.error(traceback.format_exc())
                    status = False
                    daily_reminder = DailyReminder(booking_id = every_book.id, mobile_no = mobile_no,  \
        	            status = status,user_id = every_book.user.id,service_updated = "daily reminder", message = sms_template,  \
        	    	    )
                    daily_reminder.save()
                else:
        	        daily_reminder = DailyReminder(booking_id = every_book.id, mobile_no = mobile_no,  \
        	    	status = status,user_id = every_book.user.id, service_updated = "daily reminder", message = sms_template)
                        daily_reminder.save()

            ###log code end stats
    except Exception,errorz:
        logger_error.error(traceback.format_exc())
    else:
        global buks
        buks = len(bookings)
        logger_booking.info("Total reminder SMS sent - "+str(buks))
    ###log code end stats


logger_booking.info("Booking reminder start time- "+ str(datetime.strftime(datetime.now(),'%y-%m-%d  %H:%M')))
get_Bookings_for_day()
message = "Sent %s reminder SMS"%(str(buks))
generic_utils.sendEmail('vbnetmithun@gmail.com', 'Booking reminder script run successful',message)
logger_booking.info("Booking reminder end  time- "+ str(datetime.strftime(datetime.now(),'%y-%m-%d  %H:%M')))






