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
	    yesterday = datetime.today().date()-timedelta(days =1)
        bookings = BookingDetails.objects.filter(appointment_date = yesterday,   \
            booking_status = 'USED', booking_code = 'B004', is_valid = True)
        ##log code starting
        for every_book in bookings:
        	code = every_book['booking_code']
        	studio_name = StudioProfile.objects.filter(id = every_book['studio']).values('name')
        	user = User.objects.filter(id = every_book['user']).values('first_name','email','id')
        	date = yesterday
            time = datetime.strptime(str(every_book['appointment_time']), "%H.%M").strftime("%I:%M %p")
        	#get email template and render all variables
            user_details = {'user_name':user['first_name'],'studio_name':studio_name['name'],  \
            'date':yesterday}
            message = get_template('emails/thanks_mail.html').render(Context(user_details))
            to_user = user['email']
            subject = responses.MAIL_SUBJECTS['THANKS_EMAIL']
        	try:
        	    status = generic_utils.sendEmail(form_data['email'], subject, message)
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



