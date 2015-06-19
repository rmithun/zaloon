from django.contrib import admin

# Register your models here.
from models import *

admin.site.register(StudioKind)
admin.site.register(Studio)
admin.site.register(StudioServices)
admin.site.register(StudioProfile)
admin.site.register(Service)
admin.site.register(ServiceType)
admin.site.register(StudioGroup)
admin.site.register(StudioType)
admin.site.register(StudioAmenities)
admin.site.register(Amenities)
admin.site.register(StudioPicture)
admin.site.register(StudioClosedDetails)
admin.site.register(CloseDates)


#admin.site.register(ThatModel)