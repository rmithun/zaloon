#all login responses to ng
BOOKING_RESPONSES = {"BOOKING_SUCCESS":{"MSG":"Booked successfully.","CODE":'SBUK01'}, \
                    "BOOKING_FAIL":{"MSG":"Booking failed.","CODE":'FBUK02'}, \
                    "BOOKING_CANCELLED_SUCCESS":{"MSG":"Cancelled successfully.","CODE":'CSBUK03'}, \
                    "BOOKING_CANCELLED_FAIL":{"MSG":"Could not cancel booking.Contact support","CODE":'CFBUK04'}, \
                    "BOOKING_USED":{"MSG":"Service used.","CODE":'SBUKUSD05'}, \
                    "BOOKING_UN_USED":{"MSG":"Service used.","CODE":'SBUKUNUSD06'}, \
				   }

BOOKING_CODES = {'BOOKED':'B001','FAILED':'B002','CANCEL':'B003','USED':'B004','UNUSED':'B005'}
PAYMENT_CODES = {'PAID':'P001','PAY_FAILED':'P002','PAY_CANCELLED':'P003',  \
                 'REFUND_REQUESTED':'P004','REFUND_SUCCESS':'P005'}