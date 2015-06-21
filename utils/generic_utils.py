##standard imports
from datetime import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.MIMEText import MIMEText
import os, sys


##third party imports
from oauthlib.common import generate_token
from oauth2_provider.settings import oauth2_settings
from django.http import JsonResponse
from oauth2_provider.models import AccessToken, Application, RefreshToken
from django.utils.timezone import now, timedelta
from django.contrib.auth import login
from social.apps.django_app.utils import psa
from django.http import HttpResponse

##application imports
from user_accounts.models import UserProfile
from django.conf import settings
from onepass.settings import SMTP_SERVER, SMTP_USERNAME, SMTP_PASSWORD, SMTP_PORT, SMTP_DO_TLS
#import logging

def get_token_json(access_token,app,refresh_token):
    """
    Takes an AccessToken instance as an argument
    and returns a JsonResponse instance from that
    AccessToken
    """
    token = {
        'access_token': access_token.token,
        'expire_time': oauth2_settings.ACCESS_TOKEN_EXPIRE_SECONDS,
        'token_type': 'Bearer',
        'scope': access_token.scope,
        'refresh_token':refresh_token,
        'client_id':app.client_id,
        'client_secret':app.client_secret
    }
    return JsonResponse(token)	


def access_token_gen(user):
    try:
        app = Application.objects.get(name="Facebook")
        old_access_token = AccessToken.objects.get(user=user,  \
        	application=app)
        old_refresh_token = RefreshToken.objects.get(user=user,  \
        	access_token=old_access_token)
    except:
        pass
    else:
        old_access_token.delete()
        old_refresh_token.delete()
    # we generate an access token
    token = generate_token()
    # we generate a refresh token
    refresh_token = generate_token()
    expires = now() + timedelta(seconds=oauth2_settings.ACCESS_TOKEN_EXPIRE_SECONDS)
    scope = "read write"
    # we create the access token
    access_token = AccessToken.objects.\
        create(user=user,
               application=app,
               expires=expires,
               token=token,
               scope=scope)
    # we create the refresh token
    RefreshToken.objects.\
        create(user=user,
               application=app,
               token=refresh_token,
               access_token=access_token)
    return get_token_json(access_token,app,refresh_token)

def social_auth_to_profile(backend, details, response, user=None, is_new=False, *args, **kwargs):
    try:
        dob = None
        sex = None
        city_state = None
        if response.has_key('birthday'):  
                dob = datetime.strptime(response['birthday'],'%m/%d/%Y').date()
        if response.has_key('gender'):
                sex = response['gender']
        if response.has_key('location') and len(response['location'])>0:
                if response['location'].has_key('name'):
                    city_state = response['location']['name']
        if is_new:
            if response.has_key('email'):
                profile = UserProfile()
                profile.user_acc_id = user.id
        else:
            UserProfile.objects.filter(user_acc = user).update(dob = dob,  \
                sex = sex, city_state = city_state,  \
                service_updated = 'User details updation', updated_date_time = \
                datetime.now())
        if is_new:
            profile.service_updated = "User first login"
            profile.facebook_id = response['id']
            profile.dob = dob
            profile.city_state = city_state
            profile.sex = sex
            profile.save()
    except Exception ,e:
        print repr(e)
        return None
    else:
        return user


def sendEmail(to, subject, message, raw = 0):
    server = smtplib.SMTP(host = SMTP_SERVER,port = SMTP_PORT,timeout = 10)
    server.starttls()
    server.login(SMTP_USERNAME, SMTP_PASSWORD)
    msg = MIMEMultipart()
    #logger = logging.getLogger('log.errors')
    fromaddr = 'vbnetmithun@gmail.com'
    msg['Subject'] = subject
    msg['From'] = "gopanther  <vbnetmithun@gmail.com>"
    to = "mittugotmail@gmail.com"
    msg['To'] = to
    msg.attach(MIMEText(message, 'html','utf-8'))
    toaddrs = to
    try:
        server.sendmail(fromaddr, toaddrs, msg.as_string())
    except Exception, err:
        #logger.error(err)
        server.quit()
        return False
    else:
        return True


def sendSMS(to,from_,body):
    from twilio.rest import TwilioRestClient
    client  = TwilioRestClient(settings.TWILIO_ID, settings.TWILIO_KEY)
    message = client.messages.create(to = to, from_= from_, body = message)
