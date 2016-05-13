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

#application imports
from booking.models import BookingDetails,BookingServices,MerchantDailyReportStatus
from studios.models import StudioProfile, Studio
from utils import responses, generic_utils


""""------------------------------------------------------------------------------------------------------
Name | Booking id | Services Booked | Offer code | Booking amount | Actual amount | To pay 
------------------------------------------------------------------------------------------------------

------------------------------------------------------------------------------------------------------
Total Bookings -  Total Booking amount  - Total Amount after offer - Total to pay 
------------------------------------------------------------------------------------------------------
"""


def daily_merchant_report():
    try:
        ##get all used booking for the day
        today = datetime.today().date()
        bookings = BookingDetails.objects.filter(appointment_date = today,  \
            booking_status = 'USED', status_code = 'B004', is_valid = False)
        studios_visited = []
        to_print = {}
        for stud in bookings:
            #if stud not in studios_visited:
            try:
                services_booked = BookingServices.objects.filter(booking_id = stud.id)
                transaction_charge = StudioAccountDetails.objects.values('transaction_percent').get( \
                    studio_id = stud.studio_id)
                transaction_percent = int(transaction_charge['transaction_percent'])
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
                obj['offer_code'] = stud.promo.promo_code
                obj['booking_amount'] = stud.purchase.purchase_amount
                obj['actual_amount'] = stud.purchase.actual_amount
                obj['amount_to_pay'] = (obj['booking_amount'] - (obj['booking_amount']/transaction_percent  ))
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


def render_to_pdf(template_url,data,studio):
    ##generate pdf with data
    #import pdb;pdb.set_trace();
    try:
        template = get_template(template_url)
        context = Context(data)
        html =  template.render(context)
        filename = data['todayslist']['data'][0]['studio_name'] + str(datetime.today().date())
        result = open(filename+'.pdf', 'wb')
        #result = StringIO.StringIO()
        pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("ISO-8859-1")), result)
        if not pdf.err:
            ###get and save the pdf 
            result = open(filename+'.pdf', 'r')
            pdf = File(result)
            rep = MerchantDailyReportStatus(studio_id = studio, report = pdf)
            rep.save()
            studio_dt = StudioProfile.objects.values('studio').get(id = studio)
            studio_email = Studio.objects.values('email').get(id = studio_dt['studio'])
            try:
                #send email
                subject = (responses.MAIL_SUBJECTS['DAILY_REPORT_EMAIL'])%(today)
                generic_utils.sendEmail(studio_email['email'],subject,message)
            except Exception,e:
                print repr(e)
            ##save pdf to table
            ##location should be inside studio
    except Exception,pdfrenderr:
        print (pdfrenderr)

def generate_pdf():
    to_generate = daily_merchant_report()
    for key,data in to_generate.iteritems():
        try:
            pdf_file = render_to_pdf('../templates/reports/merchant_daily_report.html',  \
               {'pagesize':'A4','todayslist':data},key)
        except Exception,pdfgenrateerr:
            print (pdfgenrateerr)
     




def send_pdf_as_mail():

    """function to send all the record for tha data which are not send"""
    ##for the day get all the pdfs
    ##send one by one
    ##update table
    print "hto"


generate_pdf()




