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
def studio_type():
	try:

		 studios = StudioProfile.objects.all().values('id')
		 ser_types = ServiceType.objects.all().values('id')
		 #import pdb;pdb.set_trace();
		 for stu in studios:
		 	for ser in ser_types:
		 		new_type = StudioServiceTypes(studio_profile_id = stu['id'],  \
		 			service_type_id = ser['id'], service_updated = "Admin")
		 		new_type.save()
	except:
		print traceback.format_exc()
		transaction.rollback()
	else:
		transaction.commit()


studio_type()