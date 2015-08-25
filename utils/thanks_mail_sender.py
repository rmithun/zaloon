##script which sends tahnks and feedback mail all the bookings used
##for the day. 
##this script should run at differnt time in different day , so that
##we will analyze when the user interaction is more
##for now run it at 8.PM daily


import os,sys
import django
sys.path.append(os.path.join(os.path.dirname(__file__), 'onepass'))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..')))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "onepass.settings")
django.setup()

from datetime import datetime, timedelta
from user_accounts import models
from booking.models import BookingDetails, ThanksMail, ReviewLink
from studios.models import StudioProfile
from utils import responses, generic_utils
from django.contrib.auth.models import User
from django.template.loader import get_template
from django.template import Context
import logging
import traceback



logger_booking = logging.getLogger('log.daily_scripts')
logger_error = logging.getLogger('log.errors')


##get all used bookings for the day
##get the code,date, time, studio, services
#get mobile number from BookedMessageSend
##get SMS template 
##send SMS
##Make an entry in thanks_reminder table with status	
##need to integrate with thread que system when the count overflows in future
def send_thanks_mail():
    try:
        yesterday = datetime.today().date()-timedelta(days = 1)
        status_code = responses.BOOKING_CODES['USED']
        bookings = BookingDetails.objects.filter(appointment_date = yesterday,   \
        booking_status = 'USED', status_code = status_code, is_valid = False)
        ##log code starting
        status_code = responses.BOOKING_CODES['EXPIRED']
        for every_book in bookings:
            #code = every_book.booking_code
            studio_name = StudioProfile.objects.values('name').get(id = every_book.studio.id)
            user = User.objects.values('first_name','email','id').get(id = every_book.user.id)
            date = yesterday
            #get email template and render all variables
            review_link = None
            review_key = ReviewLink.objects.get('link_code').filter(booking_id = every_book.id, is_reviewed = 0)
            if review_key:
                review_link = settings.HOST_NAME+'/booking/review_from_email/?review_key='+str(review_key['link_code'])+  \
                '&&booking_id='+str(every_book.id)
            user_details = {'first_name':user['first_name'],'studio_name':studio_name['name'],  \
            'date':yesterday,'review_link':review_link}
            logger_booking.info("Thanks mail user details - "+str(user_details))
            message = get_template('emails/thanks_email.html').render(Context(user_details))
            to_user = user['email']
            subject = responses.MAIL_SUBJECTS['THANKS_EMAIL']
            try:
                has_sent = ThanksMail.objects.filter(booking_id = every_book.id)
                if not has_sent:
                    status = generic_utils.sendEmail(to_user, subject, message)
                    BookingDetails.objects.filter(id = every_book.id).update(is_valid = False, \
                        booking_status = 'EXPIRED', status_code = status_code)
            except Exception,smserr:
                logger_error.error(traceback.format_exc())
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
    except Exception,errorz:
        logger_error.error(traceback.format_exc())
        print errorz
    else:
        logger_booking.info("Total thanks mail sent - "+str(len(bookings)))
        ###log code end stats


        
logger_booking.info("Thanks mail start time- "+ str(datetime.strftime(datetime.now(),'%y-%m-%d  %H:%M')))
send_thanks_mail()
logger_booking.info("Thanks mail end  time- "+ str(datetime.strftime(datetime.now(),'%y-%m-%d  %H:%M')))

try:
    BookingDetails.objects.filter(appointment_date = yesterday, booking_status = 'BOOKED',   \
    status_code = 'B001', is_valid = True).update(booking_status = 'EXPIRED',   \
    status_code = status_code, is_valid = False)
except:
    logger_error.error(traceback.format_exc())
