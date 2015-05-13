##standard imports
from datetime import datetime

##third party imports
from oauthlib.common import generate_token
from oauth2_provider.settings import oauth2_settings
from django.http import JsonResponse
from oauth2_provider.models import AccessToken, Application, RefreshToken
from django.utils.timezone import now, timedelta
from django.contrib.auth import login
from social.apps.django_app.utils import psa

##application imports
from user_accounts.models import UserProfile

def get_token_json(access_token):
    """
    Takes an AccessToken instance as an argument
    and returns a JsonResponse instance from that
    AccessToken
    """
    token = {
        'access_token': access_token.token,
        'expires_in': oauth2_settings.ACCESS_TOKEN_EXPIRE_SECONDS,
        'token_type': 'Bearer',
        'refresh_token': access_token.refresh_token.token,
        'scope': access_token.scope
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
    return get_token_json(access_token)

def social_auth_to_profile(backend, details, response, user=None, is_new=False, *args, **kwargs):
    try:
        if is_new:
            if response.has_key('email'):
                profile = UserProfile()
                profile.user_acc_id = user.id
        else:
            if response.has_key('birthday'):  
                dob = datetime.strptime(response['birthday'],'%m/%d/%Y').date()
            if response.has_key('gender'):
                sex = response['gender']
            if response.has_key('location') and len(response['location'])>0:
                if response['location'].has_key('name'):
                    city_state = response['location']['name']
            UserProfile.objects.filter(user_acc = user).update(dob = dob,  \
                sex = sex, city_state = city_state,  \
                service_updated = 'User details updation')
        if is_new:
            profile.service_updated = "User first login"
            profile.facebook_id = response['id']
            profile.save()
        #as different function
        token = access_token_gen(user)
        access_token = token['access_token']
        user = request.backend.do_auth(request.GET.get('access_token'))
        if user:
            login(request, user)
            print "Logged in"
        print token
    except Exception ,e:
        print repr(e)