##script which send reports to all merchants about the booking
##they had previous day.The script should run every day 6AM


from datetime import datetime
import django
from booking.models import BookingDetails,BookingServices
from studios.models import StudioProfile
from utils import Responses
from django.contrib.auth.models import User
from django.db import transaction

------------------------------------------------------------------------------------------------------
Name | Booking id | Services Booked | Offer code | Booking amount | Actual amount | To pay 
------------------------------------------------------------------------------------------------------

------------------------------------------------------------------------------------------------------
Total Bookings -  Total Booking amount  - Total Amount after offer - Total to pay 
------------------------------------------------------------------------------------------------------

def daily_merchant_report():
	try:
		##get all used booking for the day
        today = datetime.today().date()
        bookings = BookingDetails.objects.filter(appointment_date = today,  \
            booking_status = 'USED', status_code = '', is_valid = True)
        studios_visited = []
        to_print = {}
        for stud in booking:
            #if stud not in studios_visited:
            try:
                services_booked = BookingServices.objects.filter(booking_id = stud['id'])
                services = []
                for sun in services_booked:
                    services.append(sun['service'].service_name)
                obx = {}
                obx['studio_id'] =  stud['studio_id']
                obx['data'] = []
                obj = {}
                obj['studio_name'] = stud['studio'].name 
                obj['booking_id'] = stud['id']
                obj['services_booked'] = services[:]
                obj['offer_code'] = stud['promo'].promo_code
                obj['booking_amount'] = stud['purchase'].purchase_amount
                obj['actual_amount'] = stud['purchase'].actual_amount
                obj['amount_to_pay'] = (obj['booking_amount'] - (obj['booking_amount']/10))
                obx['data'].append(obj)
                if stud not in studios_visited:
                    studios_visited.append(stud['id'])
                    to_print[stud['studio_id']] = obx
                else:
                    to_print[stud['studio_id']]['data'].append(obj)
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
        return to_print

def render_to_pdf(template,data):
    ##generate pdf with data
    ##save pdf to table
    ##location should be inside studio

def generate_pdf():
    to_generate = daily_merchant_report()
    for data in to_generate:
        pdf_file = render_to_pdf('merchant_report.html',{'pagesize':'A4','data':data})
     



def send_pdf_as_mail():

    """function to send all the record for tha data which are not send"""
    ##for the day get all the pdfs
    ##send one by one
    ##update table
