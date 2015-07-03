from django.contrib import admin
from models import * 
# Register your models here.
admin.site.register(BookingDetails)
admin.site.register(Purchase)
admin.site.register(BookingServices)
admin.site.register(StudioReviews)
admin.site.register(Coupon)
admin.site.register(CouponForStudios)
admin.site.register(MerchantDailyReportStatus)
admin.site.register(ThanksMail)
admin.site.register(DailyBookingConfirmation)
admin.site.register(BookedMessageSent)
admin.site.register(DailyReminder)
