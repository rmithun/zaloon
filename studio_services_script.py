import xlrd
from datetime import datetime
from os import listdir
from os.path import isfile, join
import django,sys,os
sys.path.append(os.path.join(os.path.dirname(__file__), 'onepass'))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..')))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "onepass.settings")
django.setup()

from django.core.files import File
from django.db import transaction
from studios.models import *
import traceback
import re
from PIL import Image, ImageFile
from os.path import getsize
from os import listdir
import io,random





def compressImages(image_file,picname):
  new_file_name = str(random.randint(1000,90000))
  img = Image.open(image_file)
  if image_file:
    format = str(img.format)
    if format != 'PNG' and format != 'JPEG':
        print 'Ignoring file "' + filename + '" with unsupported format ' + format
        return False
    ImageFile.MAXBLOCK = img.size[0] * img.size[1]
    divider = 1
    if img.size[0] > 1000:
      divider = 2
    if img.size[0] > 2000:
      divider = 4
    if img.size[0] > 3000:
      divider = 6
    width = img.size[0]/divider
    height = img.size[0]/divider
    img = img.resize((width, height), Image.ANTIALIAS)
    try:
      os.remove("/home/mithu/Desktop/dataentry/temp/"+picname)
    except OSError:
      pass
    picname = "/home/mithu/Desktop/dataentry/temp/"+new_file_name+picname
    img.save(picname, quality=50,optimize=True)
    return picname
  return False




def get_timesplits(sent_time):
	sent_time = str(sent_time)
	mins = 00
	hr = 5
	if len(sent_time) is 1:
		hr = int(sent_time)
	else:
		if ":" in sent_time:
			hr = int(sent_time.split(":")[0])
			mins = int(sent_time.split(":")[1])
		elif "." in sent_time:
			hr = int(sent_time.split(".")[0])
			mins = int(sent_time.split(".")[1])
		else:
			hr = sent_time[0]
	if hr < 10:
		hr = '0' + str(hr)
	if mins < 10:
		mins = '0' + str(mins)
	time = str(hr) + ":" + str(mins) + ":00"
	from_ti = datetime.strptime(time,'%H:%M:%S').time()
	return from_ti


@transaction.commit_manually
def insert_studio_details(parlour_name):
	try:

		studio_details_book = xlrd.open_workbook('/home/mithu/Desktop/dataentry/'+parlour_name+'/'+parlour_name+'DetailsForm.xls')
		sd_first_sheet = studio_details_book.sheet_by_index(0)
		details = {}
		for i in range(0,sd_first_sheet.nrows):
			#print sd_first_sheet.row_values(i)[0],sd_first_sheet.row_values(i)[1]
			details[sd_first_sheet.row_values(i)[0]] = str(sd_first_sheet.row_values(i)[1])
		if details['has_group'] == 0:
			details['group_name'] = 'No Branches'
		got_group = StudioGroup.objects.filter(group_name__icontains = details['group_name']).values('id','group_name')
		if got_group:
			details['group_name'] = got_group[0]['group_name']
			details['group_id'] = got_group[0]['id']
		else:
			new_group = StudioGroup(group_name = details['group_name'], service_updated = 'new entry from script',  \
				updated_date_time = datetime.now())
			new_group.save()
			details['group_id'] = new_group.id

		if details['studio_type'].lower() in 'salon':
			details['studio_type_id'] = 1
		elif details['studio_type'].lower() in 'beauty':
			details['studio_type_id'] = 3
		else:
			details['studio_type_id'] = 2

		if details['studio_kind'].lower() in 'unisex':
			details['studio_kind_id'] = 3
		elif details['studio_kind'].lower() in 'women':
			details['studio_kind_id'] = 2
		else:
			details['studio_kind_id'] = 1
		###new studio login details
		studio_tbl = Studio.objects.create_user(email = details['email'], password = 'dummy')
		studio_tbl.is_active = True
		studio_tbl.save()

		##trim the spaces
		##change open close time format
		##check bank account number
		##check studio close dates
		details['opening_at'] = get_timesplits(details['opening_at'])
		details['closing_at'] = get_timesplits(details['closing_at'])
		
		if details['bank_account_no'].strip() != details['confirm_account_no'].strip():
			print "account no doesnt match"
			exit(0)
		print details
		##new studio profile
		path = '/home/mithu/Desktop/dataentry/'+parlour_name+'/thumbnail/'
		onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
		thumbnail = open(path+onlyfiles[0])
		newfile_name = compressImages(thumbnail,onlyfiles[0])
		if newfile_name:
			path2 = newfile_name
	        file_ = open(path2)
	        img = File(file_)
	        new_studio_profile = StudioProfile(studio_group_id = details['group_id'], studio_id = studio_tbl.id, studio_type_id = details['studio_type_id'], \
			studio_kind_id = details['studio_kind_id'], name = details['name'].strip(), address_1 = details['address_1'].strip(),  \
			address_2 = details['address_2'].strip(), landmark = details['landmark'].strip(), city = details['city'].strip(),  \
			area = details['area'].strip(), state = details['state'].strip(),search_field_1 =details['search_field_1'].strip(), \
			search_field_2 =details['search_field_2'].strip(),landline_no_1 = details['landline_no_1'].strip(), landline_no_2 = \
			details['landline_no_2'].strip(),in_charge_person = details['in_charge_person'].strip(), incharge_mobile_no =  \
			details['in_charge_mobileno'].strip().split('.')[0],contact_person = details['contact_person'].strip(), contact_mobile_no = \
			details['contact_mobileno'].strip().split('.')[0], opening_at = details['opening_at']	, closing_at = details['closing_at'],  \
			is_ac = True, latitude = details['latitude'].strip(), longitude = details['longitude'].strip(), commission_percent = int(float(details['rate'])), \
			has_service_tax = float(details['service_tax']),thumbnail = img)
                new_studio_profile.save()
	        #stu_pic = StudioProfile.objects.get(id = obj.id)
	        #stu_pic.thumbnail = img
	        #stu_pic.save()
	        file_.close()
			#imz = File(thumbnail)
		#import pdb;pdb.set_trace();
		thumbnail.close()
		##account details
		account_no = re.findall(r'\d+', details['bank_account_no'].strip())[0]
		new_acc = StudioAccountDetails(studio_id =  new_studio_profile.id, bank_name = details['bank_name'].strip(), \
			bank_branch = details['bank_branch'].strip(),bank_ifsc = details['bank_ifsc_code'].strip(), bank_city = details['bank_city'].strip(), \
			bank_acc_number = account_no,service_updated ='new studio script', updated_date_time = \
			datetime.now(),name = details['acc_name'].strip())
		new_acc.save()

		path = '/home/mithu/Desktop/dataentry/'+parlour_name+'/pics/'
		onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
		print onlyfiles
		for i in onlyfiles:
			image_file = open(path+i)
			newfile_name = compressImages(image_file,i)
			if newfile_name:
				path2 = newfile_name
		        file_ = open(path2)
		        img = File(file_)
		        stu_pic = StudioPicture(studio_profile_id = new_studio_profile.id, picture = img, service_updated = \
		          'service_updated')
		        stu_pic.save()
		        file_.close()
		##studio closed details
		closed_on = []
		if details['closed_on_days'] != 'none':
			if "," in details['closed_on_days'] :
			    closed_on = details['closed_on_days'].split(",")
			else:
				closed_on = details['closed_on_days'].split(" ")
		for dyz in closed_on:
			if 'sun' in dyz.lower():
				closed_id = 1
			if 'mon' in dyz.lower():
				closed_id = 2
			if 'tue' in dyz.lower():
				closed_id = 3
			if 'wed' in dyz.lower():
				closed_id = 4
			if 'thu' in dyz.lower():
				closed_id = 5
			if 'fri' in dyz.lower():
				closed_id = 6
			if 'sat' in dyz.lower():
				closed_id = 7
			closed_on_dates = StudioClosedDetails(closed_on_id = closed_id, studio_id = new_studio_profile.id, 
					service_updated = 'new studio script', updated_date_time = datetime.now())
			closed_on_dates.save()
		###enter service types for studio

		services_in_studio = xlrd.open_workbook("/home/mithu/Desktop/dataentry/"+parlour_name+"/"+parlour_name+"Service.xls")
		studio_service_details = services_in_studio.sheet_by_index(0)
		service_details = {}
		service_types = []
		services = []
		for i in range(1,studio_service_details.nrows):
			obj ={}
			service_types.append(studio_service_details.row_values(i)[2])
			obj['service_name'] = studio_service_details.row_values(i)[1]
			obj['service_type'] = studio_service_details.row_values(i)[2]
			obj['duration'] = studio_service_details.row_values(i)[3]
			obj['rate'] = studio_service_details.row_values(i)[4]
			obj['sex'] = studio_service_details.row_values(i)[5]
			services.append(obj)
		service_types=set(service_types)
		for st in service_types:
			new_st =StudioServiceTypes(studio_profile_id = new_studio_profile.id, service_type_id = st,  \
				service_updated = "studio entry script", updated_date_time = datetime.now())
			new_st.save()
		for serz in services:
			try:
				is_there = Service.objects.filter(service_name = serz['service_name'].strip(),service_type_id = int(serz['service_type']), \
					min_duration = int(serz['duration']), is_active = True, service_for = int(serz['sex']))
				if details['has_group'] == 1:
					service_id = is_there[0].id
				else:
					new_service = Service(service_name = serz['service_name'].strip(),service_type_id = int(serz['service_type']), \
						min_duration = int(serz['duration']), is_active = True, service_for = int(serz['sex']), \
						service_updated = 'studio entry script', updated_date_time = datetime.now())
					new_service.save()
					service_id = new_service.id
				#enter service in studio
				new_st_ser = StudioServices(studio_profile_id = new_studio_profile.id, service_id = service_id,  \
					mins_takes = int(serz['duration']), price = int(serz['rate']),  \
					service_updated = 'studio entry script', updated_date_time = datetime.now())
				new_st_ser.save()
			except Exception as r:
				import pdb;pdb.set_trace();
				print(traceback.format_exc())
	except Exception as e:
		print repr(e)
		print(traceback.format_exc())
		transaction.rollback()
	else:
		try:
			transaction.commit()
		except Exception as d:
			print(traceback.format_exc())




@transaction.commit_manually        
def services_for_studio(studio_id,parlour_name):
	try:
		new_studio_profile = StudioProfile.objects.get(id = studio_id)
		details = {}
		details['has_group'] = 1
		services_in_studio = xlrd.open_workbook("/home/mithu/Desktop/dataentry/"+parlour_name+"/"+parlour_name+"Service.xls")
		studio_service_details = services_in_studio.sheet_by_index(0)
		service_details = {}
		service_types = []
		services = []
		for i in range(1,studio_service_details.nrows):
			obj ={}
			service_types.append(studio_service_details.row_values(i)[2])
			obj['service_name'] = studio_service_details.row_values(i)[1]
			obj['service_type'] = studio_service_details.row_values(i)[2]
			obj['duration'] = studio_service_details.row_values(i)[3]
			obj['rate'] = studio_service_details.row_values(i)[4]
			obj['sex'] = studio_service_details.row_values(i)[5]
			services.append(obj)
		service_types=set(service_types)
		import pdb;pdb.set_trace();
		for st in service_types:
			has_st_type = StudioServiceTypes.objects.filter(service_type_id = st, studio_profile_id = new_studio_profile.id)
			if not has_st_type:
				new_st =StudioServiceTypes(studio_profile_id = new_studio_profile.id, service_type_id = st,  \
					service_updated = "studio entry script", updated_date_time = datetime.now())
				new_st.save()
		for serz in services:
			try:
				is_there = Service.objects.filter(service_name = serz['service_name'].strip(),service_type_id = int(serz['service_type']), \
					min_duration = int(serz['duration']), is_active = True, service_for = int(serz['sex']))
				if details['has_group'] == 1 and is_there:
					service_id = is_there[0].id
				else:
					new_service = Service(service_name = serz['service_name'].strip(),service_type_id = int(serz['service_type']), \
						min_duration = int(serz['duration']), is_active = True, service_for = int(serz['sex']), \
						service_updated = 'studio entry script', updated_date_time = datetime.now())
					new_service.save()
					service_id = new_service.id
				#enter service in studio
				new_st_ser = StudioServices(studio_profile_id = new_studio_profile.id, service_id = service_id,  \
					mins_takes = int(serz['duration']), price = int(serz['rate']),  \
					service_updated = 'studio entry script', updated_date_time = datetime.now())
				new_st_ser.save()
			except Exception as r:
				print(traceback.format_exc())
	except Exception as e:
		print repr(e)
		print(traceback.format_exc())
		transaction.rollback()
	else:
		try:
			transaction.commit()
		except Exception as d:
			print(traceback.format_exc())





insert_studio_details("StylinAadambakkam")

#services_for_studio(studi_id,"name")
##insert studio group
##insert studio profile & thumbnail
##insert pictures
##insert account details
def insert_service_types():
	service_types = ['Haircut','Hair Colouring','Hair Spa','Massage','Skin Care/De-Tan','Bleach','Reflexology', \
'Manicure & Pedicure','Straightening & Curling','Style Bar','Threading','Waxing','Body Treatment/Body Bright',  \
'Facials','Makeup','Shave and Trim']
	for i in service_types:
		new_sst = ServiceType(service_name = i, description = i,is_active = True, service_updated ='studio entry script', \
			updated_date_time = datetime.now())
		new_sst.save()

#insert_service_types()

def insert_studio_kind_types():
	studio_kind  = ['Men','Women','Unisex']
	studio_type = ['Salon','Spa','Beauty Parlour']
	for ki in studio_kind:
		new_kind = StudioKind(kind_desc = ki, updated_date_time = datetime.now(), service_updated = 'studio entry script')
		new_kind.save()
	for ty in studio_type:
		new_type = StudioType(type_desc = ty, updated_date_time = datetime.now(), service_updated = 'studio entry script')
		new_type.save()

#insert_studio_kind_types()
