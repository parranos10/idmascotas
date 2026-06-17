from decouple import config
from pathlib import Path
from decouple import config
import cloudinary
import cloudinary.uploader
import cloudinary.api
# BASE DIRECTORY
BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=True, cast=bool)
ALLOWED_HOSTS = ['petqr.onrender.com',
                  '127.0.0.1',
                  'idsmascotas.com',
                  'www.idsmascotas.com'
                  ]


# APPLICATIONS
INSTALLED_APPS = [
    'cloudinary',
    'cloudinary_storage',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # TU APP
    'mascotas',
]


# MIDDLEWARE
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# URLS PRINCIPALES
ROOT_URLCONF = 'petqr.urls'


# TEMPLATES
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        # CARPETA TEMPLATES
        'DIRS': [BASE_DIR / 'templates'],

        'APP_DIRS': True,

        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# WSGI
WSGI_APPLICATION = 'petqr.wsgi.application'


# DATABASE
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# PASSWORD VALIDATION
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


# LANGUAGE
LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Guayaquil'

USE_I18N = True

USE_TZ = True


# STATIC FILES
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

STATIC_ROOT = BASE_DIR / 'staticfiles'
STORAGES = {
    "default": {
        "BACKEND": "cloudinary_storage.storage.MediaCloudinaryStorage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# MEDIA FILES
MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / 'media'


# DEFAULT PRIMARY KEY
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'dcutgvqcy',
    'API_KEY': '964466697263111',
    'API_SECRET': 'CSIetGrmPV2kzrkMkpRrLubettg',
}
cloudinary.config(
    cloud_name="dcutgvqcy",
    api_key="964466697263111",
    api_secret="CSIetGrmPV2kzrkMkpRrLubettg",
    secure=True
)

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')

EMAIL_TIMEOUT = 10











