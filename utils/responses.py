#all login responses to ng

##different responses
##BOOKING PAYMENT CANCEL REFUND 
BOOKING_RESPONSES = {"BOOKING_SUCCESS":{"MSG":"Booked successfully.","CODE":'B001'}, \
                    "BOOKING_FAIL":{"MSG":"Booking failed.","CODE":'B002'}, \
                    "BOOKING_CANCELLED_SUCCESS":{"MSG":"Cancelled successfully.","CODE":'B003'}, \
                    "BOOKING_CANCELLED_FAIL":{"MSG":"Could not cancel booking.Contact support","CODE":'B003F'}, \
                    "BOOKING_USED":{"MSG":"Service used.","CODE":'B004'}, \
                    "BOOKING_UN_USED":{"MSG":"Service used.","CODE":'B005'}, \
				   }

BOOKING_CODES = {'BOOKED':'B001','FAILED':'B002','CANCEL':'B003','USED':'B004','UNUSED':'B005'}
PAYMENT_CODES = {'PAID':'P001','PAY_FAILED':'P002','PAY_CANCELLED':'P003',  \
                 'REFUND_REQUESTED':'P004','REFUND_SUCCESS':'P005'}

SMS_TEMPLATES = {'DLY_REM':"Hi %s,This is a reminder for your booking for %s on %s at %s ",
                'HLY_REM':"Hi %s,This is a reminder for your booking for %s on %s at %s "}

MAIL_SUBJECTS = {'THANKS_EMAIL':"Thank you for using gopanther.com"}