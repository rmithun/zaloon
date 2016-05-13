#all login responses to ng

##different responses
##BOOKING PAYMENT CANCEL REFUND 
BOOKING_RESPONSES = {"BOOKING_SUCCESS":{"MSG":"Booked successfully.","CODE":'B001'}, \
                    "BOOKING_FAIL":{"MSG":"Booking failed.","CODE":'B002'}, \
                    "BOOKING_CANCELLED_SUCCESS":{"MSG":"Cancelled successfully.","CODE":'B003'}, \
                    "BOOKING_CANCELLED_FAIL":{"MSG":"Could not cancel booking.Contact support","CODE":'B003F'}, \
                    "BOOKING_USED":{"MSG":"Service used.","CODE":'B004'}, \
                    "BOOKING_UN_USED":{"MSG":"Service used.","CODE":'B005',}, \
                    "DATE_EXPIRED":{"MSG":"The selected date is crossed","CODE":'B006'},  \
                    "TIME_EXPIRED":{"MSG":"The selected time is not available now","CODE":'B007'}
           }

BOOKING_CODES = {'BOOKED':'B001','FAILED':'B002','CANCELLED':'B003','USED':'B004','UNUSED':'B005',  \
                 'BOOKING':'B006','EXPIRED':'B007'}
PAYMENT_CODES = {'PAID':'P001','PAY_FAILED':'P002','PAY_CANCELLED':'P003',  \
                 'REFUND_REQUESTED':'P004','REFUND_SUCCESS':'P005'}

SMS_TEMPLATES = {'DLY_REM':"Hi %s,This is a reminder for your booking in zaloon.in for %s, %s on %s at %s. Booking code - %s",
                'HLY_REM':"Hi %s,This is a reminder for your booking for %s on %s at %s ",
                'BOOKING_SMS':"Hi %s,Your appointment with %s on %s at %s has been confirmed.Your booking code is %s.",
                'STUDIO_SMS':"Hey! You have a new booking from %s (%s) on %s at %s.Booking code - %s"}

MAIL_SUBJECTS = {'THANKS_EMAIL':"How was %s?",
                 'BOOKING_EMAIL':"Booking code from Zaloon.in",
                 'CANCEL_EMAIL':"Cancelled booking details",
                 'DAILY_REPORT_EMAIL':"Daily booking report from zaloon for %s",
                 'STUDIO_REQ_REGISTER':"We will contact you shortly.",
                 'DAILY_BOOKING_MAIL':"Confirmed Booking details for %s.",
                 'STUDIO_BOOKING_EMAIL':"Hey! You have a new Booking from %s",
                 'STUDIO_CANCEL_EMAIL':"Booking cancellation for %s",
                 'DAILY_INVOICE_MAIL':"Invoice details for %s."}



HOURS_DICT = {0:[00,15,30,45],1:[00,15,30,45],2:[00,15,30,45],3:[00,15,30,45],  \
              4:[00,15,30,45],5:[00,15,30,45],6:[00,15,30,45],7:[00,15,30,45],  \
              8:[00,15,30,45],9:[00,15,30,45],10:[00,15,30,45],11:[00,15,30,45], \
              12:[00,15,30,45], 13:[00,15,30,45],14:[00,15,30,45],15:[00,15,30,45], \
              16:[00,15,30,45],17:[00,15,30,45],18:[00,15,30,45],19:[00,15,30,45],  \
              20:[00,15,30,45],21:[00,15,30,45],22:[00,15,30,45],23:[00,15,30,45]}


COUPON_RESPONSE = {'NO_COUPON':'Sorry, Coupon expired.', \
                   'INVALID_COUPON':'The coupon code is invalid', \
                   'NOT_APPLICABLE':'Sorry, Coupon code not applicable.',\
                   'COUPON_USED':'Sorry, Coupon code not applicable.This Coupon code was already used.',
                   'COUPON_EXPIRED_USED':'Sorry, Coupon code not applicable.This Coupon code was already used/expired.',
                   'COUPON_MIN_AMOUNT':'The minimum booking amount should be %s to apply this coupon'}


SERVICE_TAX = 14