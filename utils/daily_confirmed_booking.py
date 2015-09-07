##script which send reports to all merchants about the booking
##they had previous day.The script should run every day 6AM


#standard library imports
from datetime import datetime
import logging
import traceback

#third party imports
import os,sys
import django
sys.path.append(os.path.join(os.path.dirname(__file__), 'onepass'))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..')))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "onepass.settings")
django.setup()


from django.contrib.auth.models import User
from django.db import transaction
import cStringIO as StringIO
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from cgi import escape
from django.core.files import File
from django.db import transaction

#application imports
from booking.models import BookingDetails,BookingServices,MerchantDailyReportStatus, DailyBookingConfirmation
from studios.models import StudioProfile, Studio
from utils import responses, generic_utils


logger_booking = logging.getLogger('log.daily_scripts')
logger_error = logging.getLogger('log.errors')


""""
--------------------------------------------------------------------------------------------------------------
Name | Mobile | Booking id | Services Booked | From Time | To Time | Booking Code | Booking Amount | Mark Used  
--------------------------------------------------------------------------------------------------------------
"""

today = datetime.today().date()
buks = None
def daily_confirmed_booking():
    try:
        ##get all used booking for the day
        #import pdb;pdb.set_trace();
        time = datetime.now().replace(hour = 13, minute = 00)
        if datetime.now().hour < 13:
            bookings = BookingDetails.objects.filter(appointment_date = today,  \
            booking_status = 'BOOKED', status_code = 'B001', is_valid = True,  \
            appointment_start_time__lt = time)
        else:
            bookings = BookingDetails.objects.filter(appointment_date = today,  \
            booking_status = 'BOOKED', status_code = 'B001', is_valid = True,  \
            appointment_start_time__gte = time)
        studios_visited = []
        to_print = {}
        for stud in bookings:
            #if stud not in studios_visited:
            try:
                services_booked = BookingServices.objects.filter(booking_id = stud.id)
                services = []
                for sun in services_booked:
                    services.append(sun.service.service_name)
                obx = {}
                obx['studio_id'] =  stud.studio_id
                obx['data'] = []
                obj = {}
                obj['studio_name'] = stud.studio.name
                obj['studio_address1'] = stud.studio.address_1
                obj['studio_address2'] = stud.studio.address_2
                obj['studio_area'] = stud.studio.area
                obj['studio_city'] = stud.studio.city
                obj['booking_id'] = stud.id
                obj['services_booked'] = services[:]
                obj['appointment_date'] = today
                obj['appointment_start_time'] = stud.appointment_start_time
                obj['appointment_end_time'] = stud.appointment_end_time
                obj['booking_code'] = stud.booking_code
                obj['booking_amount'] = stud.purchase.purchase_amount
                obj['mobile_no'] = stud.mobile_no
                obx['data'].append(obj)
                if stud.studio_id not in studios_visited:
                    studios_visited.append(stud.studio_id)
                    to_print[stud.studio_id] = obx
                else:
                    to_print[stud.studio_id]['data'].append(obj)
            except Exception,jsonerr:
                logger_error.error(traceback.format_exec())
                dm_status = DailyMerchantReportStatus(booking_id = stud['id'],  \
                    studio_id = stud['studio_id'], status = 'Fail')
                dm_status.save()
            else:   
                dm_status = DailyMerchantReportStatus(booking_id = stud['id'],  \
                    studio_id = stud['studio_id'], status = 'Fail')
                dm_status.save()
    except Exception,majErr:
        logger_error.error(traceback.format_exec())
    else:
        logger_booking.info(" data to render  "+str(to_print))
        return to_print

@transaction.commit_manually
def render_to_pdf(template_url,data,studio):
    ##generate pdf with data
    try:
        template = get_template(template_url)
        context = Context(data)
        html =  template.render(context)
        filename = data['todayslist']['data'][0]['studio_name'] + str(datetime.today().date())+"__bookings"
        result = open(filename+'.pdf', 'wb')
        #result = StringIO.StringIO()
        logger_booking.info("File name "+str(filename))
        logger_booking.info("File name "+str(data))
        try:
            pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("ISO-8859-1")), result)
        except:
            pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-8")), result, encoding="UTF-8")
        if not pdf.err:
            ###get and save the pdf 
            result = open(filename+'.pdf', 'r')
            pdf = File(result)
            rep = DailyBookingConfirmation(studio_id = studio, booking_pdf = pdf,  \
                service_updated = "daily confirm booking sender")
            rep.save()
            studio_dt = StudioProfile.objects.values('studio').get(id = studio)
            studio_email = Studio.objects.values('email').get(id = studio_dt['studio'])
            try:
                #send email
                subject = (responses.MAIL_SUBJECTS['DAILY_BOOKING_MAIL'])%(today)
                generic_utils.sendEmail('vbnetmithun@gmail.com',subject,message)
                ##generic_utils.sendEmail(studio_email['email'],subject,message)
                rep = DailyBookingConfirmation.filter(studio_id = studio, report_date = \
                 today).update(mail_sent = 1, updated_date_time = datetime.now())
            except Exception,e:
                logger_error.error(traceback.format_exec())
            ##save pdf to table
            ##location should be inside studio
            result.close();
    except Exception,pdfrenderr:
        transaction.rollback()
        logger_error.error(traceback.format_exec())
        
    else:
        transaction.commit()


def generate_pdf():
    to_generate = daily_confirmed_booking()
    buks = len(to_generate)
    logger_booking.info("Sent mails to %s  studios - "%(str(buks)))
    for key,data in to_generate.iteritems():
        try:
            logger_booking.info("data to be rendered - "+str(key)+"---"+str(data))
            pdf_file = render_to_pdf('../templates/emails/daily_confirmed_bookings.html',  \
               {'pagesize':'A4','todayslist':data},key)
        except Exception,pdfgenrateerr:
            logger_error.error(traceback.format_exec())

     
logger_booking.info("Confirmed booking script starts running  "+datetime.strftime(datetime.now(),  \
            '%y-%m-%d %H:%M'))
generate_pdf()
message = "Sent mails to %s  studios"%(str(buks))
generic_utils.sendEmail('vbnetmithun@gmail.com', 'Daily report script run sucessfull',message)
logger_booking.info("Confirmed booking script stops running  "+datetime.strftime(datetime.now(),  \
            '%y-%m-%d %H:%M'))





