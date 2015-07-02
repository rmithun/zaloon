##script which send reminder notification for all the booked users
##for the day. This differes from every hour notification script
##this runs every day at 7 AM

from datetime import datetime
from booking.models import BookingDetails,BookedMessageSent,DailyReminder
from studios.models import StudioProfile
from utils import responses, generic_utils
from django.contrib.auth.models import User


#application imports
##get all active bookings for the day
##get the code,date, time, studio, services
#get mobile number from BookedMessageSend
##get SMS template 
##send SMS
##Make an entry in daily_reminder table with status	


today = datetime.today().date()
##need to integrate with thread queue system when the count overflows indatetime.date(2015, 7, 1) future
def get_Bookings_for_day():
    try:
        import pdb;pdb.set_trace();
        bookings = BookingDetails.objects.filter(appointment_date = today,   \
            booking_status = 'BOOKED', status_code = 'B001', is_valid = True)
        ##log code starting
        for every_book in bookings:
            has_sent  = DailyReminder.objects.filter(booking_id = every_book.id, status = True)
            if len(has_sent) is 0:
        	    code = every_book.booking_code
        	    studio_name = StudioProfile.objects.values('name','area').get(id = every_book.studio.id)
        	    user_name = User.objects.values('first_name','id').get(id = every_book.user.id)
        	    date = today
                    time = datetime.strptime(str(every_book.appointment_start_time), "%H:%M:%S").strftime("%I:%M %p")
        	    mobile_no = BookedMessageSent.objects.filter(booking_id = every_book.id).values('mobile_no')
                    ##get sms template
                    mobile_no = '9677267542'
        	    sms_template = (responses.SMS_TEMPLATES['DLY_REM'])%(user_name['first_name'], studio_name['name'],   \
                    studio_name['area'], date, time,code)
        	    try:
        	        status = generic_utils.sendSMS(mobile_no,sms_template)
                        print "mi"
        	    except Exception,smserr:
        		    print repr(smserr)
        		    status = False
        	            daily_reminder = DailyReminder(booking_id = every_book.id, mobile_no = mobile_no,  \
        	            status = status,user_id = user_name['id'],service_updated = "daily reminder", message = sms_template,  \
        	    	    )
                            daily_reminder.save()
        	    else:
        	        daily_reminder = DailyReminder(booking_id = every_book.id, mobile_no = mobile_no,  \
        	    	status = status,user_id = user_name['id'], service_updated = "daily reminder", message = sms_template,  \
        	    	)
                        daily_reminder.save()
            ###log code end stats
    except Exception,error:
        print error
    else:
        print len(bookings)
    ###log code end stats


get_Bookings_for_day()



