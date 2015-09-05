from django.contrib import admin

# Register your models here.
from models import *


class StudioTypeAdmin(admin.ModelAdmin):
	list_display = ['type_desc']

class StudioKindAdmin(admin.ModelAdmin):
	list_display = ['kind_desc']
	
class AmenitiesAdmin(admin.ModelAdmin):
	list_display = ['amenity_name']

class StudioGroupAdmin(admin.ModelAdmin):
	list_display = ['group_name']

class ServiceAdmin(admin.ModelAdmin):
	list_display = ['service_name']

class StudioProfileAdmin(admin.ModelAdmin):
	list_display = ['name','area']
	
class ServiceTypeAdmin(admin.ModelAdmin):
	list_display = ['service_name']

class CloseDatesAdmin(admin.ModelAdmin):
	list_display = ['closed_on_day']

class StudioServicesAdmin(admin.ModelAdmin):
	list_display = ['studio_profile','service']

class StudioServicesTypesAdmin(admin.ModelAdmin):
	list_display = ['studio_profile','service_type']


admin.site.register(StudioServiceTypes, StudioServicesTypesAdmin)
admin.site.register(StudioKind,StudioKindAdmin)
admin.site.register(Studio)
admin.site.register(StudioServices,StudioServicesAdmin)
admin.site.register(StudioProfile,StudioProfileAdmin)
admin.site.register(Service,ServiceAdmin)
admin.site.register(ServiceType,ServiceTypeAdmin)
admin.site.register(StudioGroup,StudioGroupAdmin)
admin.site.register(StudioType, StudioTypeAdmin)
admin.site.register(StudioAmenities)
admin.site.register(Amenities,AmenitiesAdmin)
admin.site.register(StudioPicture)
admin.site.register(StudioClosedDetails)
admin.site.register(CloseDates,CloseDatesAdmin)
admin.site.register(StudioAddRequest)


#admin.site.register(ThatModel)

