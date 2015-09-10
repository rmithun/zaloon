bank_name = ['HDFC','AXIS','KOTAK','SBI','ICICI','INDIAN BANK','IOB','IDBI','CITI']
bank_branch = ['Adyar','Guindy','Anna Nagar']
bank_ifsc = ['HDFC001','AXIS001','KOTAK001','SBI001','ICICI001','IB001','IOB001','IDBI001','CITI001']
bank_city = 'Chennai'
import random
import os,sys
import django
sys.path.append(os.path.join(os.path.dirname(__file__), 'onepass'))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..')))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "onepass.settings")
django.setup()
from studios.models import *
from django.db import transaction


studios = StudioProfile.objects.all()
for stu in studios:
	new_pay = StudioAccountDetails(studio = stu, bank_name = random.choice(bank_name),  \
		bank_branch = random.choice(bank_branch), bank_ifsc = random.choice(bank_ifsc),  \
		bank_city = 'Chennai',bank_acc_number = random.randint(1000000,9999999),  \
		service_updated = 'static script')
	new_pay.save()
