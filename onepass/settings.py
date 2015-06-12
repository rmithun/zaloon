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






# Application definition

INSTALLED_APPS = (
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

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATIC_URL = '/static/'


STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

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


if 0:
    STATIC_URL = '/static/'
    STATIC_URL = '/static/'
    STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    )
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
    }
    ALLOWED_HOSTS = []
else:
    STATICFILES_LOCATION = 'static'
    STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    STATIC_URL = "https://%s/%s/" % (AWS_CDN_URL, STATICFILES_LOCATION)
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'bopanther_test_db',                      # Or path to database file if using sqlite3.
            # The following settings are not used with sqlite3:
            'USER': 'bopanther_dba',
            'PASSWORD': '11July!99#',
            'HOST': 'bopanther.cwh48zxk9diu.ap-southeast-1.rds.amazonaws.com',                      # Empty for localhost through domain sockets or           '127.0.0.1' for localhost through TCP.
            'PORT': '5432',                      # Set to empty string for default.
        }
    }
    #ALLOWED_HOSTS = ['bebalance.com', 'http://bebalance.com']
    ALLOWED_HOSTS = []






TEMPLATE_DIRS = (
    'templates/',
)
TEMPLATE_LOADERS = (

    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',

)



TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
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
    )

}


OAUTH2_PROVIDER = {
    # this is the list of available scopes
    'SCOPES': {'read': 'Read scope', 'write': 'Write scope'}
}

SOCIAL_AUTH_FACEBOOK_KEY = 442685319234348
SOCIAL_AUTH_FACEBOOK_SECRET = '514402ab5b5f424bb288737376f508d3'


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
