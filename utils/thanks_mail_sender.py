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
from django.conf import settings

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
buks = None
def send_thanks_mail():
    #import pdb;pdb.set_trace();
    try:
        yesterday = datetime.today().date()-timedelta(days = 1)
        status_code = responses.BOOKING_CODES['BOOKED']
        bookings = BookingDetails.objects.filter(appointment_date = yesterday,   \
        booking_status = 'BOOKED', status_code = status_code, is_valid = True)
        ##log code starting
        status_code = responses.BOOKING_CODES['USED']
        for every_book in bookings:
            try:
                #code = every_book.booking_code
                #studio_name = StudioProfile.objects.values('name').get(id = every_book.studio.id)
                #user = User.objects.values('first_name','email','id').get(id = every_book.user.id)
                date = yesterday
                #get email template and render all variables
                review_link = None
                review_key = ReviewLink.objects.values('link_code').filter(booking_id = every_book.id, is_reviewed = 0)
                if review_key:
                    review_link = settings.HOST_NAME+'/booking/review_from_email/?review_key='+str(review_key[0]['link_code'])+  \
                    '&&booking_id='+str(every_book.id)
                user_details = {'first_name':every_book.user.first_name,'studio_name':every_book.studio.name,  \
                'date':every_book.appointment_date,'review_link':review_link}
                logger_booking.info("Thanks mail user details - "+str(user_details))
                message = get_template('emails/thanks_email.html').render(Context(user_details))
                to_user = every_book.user.email
                subject = responses.MAIL_SUBJECTS['THANKS_EMAIL']%(every_book.studio.name)
                has_sent = ThanksMail.objects.filter(booking_id = every_book.id, status = True)
                if not has_sent:
                    status = generic_utils.sendEmail(to_user, subject, message)
                    updated = BookingDetails.objects.filter(id = every_book.id).update(is_valid = False, \
                        booking_status = 'USED', status_code = status_code,  \
                        service_updated = "thanks mail")
                    if updated:
                        thanks_mail = ThanksMail(booking_id = every_book.id, email = to_user,
                        status = status,user_id = every_book.user.id, service_updated = "thanks mail",  \
                        )
                        thanks_mail.save()
            except Exception,smserr:
                logger_error.error(traceback.format_exc())
                status = False
                thanks_mail = ThanksMail(booking_id = every_book.id, email = to_user, \
                status = status,user_id = every_book.user.id ,service_updated = "thanks mail",  \
                )
                thanks_mail.save()
    except Exception,errorz:
        logger_error.error(traceback.format_exc())
    else:
        buks = len(bookings)
        logger_booking.info("Total thanks mail sent - "+str(buks))
        message = "Sent %s mails"%(str(buks))
        status = generic_utils.sendEmail('asha.ruku93@gmail.com', 'Thanks mail run successful',message)

        ###log code end stats


        
logger_booking.info("Thanks mail start time- "+ str(datetime.strftime(datetime.now(),'%y-%m-%d  %H:%M')))
send_thanks_mail()
logger_booking.info("Thanks mail end  time- "+ str(datetime.strftime(datetime.now(),'%y-%m-%d  %H:%M')))


"""
try:
    BookingDetails.objects.filter(appointment_date = yesterday, booking_status = 'BOOKED',   \
    status_code = 'B001', is_valid = True).update(booking_status = 'EXPIRED',   \
    status_code = status_code, is_valid = False)
except:
    logger_error.error(traceback.format_exc())
"""