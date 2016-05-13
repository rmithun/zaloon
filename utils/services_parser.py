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
def service_parse():
	try:
		mins = range(15,165,15)
		data = open('/home/mithun/Desktop/test.html')
		parsed=BeautifulSoup(data,"html5lib")
		services = parsed.findAll('ul')
		for itsm in services:
			new_service = Service(service_type_id = 5, min_duration = random.choice(mins),service_name = itsm.find('li').text, \
				service_for = 3)
			new_service.save()
	except:
		transaction.rollback()
	else:
		transaction.commit()



service_parse()