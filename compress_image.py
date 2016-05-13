from PIL import Image, ImageFile
from os.path import getsize
from os import listdir
from datetime import datetime
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
import urllib2 as urllib
import io,random





@transaction.commit_manually
def AddImages(obj,path):
  try:
    #import pdb;pdb.set_trace();
    filename = obj.thumbnail.url
    thumbail_path = '/home/asha/Desktop/DataEntry/'+path+'/thumbnail/'
    thumbs = [f for f in listdir(thumbail_path) if isfile(join(thumbail_path, f))]
    image_file = open(thumbail_path+thumbs[0])
    newfile_name = compressImages(image_file,thumbs[0])
    if newfile_name:
        path2 = newfile_name
        file_ = open(path2)
        img = File(file_)
        stu_pic = StudioProfile.objects.get(id = obj.id)
        stu_pic.thumbnail = img
        stu_pic.save()
        file_.close()
    pics_path = '/home/asha/Desktop/DataEntry/'+path+'/pics/'
    onlyfiles = [f for f in listdir(pics_path) if isfile(join(pics_path, f))]
    stu_pic = StudioPicture.objects.filter(studio_profile_id = obj.id)
    stu_pic.delete()
    for i in onlyfiles:
      image_file = open(pics_path+i)
      newfile_name = compressImages(image_file,i)
      if newfile_name:
        path2 = newfile_name
        file_ = open(path2)
        img = File(file_)
        stu_pic = StudioPicture(studio_profile_id = obj.id, picture = img, service_updated = \
          'service_updated')
        stu_pic.save()
        file_.close()
  except Exception as e:
    print repr(e)
    transaction.rollback()
  else:
    transaction.commit()




"""
26 Sparkle Blue,Ramapuram
27 The Halt
31 Naturals,Porur
34 O'range Family Salon, Chennai
35 Studio Profile
36 Essensuals,Iyyappanthangal
38 Essensuals,Nandambakkam
20 Naturals,Ramapuram
39 Essensuals,Porur"""
obj = StudioProfile.objects.filter(id = 39)[0]
AddImages(obj,'essensualsporur')
 

