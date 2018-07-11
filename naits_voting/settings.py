import os

import environ

env = environ.Env()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

APPS_DIR = os.path.join(BASE_DIR, 'bitpoint')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'i@bqy_zn5p#xeoi0l@1zv=56g32--=i2lw-#h@py#bt6mi5fxn'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
	# third party apps: for tagging and ayncronous messeging
    'taggit',
    'channels',

    # third party apps: for admin UI
    'jet.dashboard',
    'jet',
    # django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',

    # third party app: used in login page for appending html attributes to input fields
    'widget_tweaks',

    # Local Apps
    'bitpoint.authentication',
    'bitpoint.voting',
    'bitpoint.messenger',
    'bitpoint.articles',
    'bitpoint.discussion',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'naits_voting.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'naits_voting.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'naits',
        'USER': 'abdul',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}



# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

LOGIN_REDIRECT_URL = '/'

AUTH_USER_MODEL = 'authentication.User'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

TAGGIT_CASE_INSENSITIVE = True

# REDIS setup
redis_host = os.environ.get('REDIS_HOST', 'localhost')

# Channels configuration

# CHANNEL_LAYERS = {
#     'default': {
#         'BACKEND': 'asgi_redis.RedisChannelLayer',
#         'CONFIG': {
#             'hosts': [REDIS_URL, ],
#         },
#         'ROUTING': 'config.routing.channel_routing',
#     }
# }

#CHANNEL_LAYERS = {
#   "default": {
#        # This example app uses the Redis channel layer implementation channels_redis
#        "BACKEND": "channels_redis.core.RedisChannelLayer",
#        "CONFIG": {
#            "hosts": [(redis_host, 6379)],
#        },
#    },
#}

# ASGI_APPLICATION = 'naits_voting.routing.application'

# EMAIL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND', default='django.core.mail.backends.smtp.EmailBackend')



##### Project-specific settings

NOTIFY_USERS_ON_ENTER_OR_LEAVE_ROOMS = True

MSG_TYPE_MESSAGE = 0  # For standard messages
MSG_TYPE_WARNING = 1  # For yellow messages
MSG_TYPE_ALERT = 2  # For red & dangerous alerts
MSG_TYPE_MUTED = 3  # For just OK information that doesn't bother users
MSG_TYPE_ENTER = 4  # For just OK information that doesn't bother users
MSG_TYPE_LEAVE = 5  # For just OK information that doesn't bother users

MESSAGE_TYPES_CHOICES = (
    (MSG_TYPE_MESSAGE, 'MESSAGE'),
    (MSG_TYPE_WARNING, 'WARNING'),
    (MSG_TYPE_ALERT, 'ALERT'),
    (MSG_TYPE_MUTED, 'MUTED'),
    (MSG_TYPE_ENTER, 'ENTER'),
    (MSG_TYPE_LEAVE, 'LEAVE'),
)

MESSAGE_TYPES_LIST = [
    MSG_TYPE_MESSAGE,
    MSG_TYPE_WARNING,
    MSG_TYPE_ALERT,
    MSG_TYPE_MUTED,
    MSG_TYPE_ENTER,
    MSG_TYPE_LEAVE,
]
