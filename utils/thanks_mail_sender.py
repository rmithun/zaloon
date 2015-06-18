##script which sends tahnks and feedback mail all the bookings used
##for the day. 
##this script should run at differnt time in different day , so that
##we will analyze when the user interaction is more
##for now run it at 7.AM



from datetime import datetime
import django
from booking.models import BookingDetails
from studios.models import StudioProfile
from utils import responses, generic_utils
from django.contrib.auth.models import User


##get all used bookings for the day
##get the code,date, time, studio, services
#get mobile number from BookedMessageSend
##get SMS template 
##send SMS
##Make an entry in thanks_reminder table with status	


##need to integrate with thread que system when the count overflows in future
def send_thanks_mail():
	try:
	    today = datetime.today().date()
        bookings = BookingDetails.objects.filter(appointment_date = today,   \
            booking_status = 'USED', booking_code = 'B004', is_valid = True)
            ##log code starting
        for every_book in bookings:
        	code = every_book['booking_code']
        	studio_name = StudioProfile.objects.filter(id = every_book['studio']).values('name')
        	user = User.objects.filter(id = every_book['user']).values('first_name','email','id')
        	date = today
            time = datetime.strptime(str(every_book['appointment_time']), "%H.%M").strftime("%I:%M %p")
        	#mobile_no = BookedMessageSend.objects.filter(booking_id = every_book['id']).values('mobile_no')
            ##get sms template
        	#get email template and render all variables
            name = user['first_name']
            email_template = ""
            to_user = user['email']
        	try:
        	    generic_utils.sendMail(to_user,bcc_user,email_template)
        	    status = True
        	except Exception,smserr:
        		print repr(smserr)
        		status = False
        		thanks_mail = ThanksMail(booking_id = every_book['id'], mobile_no = mobile_no,  \
        	    	status = status,,user_id = user['id'] ,service_updated = "daily reminder",  \
        	    	)
                thanks_mail.save()
        	else:
        		thanks_mail = ThanksMail(booking_id = every_book['id'], mobile_no = mobile_no,  \
        	    	status = status,user_id = user['id'], service_updated = "daily reminder",  \
        	    	)
                thanks_mail.save()
        ###log code end stats
    except Exception,error:
        print error
    else:
        print len(bookings)
    ###log code end stats


get_Bookings_for_day()



