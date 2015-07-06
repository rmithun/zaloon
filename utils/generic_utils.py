##standard imports
from datetime import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.MIMEText import MIMEText
import os, sys
import logging
import traceback


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

logger_user = logging.getLogger('log.user_account')
logger_error = logging.getLogger('log.errors')


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
    logger_user.info("JSON for tokens created")
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
        logger_error.error(traceback.format_exc())
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
    logger_user.info("Token created")
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
            logger_user.info("New User")
            if response.has_key('email'):
                profile = UserProfile()
                profile.user_acc_id = user.id
        else:
            logger_user.info("Exisiting user return ")
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
        logger_error.error(traceback.format_exc())
        return None
    else:
        logger_user.info("Profile created/updated")
        return user


def sendEmail(to, subject, message, *args):
    server = smtplib.SMTP(host = SMTP_SERVER,port = SMTP_PORT,timeout = 10)
    server.starttls()
    server.login(SMTP_USERNAME, SMTP_PASSWORD)
    msg = MIMEMultipart()
    fromaddr = 'donotreply@zaloon.in'
    msg['Subject'] = subject
    msg['From'] = "Zaloon.in <donotreply@zaloon.in>"
    to = "mittugotmail@gmail.com"
    msg['To'] = to
    msg.attach(MIMEText(message, 'html','utf-8'))
    
    if args:
        attachFile = MIMEBase('application', 'pdf')    
        attachFile.set_payload( open(args[0],"rb").read())    
        Encoders.encode_base64(attachFile)    
        attachFile.add_header('Content-Disposition', 'attachment; filename="%s"'% os.path.basename(args[0]))
        msg.attach(attachFile)       
    try:
        server.sendmail(fromaddr, to, msg.as_string())
    except Exception, err:
        logger_error.error(traceback.format_exc())
        server.quit()
        return False
    else:
        server.quit()
        return True


def sendSMS(to,body):

    try:
        import plivo
        auth_id = settings.PLIVO_ID
        auth_token = settings.PLIVO_KEY
        p = plivo.RestAPI(auth_id, auth_token)
        # Send a SMS
        params = {
            'src': 'ZALOON', # Caller Id
            'dst' : '91'+to, # User Number to Call
            'text' : body,
            'type' : "sms",
        }
        response = p.send_message(params)
    except:
        logger.error(traceback.format_exc())
        return False
    else:
        if response:
            return True
        else:
            return False
