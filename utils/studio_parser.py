from bs4 import BeautifulSoup
import os,sys
import django
sys.path.append(os.path.join(os.path.dirname(__file__), 'onepass'))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..')))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "onepass.settings")
django.setup()
from django.db.models import Q
from studios.models import *
import requests,random,os
from datetime import datetime
from django.db import transaction
from django.core.files import File
import traceback

@transaction.commit_manually
def parse_and_store():
	try:
		data = open('/home/jawahar/Downloads/Thiruvanmiyur.xml')
		
		parsed=BeautifulSoup(data,"html5lib")
		shops = parsed.findAll('shop')
		password = 'dummy'
		service_updated = 'Parse Script'
		names = ['asha','mithun','jawahar','ravi','muni','raja','kedar','vijay','peter','john','aakash',  \
		'raju','srini','syed','magesh','vasu','anand','rajesh','prabhu','adish','nirmal','praveen',  \
		'lalilth','ajay','ajeez','mani','sahul','mukesh','raju','guru','viki','vikram']
		has_online_payment = 1
		commission = 10
		for every_shop in shops:
			name =  every_shop.find('name').text
			address = every_shop.find('address').text
			timing = every_shop.find('timing').text
			phones = every_shop.find('phones').text
			latitude = every_shop.find('latitude').text
			longitude = every_shop.find('longitude').text
			address_split = address.split(',')
			if len(address_split) > 4:
				landmark = address_split[4]
				address_2 = address_split[2]
				address_1 = address_split[0]+','+address_split[1]
			elif len(address_split) == 4:
				landmark = address_split[3]
				address_2 = address_split[2]
				address_1 = address_split[0]+','+address_split[1]
			elif len(address_split) == 3:
				landmark = ''
				address_2 = address_split[1]
				address_1 = address_split[0]
			area = address_2.strip()
			name_split= name.split(' ')
			if len(name_split) == 1:
				name_split.append(000000)
			email = "zalo_"+name_split[0]+"_"+area.split(' ')[0]+"@gmail.com"
			group = StudioGroup.objects.filter((Q(group_name__contains = name_split[0])|  \
				Q(group_name__contains = name_split[1]))).values('id','group_name')
			if len(group) == 0:
				group = StudioGroup.objects.filter(group_name = 'No branches').values('id','group_name')
			group_id =  group[0]['id']
			if 'parlour' in name.lower():
				studio_type = 3
			elif 'salon' in name.lower():
			    studio_type = 1
			elif 'spa' in name.lower():
			    studio_type = 2
			else:
			    studio_type = 1 
			if 'chennai' in landmark.lower():
				landmark = ''
			print area
			data = requests.get(("https://maps.googleapis.com/maps/api/place/autocomplete/json?input=%s&types=geocode&key=AIzaSyDLYJn4fbF_JCQs5YU2tJ5qGQGjtYHm_Uo")%(area))
			g_places = eval(data.content)
			search_field1 = g_places['predictions'][0]['description']
			search_field2 = search_field1
			nos = []
			for item in  (phones.strip()).split(' '):
				for no in item.split('-'):
					if len(no)> 5:
						nos.append(no.rstrip())
			nos.sort(key = len)
			landline = None
			contact = None
			contact_name = None
			if len(nos)==3:
				landline = "044"+str(nos[0])
				incharge = nos[1]
				incharge_name = random.choice(names)
				contact = nos[2]
				contact_name = random.choice(names)
			elif len(nos) == 2:
				incharge = nos[0]
				incharge_name = random.choice(names)
				contact = nos[1]
				contact_name = random.choice(names)
			else:
				incharge = nos[0]
				incharge_name = random.choice(names)
			timins = timing.split('to')
			from_time = timins[0].split(' ')[0]
			print name
			print timins
			to_time = timins[1].strip().split(' ')[0]
			from_hour = from_time[0:2]
			if from_time[3:] not in ['00','15','30','45']:
				from_mins = '00'
			else:
				from_mins = from_time[3:]
			if to_time[3:] not in ['00','15','30','45']:
				to_mins = '00'
			else:
				to_mins = (to_time[3:])
				if len(to_mins) != 2:
					to_mins = "00"
			to_hour = int(to_time[0:2])+12
			if to_hour > 23:
				to_hour = 23
			str1 = from_hour+":"+str(from_mins)+":"+"00"
			str2 = str(to_hour)+":"+str(to_mins)+":"+"00"
			from_ti = datetime.strptime(str1,'%H:%M:%S').time()
			to_ti = datetime.strptime(str2,'%H:%M:%S').time()
			kind = 3
			if 'men' in name.lower():
				kind = 1
			if 'women' in name.lower():
				kind = 2
			file_name = '/home/jawahar/Downloads/images/'+random.choice(os.listdir("/home/jawahar/Downloads/images"))
			imgz = open(file_name)
			img = File(imgz)
			has_studio = Studio.objects.filter(email = email)
			if len(has_studio) == 0:
				new_studio = Studio(email = email, password = password, is_active = 1)
				new_studio.save()
				profile = StudioProfile(studio = new_studio, studio_type_id = studio_type, \
					studio_kind_id = kind, studio_group_id = group_id, name = name,  \
					address_1 = address_1, address_2 = address_2, landmark = landmark, area = area,  \
					search_field_1 = search_field1, search_field_2 = search_field2, landline_no_1 = landline, \
					incharge_mobile_no = incharge, contact_mobile_no = contact , in_charge_person=  \
					incharge_name, contact_person = contact_name, opening_at = from_ti, closing_at = \
					to_ti, thumbnail = img, service_updated = service_updated, latitude = latitude,  \
					longitude = longitude)
				profile.save()
				imgz.close()
				for i in range(0,5):
					file_name = '/home/jawahar/Downloads/images/'+random.choice(os.listdir("/home/jawahar/Downloads/images"))
					imgz = open(file_name)
					img = File(imgz)
					stu_pic = StudioPicture(studio_profile = profile, picture = img, service_updated =service_updated)
					stu_pic.save()
					imgz.close()
				close = random.choice([1,2,3,4,5,6,7])
				no_close = random.choice([2,4,5,8,12,10,13])
				if no_close%2 != 0:
					stu_closed = StudioClosedDetails(studio = profile, closed_on_id = close, service_updated = service_updated )
					stu_closed.save()
					if no_close == 13:
						stu_closed = StudioClosedDetails(studio = profile, closed_on_id = 5, service_updated = service_updated )
						stu_closed.save()
				range_ = random.choice([5,20,50,80,168,90,30,40,43,25,75])
				mins = range(15,165,15)
				for i in range(132,(132+range_)):
					service = Service.objects.get(id = i)
					stu_serv = StudioServices(studio_profile = profile, service = service, mins_takes = random.choice(mins),  \
					price = (random.randint(10,90)*4),service_updated = service_updated)
					stu_serv.save()
	except:
		print traceback.format_exc()
		transaction.rollback()
	else:
		transaction.commit()
		





		


	

parse_and_store()