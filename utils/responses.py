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

BOOKING_CODES = {'BOOKED':'B001','FAILED':'B002','CANCEL':'B003','USED':'B004','UNUSED':'B005',  \
                 'BOOKING':'B006','EXPIRED':'B007'}
PAYMENT_CODES = {'PAID':'P001','PAY_FAILED':'P002','PAY_CANCELLED':'P003',  \
                 'REFUND_REQUESTED':'P004','REFUND_SUCCESS':'P005'}

SMS_TEMPLATES = {'DLY_REM':"Hi %s,This is a reminder for your booking for %s on %s at %s ",
                'HLY_REM':"Hi %s,This is a reminder for your booking for %s on %s at %s ",
                'BOOKING_EMAIL':"Hi %s,your booking at %s on %s at %s is successfull"}

MAIL_SUBJECTS = {'THANKS_EMAIL':"Thank you for using gopanther",
                 'BOOKING_EMAIL':"Booking code from gopanther",
                 'CANCEL_EMAIL':"Cancelled booking details",
                 'DAILY_REPORT_EMAIL':"Daily booking report from gopanther"}



HOURS_DICT = {0:[00,15,30,45],1:[00,15,30,45],2:[00,15,30,45],3:[00,15,30,45],  \
              4:[00,15,30,45],5:[00,15,30,45],6:[00,15,30,45],7:[00,15,30,45],  \
              8:[00,15,30,45],9:[00,15,30,45],10:[00,15,30,45],11:[00,15,30,45], \
              12:[00,15,30,45], 13:[00,15,30,45],14:[00,15,30,45],15:[00,15,30,45], \
              16:[00,15,30,45],17:[00,15,30,45],18:[00,15,30,45],19:[00,15,30,45],  \
              20:[00,15,30,45],21:[00,15,30,45],22:[00,15,30,45],23:[00,15,30,45]}