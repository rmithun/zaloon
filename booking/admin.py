from django.contrib import admin
from models import * 
# Register your models here.
class BookingDetailsAdmin(admin.ModelAdmin):
	list_display = ['booking_code']


class CouponAdmin(admin.ModelAdmin):
	list_display = ['coupon_code']


class CouponForStudiosAdmin(admin.ModelAdmin):
	list_display = ['coupon']

admin.site.register(BookingDetails,BookingDetailsAdmin)
admin.site.register(Purchase)
admin.site.register(BookingServices)
admin.site.register(StudioReviews)
admin.site.register(Coupon,CouponAdmin)
admin.site.register(CouponForStudios,CouponForStudiosAdmin)
admin.site.register(MerchantDailyReportStatus)
admin.site.register(ThanksMail)
admin.site.register(DailyBookingConfirmation)
admin.site.register(BookedMessageSent)
admin.site.register(DailyReminder)
