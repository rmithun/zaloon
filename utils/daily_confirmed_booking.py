##script which send reports to all merchants about the booking
##they had previous day.The script should run every day 6AM


#standard library imports
from datetime import datetime

#third party imports
import django
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


""""
------------------------------------------------------------------------------------------------------
Name | Booking id | Services Booked | Booking Date | Booking Time 
------------------------------------------------------------------------------------------------------
"""

today = datetime.today().date()

def daily_confirmed_booking():
    try:
        ##get all used booking for the day
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
                obj['booking_id'] = stud.id
                obj['services_booked'] = services[:]
                obj['appointment_date   '] = today
                obj['appointment_time'] = stud.appointment_start_time
                obx['data'].append(obj)
                if stud.studio_id not in studios_visited:
                    studios_visited.append(stud.studio_id)
                    to_print[stud.studio_id] = obx
                else:
                    to_print[stud.studio_id]['data'].append(obj)
            except Exception,jsonerr:
                print repr(jsonerr)
                #dm_status = DailyMerchantReportStatus(booking_id = stud['id'],  \
                #    studio_id = stud['studio_id'], status = 'Fail')
                #dm_status.save()
            else:   
                #dm_status = DailyMerchantReportStatus(booking_id = stud['id'],  \
                #    studio_id = stud['studio_id'], status = 'Fail')
                #dm_status.save()
                pass
    except Exception,majErr:
        print repr(majErr)
    else:
        print to_print
        return to_print

@transaction.commit_manually
def render_to_pdf(template_url,data,studio):
    ##generate pdf with data
    try:
        import pdb;pdb.set_trace();
        template = get_template(template_url)
        context = Context(data)
        html =  template.render(context)
        filename = data['todayslist']['data'][0]['studio_name'] + str(datetime.today().date())+"__bookings"
        result = open(filename+'.pdf', 'wb')
        #result = StringIO.StringIO()
        pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("ISO-8859-1")), result)
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
                generic_utils.sendEmail(studio_email['email'],subject,message)
                rep = DailyBookingConfirmation.filter(studio_id = studio, report_date = \
                 today).update(mail_sent = 1, updated_date_time = datetime.now())
            except Exception,e:
                print repr(e)
            ##save pdf to table
            ##location should be inside studio
            result.close();
    except Exception,pdfrenderr:
        transaction.rollback()
        print (pdfrenderr)
    else:
        transaction.commit()

def generate_pdf():
    to_generate = daily_confirmed_booking()
    for key,data in to_generate.iteritems():
        try:
            pdf_file = render_to_pdf('../templates/emails/daily_confirmed_bookings.html',  \
               {'pagesize':'A4','todayslist':data},key)
        except Exception,pdfgenrateerr:
            print (pdfgenrateerr)
     

generate_pdf()





