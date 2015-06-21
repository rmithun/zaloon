##script which sends tahnks and feedback mail all the bookings used
##for the day. 
##this script should run at differnt time in different day , so that
##we will analyze when the user interaction is more
##for now run it at 7.AM



from datetime import datetime, timedelta
import django
from user_accounts import models
from booking.models import BookingDetails, ThanksMail
from studios.models import StudioProfile
from utils import responses, generic_utils
from django.contrib.auth.models import User
from django.template.loader import get_template
from django.template import Context


##get all used bookings for the day
##get the code,date, time, studio, services
#get mobile number from BookedMessageSend
##get SMS template 
##send SMS
##Make an entry in thanks_reminder table with status	
##need to integrate with thread que system when the count overflows in future
def send_thanks_mail():
    try:
        import pdb;pdb.set_trace();
        yesterday = datetime.today().date()-timedelta(days = 1)
        status_code = responses.BOOKING_CODES['USED']
        bookings = BookingDetails.objects.filter(appointment_date = yesterday,   \
        booking_status = 'USED', status_code = status_code, is_valid = True)
        ##log code starting
        for every_book in bookings:
            code = every_book.booking_code
            studio_name = StudioProfile.objects.values('name').get(id = every_book.studio.id)
            user = User.objects.values('first_name','email','id').get(id = every_book.user.id)
            date = yesterday
            time = datetime.strptime(str(every_book.appointment_time), "%H:%M:%S").strftime("%I:%M %p")
            #get email template and render all variables
            user_details = {'first_name':user['first_name'],'studio_name':studio_name['name'],  \
            'date':yesterday}
            message = get_template('emails/thanks_email.html').render(Context(user_details))
            to_user = user['email']
            subject = responses.MAIL_SUBJECTS['THANKS_EMAIL']
            try:
                for i in range(10):
                    status = generic_utils.sendEmail(to_user, subject, message)
                status_code = responses.BOOKING_CODES['EXPIRED']
                BookingDetails.objects.filter(id = every_book.id).update(is_valid = False, \
                    booking_status = 'EXPIRED', status_code = status_code)
            except Exception,smserr:
                print repr(smserr)
                status = False
                thanks_mail = ThanksMail(booking_id = every_book.id, email = to_user, \
                status = status,user_id = user['id'] ,service_updated = "daily reminder",  \
                )
                thanks_mail.save()
            else:
                thanks_mail = ThanksMail(booking_id = every_book.id, email = to_user,
                status = status,user_id = user['id'], service_updated = "daily reminder",  \
                )
                thanks_mail.save()
                ###log code end stats
    except Exception,error:
        print error
    else:
        print len(bookings)
        ###log code end stats


        

send_thanks_mail()



