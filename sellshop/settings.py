from django.utils.translation import gettext_lazy as _
from pathlib import Path
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
import os
import datetime
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-hn^-(8cyozfq7k^t#m5utj=f2wd42y3x+an@xq$lggs43ejn*f'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True 
DEBUG = int(os.environ.get("DEBUG", default=1))
PROD = not DEBUG
SECRET_KEY = os.environ.get("SECRET_KEY", "5%&49jgugn%x-_msxcwx%bc8#n90q%+lnw-23jwql+_8i$gyb+")
ALLOWED_HOSTS = ['*'] # os.environ.get("ALLOWED_HOSTS", "").split(" ")

from django.contrib.messages import constants as messages

# Application definition
PARLER_LANGUAGES = {
    None: (
        {'code': 'en',}, # English
        {'code': 'az',}, # Azerbaijan

    ),
    'default': {
        'fallbacks': ['en'],
        'hide_untranslated': False,
    }
}
INSTALLED_APPS = [
    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social_django',
    'sellshop',
    'accounts',
    'core',
    'blog',
    'order',
    'product',
    'rest_framework',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'rest_registration',
    'django_filters',
    'crispy_forms',
    'star_ratings',
    "corsheaders",
    'paypal.standard.ipn',    
    'django_celery_beat',
    'rosetta',
     'parler',

]
PAYPAL_RECEIVER_EMAIL = 'kamrann.nariman@gmail.com'

PAYPAL_TEST = True
SIMPLE_JWT  = {
    'ACCESS_TOKEN_LIFETIME': datetime.timedelta(days=5),
    'REFRESH_TOKEN_LIFETIME': datetime.timedelta(days=5),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True
}


DBBACKUP_STORAGE = 'django.core.files.storage.FileSystemStorage'
DBBACKUP_STORAGE_OPTIONS = {'location': '/backups/'}
MIDDLEWARE = [

    # 'blog.middlewares.BlockIPMiddleware',
    'request_logging.middleware.LoggingMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',

]
CORS_ALLOW_ALL_ORIGINS = True

# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'handlers': {
#         'file': {
#             'level': 'INFO',
#             'class': 'logging.FileHandler',
#             'filename': 'sellshop/middlewares/logs.txt',
#         },
#     },
#     'loggers': {
#         'django.request': {
#             'handlers': ['file'],
#             'level': 'INFO',  # change debug level as appropiate
#             'propagate': True,
#         },
#     },
# }

ROOT_URLCONF = 'sellshop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
                'tools.context.main_context'
            ],
        },
    },
]


LOCALE_PATHS = [
    BASE_DIR / 'locale/',
]

WSGI_APPLICATION = 'sellshop.wsgi.application'


# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB'),
        'HOST': os.environ.get('POSTGRES_HOST'),
        'PORT': os.environ.get('POSTGRES_PORT'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD')
    }
    # 'default': {
    #     'ENGINE': os.environ.get("DB_ENGINE",'django.db.backends.postgresql'),
    #     'NAME': os.environ.get("DB_NAME",'sellshop'),
    #     'USER': os.environ.get("DB_USER",'postgres'),
    #     'PASSWORD': '123',
    #     'HOST': 'localhost',
    #     'PORT': 5432,
        
    # }
}



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


LANGUAGE_CODE = 'en'

LANGUAGES = (
    ('en', _('English')),
    ('az', _('Azerbaijan')),
    ('hy', _('Armenian')),
)

MODELTRANSLATION_DEFAULT_LANGUAGE = 'en'

MODELTRANSLATION_LANGUAGES = ('en', 'az')

USE_I18N = True

USE_L10N = True

USE_TZ = True

TIME_ZONE = 'Asia/Baku'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATIC_URL = 'static/'
if PROD:
    STATIC_ROOT = os.path.join(BASE_DIR, "static")
else:
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "static")
    ]
# STATICFILES_DIRS = ["static"]
# STATIC_ROOT = BASE_DIR / "staticfiles"
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")

AUTH_USER_MODEL = 'accounts.User'

AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'home'

LOGOUT_URL = 'logout'

LOGOUT_REDIRECT_URL = 'login'

SOCIAL_AUTH_FACEBOOK_KEY = '539312060905517'  # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = '50d577418bd1bfe2efe14884c6ae268e'  # App Secret

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '904866318192-a8nfkmqmgikjn0p54i8gtkuj8cc5ncgt.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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'

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'
SOCIAL_AUTH_LOGIN_URL = '/'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

CELERY_BROKER_URL = "redis://redis:6379"
CELERY_RESULT_BACKEND ="redis://redis:6379"
CELERY_TIMEZONE = "Asia/Baku"
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_TRACK_STARTED = True
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'
# CELERY_TASK_TIME_LIMIT = 30 * 60

REST_REGISTRATION = {
    'REGISTER_VERIFICATION_ENABLED': False,
    'RESET_PASSWORD_VERIFICATION_ENABLED': False,
    'REGISTER_EMAIL_VERIFICATION_ENABLED': False,
}


SESSION_EXPIRE_AT_BROWSER_CLOSE = False
SESSION_COOKIE_AGE = 30 * 60


MESSAGE_TAGS = {
        messages.DEBUG: 'secondary',
        messages.INFO: 'info',
        messages.SUCCESS: 'success',
        messages.WARNING: 'warning',
        messages.ERROR: 'danger',
}   
EMAIL_BACKEND = os.environ.get('EMAIL_BACKEND') 
EMAIL_HOST = os.environ.get('EMAIL_HOST') 
EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS') 
EMAIL_PORT = os.environ.get('EMAIL_PORT') 
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER') 
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD') 

    