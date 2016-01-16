"""
Django settings for onepass project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'a-o-a%mudeees3je=$2qaa132e3e*f3167h*50q(j)0khoty_&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ADMINS = (('Mithun', 'vbnetmithun@gmail.com'), ('Asha', 'asha.ruku93@gmail.com'),('Jawahar', 'jawahar7.ceg@gmail.com'))


SERVER_EMAIL = "donotreply@zaloon.in"

# Application definition

INSTALLED_APPS = (
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'oauth2_provider',
    'social.apps.django_app.default',
    'user_accounts',
    'booking',
    'studios',
    'gunicorn',
    'storages',

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'onepass.urls'

WSGI_APPLICATION = 'onepass.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases



# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

#STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATIC_URL = '/static/'





# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)


MEDIA_ROOT = BASE_DIR
AWS_STORAGE_BUCKET_NAME = 'noqimages'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_ACCESS_KEY_ID = 'AKIAIKMW5IUS3L2OCCRQ'
AWS_SECRET_ACCESS_KEY = '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'
AWS_S3_SECURE_URLS = False
MEDIAFILES_LOCATION = 'media'
AWS_CDN_URL = "http://dj44veg5gcpqb.cloudfront.net/"
MEDIA_URL = "http://%s/%s/" % (AWS_CDN_URL, MEDIAFILES_LOCATION)
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

if DEBUG:
    """STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    )"""
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'zaloon_prod',                      # Or path to database file if using sqlite3.
            # The following settings are not used with sqlite3:
            'USER': 'zaloon_dba',
            'PASSWORD': '11July!99#',
            'HOST': 'zaloon.cwh48zxk9diu.ap-southeast-1.rds.amazonaws.com',                      # Empty for localhost through domain sockets or           '127.0.0.1' for localhost through TCP.
            'PORT': '5432',                      # Set to empty string for default.
        }
    }
    
    #ALLOWED_HOSTS = []
    
    ##AWS DEV DB
    HOST_NAME = 'http://127.0.0.1:8000'
    # Additional locations of static files
    STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    )  
    """DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
    }
    
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'zaloon_dev',                      # Or path to database file if using sqlite3.
            # The following settings are not used with sqlite3:
            'USER': 'zaloon_dev',
            'PASSWORD': 'Zaloon123',
            'HOST': 'zaloon-dev.cyscy0cpjemo.ap-southeast-1.rds.amazonaws.com',
            'PORT': '5432',                      # Set to empty string for default.
        }
    }
    """
 

    ALLOWED_HOSTS = []
    HOST_NAME = 'http://www.dev.zaloon.in'
else:
    # Additional locations of static files
    STATICFILES_DIRS = (
    
        "static/",
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    )
    STATICFILES_LOCATION = 'static'
    STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    STATIC_URL = "https://%s/%s/" % (AWS_CDN_URL, STATICFILES_LOCATION)
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'zaloon_prod',                      # Or path to database file if using sqlite3.
            # The following settings are not used with sqlite3:
            'USER': 'zaloon_dba',
            'PASSWORD': '11July!99#',
            'HOST': 'zaloon.cwh48zxk9diu.ap-southeast-1.rds.amazonaws.com',                      # Empty for localhost through domain sockets or           '127.0.0.1' for localhost through TCP.
            'PORT': '5432',                      # Set to empty string for default.
        }
    }
    #ALLOWED_HOSTS = []
    ALLOWED_HOSTS = ['zaloon.in','www.zaloon.in','http://zaloon.in','http://www.zaloon.in',  \
    'https://zaloon.in','https://www.zaloon.in']


#AWS SES SMTP SETTINGS
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
SMTP_SERVER = 'email-smtp.eu-west-1.amazonaws.com'
SMTP_USERNAME = 'AKIAI3AQZ6M5Y4GARYKQ'
SMTP_PASSWORD = 'ArAUIN7BrYD/0fAIzOVXVNAnCLd3KCIEObM1ix1aty4n'
SMTP_PORT = '587'
SMTP_DO_TLS = True
BCC_EMAIL = 'vbnetmithun@gmail.com' 



TEMPLATE_DIRS = (
     os.path.join(BASE_DIR, 'templates/'),
)
TEMPLATE_LOADERS = (

    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',

)



TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
     "django.core.context_processors.request",
)

AUTHENTICATION_BACKENDS = (
    'social.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)


REST_FRAMEWORK = {
 'DEFAULT_AUTHENTICATION_CLASSES': (
        'oauth2_provider.ext.rest_framework.OAuth2Authentication',
    ),
 'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
 'DEFAULT_THROTTLE_RATES': {
        'anon': '5/day',  ##change before going live
        'user': '10/day'
    }

}


OAUTH2_PROVIDER = {
    # this is the list of available scopes
    'SCOPES': {'read': 'Read scope', 'write': 'Write scope'}
}

SOCIAL_AUTH_FACEBOOK_KEY = 442685319234348 #test
SOCIAL_AUTH_FACEBOOK_KEY = 442681529234727 #production
SOCIAL_AUTH_FACEBOOK_SECRET = '514402ab5b5f424bb288737376f508d3' #test
SOCIAL_AUTH_FACEBOOK_SECRET = '4a43863afe181c1c014f669cceae3d92' #production


SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    #'social.pipeline.social_auth.associate_by_email',
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details',
    'utils.generic_utils.social_auth_to_profile'
)


SOCIAL_AUTH_FACEBOOK_SCOPE = ['email', 'user_location','user_birthday']
SOCIAL_AUTH_USERNAME_IS_FULL_EMAIL = True
SOCIAL_AUTH_FACEBOOK_EXTRA_DATA = [('gender','gender')]
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/account/home/'
SOCIAL_AUTH_DISCONNECT_REDIRECT_URL = '/'


FBAPIKEY = 442685319234348

PLIVO_ID = 'MAZGRINGVMODA2MJDJNG'
PLIVO_KEY = 'MzFkYWZmZDQ3YmQ3YTRkODY1NGNmZGVmZWRhOGVl'

VENV_ROOT = os.path.dirname(os.path.abspath(__file__))
REQ_RES_PATH = VENV_ROOT.split('/')[1:-1]
REQ_RES_PATH = '/'.join(REQ_RES_PATH)
LOG_PATH = '/'+REQ_RES_PATH+'/logs/'

###logging
LOGGING = {
        'version': 1,
        'disable_existing_loggers': True,
        'formatters': {
            'verbose': {
                'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
            },
            'simple': {
                'format': '%(levelname)s %(message)s'
            },
        },
        'handlers': {
            'file_booking': {                # define and name a handler
                'level': 'DEBUG',
                'class': 'logging.FileHandler', # set the logging class to log to a file
                'formatter': 'verbose',         # define the formatter to associate
                'filename': os.path.join(LOG_PATH, 'booking.log') # log file
            },
    
            'file_studios': {                 
                'level': 'DEBUG',
                'class': 'logging.FileHandler', # set the logging class to log to a file
                'formatter': 'verbose',         # define the formatter to associate
                'filename': os.path.join(LOG_PATH, 'studios.log')  # log file
            },
            
            'req_res_log': {                 
                'level': 'DEBUG',
                'class': 'logging.FileHandler', # set the logging class to log to a file
                'formatter': 'verbose',         # define the formatter to associate
                'filename': os.path.join(LOG_PATH,  'req_res_log.log')  # log file
            },
    
            'user_account_log': {                 
                'level': 'DEBUG',
                'class': 'logging.FileHandler', # set the logging class to log to a file
                'formatter': 'verbose',         # define the formatter to associate
                'filename': os.path.join(LOG_PATH, 'user_account.log')  # log file
            },

            'daily_scripts_log': {                 
                'level': 'DEBUG',
                'class': 'logging.FileHandler', # set the logging class to log to a file
                'formatter': 'verbose',         # define the formatter to associate
                'filename': os.path.join(LOG_PATH, 'daily_scripts.log')  # log file
            },
    
            'file_applicationerror': {                 
                'level': 'DEBUG',
                'class': 'logging.FileHandler', # set the logging class to log to a file
                'formatter': 'verbose',         # define the formatter to associate
                'filename': os.path.join(LOG_PATH, 'errors.log')  # log file
            },
    
        },
        'loggers': {
            'log.booking': {              # define a logger - give it a name
                'handlers': ['file_booking'], # specify what handler to associate
                'level': 'INFO',                 # specify the logging level
                'propagate': True,
            },     
    
            'log.studios': {               # define another logger
                'handlers': ['file_studios'],  # associate a different handler
                'level': 'INFO',                 # specify the logging level
                'propagate': True,
            },        
    
            'log.req_res': {               # define another logger
                'handlers': ['req_res_log'],  # associate a different handler
                'level': 'INFO',                 # specify the logging level
                'propagate': True,
            },   
            
            'log.user_account': {               # define another logger
                'handlers': ['user_account_log'],  # associate a different handler
                'level': 'DEBUG',                 # specify the logging level
                'propagate': True,
            },
            'log.daily_scripts': {               # define another logger
                'handlers': ['daily_scripts_log'],  # associate a different handler
                'level': 'DEBUG',                 # specify the logging level
                'propagate': True,
            },
    
           'log.errors': {               # define another logger
                'handlers': ['file_applicationerror'],  # associate a different handler
                'level': 'ERROR',                 # specify the logging level
                'propagate': True,
            },
    
    
    }
}

##MEMCACHE

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}



##RAZORPAY SETTINGS
if DEBUG:
    RZP_KEY_ID = 'rzp_test_bKVgZ668B7jtSR'
    RZP_SECRET_KEY = 'xn0zaYvoB90aUwLu2bad8oSs'
else:
    RZP_KEY_ID = 'rzp_live_RYXktqbBE8xIJb'
    RZP_SECRET_KEY = 'UWgcD2L2UrlQxzOz2B8i2WM1'

##CCAVENUE SETTINGS
MERCHANT_ID = 71637
WORKING_KEY = '1A69CD164CBEB1F1822010B3E0495369'
ACCESS_CODE = 'AVNI05CG68BJ32INJB'
CURRENCY = 'INR'
if DEBUG:
    REDIRECT_URL = 'www.zaloon.in/paymentsuccess/'
    CANCEL_URL =  'www.zaloon.in/paymentfailed/'
else:
    REDIRECT_URL = 'www.zaloon.in/paymentsuccess/'
    CANCEL_URL =  'www.zaloon.in/paymentfailed/'
LANGUAGE = 'EN'
INTEGRATION_TYPE = "iframe_normal"



