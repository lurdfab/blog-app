"""
Django settings for blogapp project.

Generated by 'django-admin startproject' using Django 4.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
from decouple import config
from datetime import timedelta #required for the simpleJWT

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', cast=bool)

ALLOWED_HOSTS = []

AUTH_USER_MODEL = "users.User"
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #project apps
    'blogapi',
    'users',



    # Third party apps
    'rest_framework',
    'django_filters',
    'rest_framework.authtoken', #this is the restframework token authentication
    'rest_framework_simplejwt', #this is a third token provider JWT
  
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

ROOT_URLCONF = 'blogapp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'blogapp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": 'django.db.backends.postgresql_psycopg2',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config("DB_PORT"),
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True




LANGUAGES = [
    #("af", "Afrikaans"),  # Afrikaans
    ("ar", "العربية‏"),  # Arabic
    #("ast", "Asturiano"),  # Asturian
    #("az", "Azərbaycan dili"),  # Azerbaijani
    #("bg", "Български"),  # Bulgarian
    #("be", "Беларуская"),  # Belarusian
    #("bn", "বাংলা"),  # Bengali
    #("br", "Bretón"),  # Breton
    #("bs", "Bosanski"),  # Bosnian
    ("ca", "Català"),  # Catalan
    # ("cs", "Čeština"),  # Czech
    # ("cy", "Cymraeg"),  # Welsh
    ("da", "Dansk"),  # Danish
    ("de", "Deutsch"),  # German
    # ("el", "Ελληνικά"),  # Greek
    ("en", "English (US)"),  # English
    # ("en-au", "English (Australia)"),  # Australian English
    # ("en-gb", "English (UK)"),  # British English
    # ("eo", "esperanta"),  # Esperanto
    ("es", "Español"),  # Spanish
    # ("es-ar", "Español (Argentina)"),  # Argentinian Spanish
    # ("es-mx", "Español (México)"),  # Mexican Spanish
    # ("es-ni", "Español (Nicaragua)"),  # Nicaraguan Spanish
    # ("es-ve", "Español (Venezuela)"),  # Venezuelan Spanish
    # ("et", "Eesti"),  # Estonian
    ("eu", "Euskara"),  # Basque
    ("fa", "فارسی‏"),  # Persian
    ("fi", "Suomi"),  # Finnish
    ("fr", "Français"),  # French
    # ("fy", "Frysk"),  # Frisian
    # ("ga", "Irish"),  # Irish
    # ("gl", "Galego"),  # Galician
    ("he", "עברית‏"),  # Hebrew
    # ("hi", "हिन्दी"),  # Hindi
    # ("hr", "Hrvatski"),  # Croatian
    # ("hu", "Magyar"),  # Hungarian
    # ("ia", "Interlingua"),  # Interlingua
    # ("id", "Bahasa Indonesia"),  # Indonesian
    # ("io", "IDO"),  # Ido
    # ("is", "Íslenska"),  # Icelandic
    ("it", "Italiano"),  # Italian
    ("ja", "日本語"),  # Japanese
    # ("ka", "ქართული"),  # Georgian
    # ("kk", "Қазақша"),  # Kazakh
    # ("km", "ភាសាខ្មែរ"),  # Khmer
    # ("kn", "ಕನ್ನಡ"),  # Kannada
    ("ko", "한국어"),  # Korean
    # ("lb", "Lëtzebuergesch"),  # Luxembourgish
    # ("lt", "Lietuvių"),  # Lithuanian
    ("lv", "Latviešu"),  # Latvian
    # ("mk", "Македонски"),  # Macedonian
    # ("ml", "മലയാളം"),  # Malayalam
    # ("mn", "Монгол"),  # Mongolian
    # ("mr", "मराठी"),  # Marathi
    # ("my", "မြန်မာ"),  # Burmese
    ("nb", "Norsk (bokmål)"),  # Norwegian Bokmal
    # ("ne", "नेपाली"),  # Nepali
    ("nl", "Nederlands"),  # Dutch
    # ("nn", "Norsk (nynorsk)"),  # Norwegian Nynorsk
    # ("os", "Ирон æвзаг"),  # Ossetic
    # ("pa", "ਪੰਜਾਬੀ"),  # Punjabi
    ("pl", "Polski"),  # Polish
    # ("pt", "Português (Portugal)"),  # Portuguese
    ("pt-br", "Português (Brasil)"),  # Brazilian Portuguese
    # ("ro", "Română"),  # Romanian
    ("ru", "Русский"),  # Russian
    # ("sk", "Slovenčina"),  # Slovak
    # ("sl", "Slovenščina"),  # Slovenian
    # ("sq", "Shqip"),  # Albanian
    ("sr", "Српски"),  # Serbian
    # ("sr-latn", "srpski"),  # Serbian Latin
    ("sv", "Svenska"),  # Swedish
    # ("sw", "Kiswahili"),  # Swahili
    # ("ta", "தமிழ்"),  # Tamil
    # ("te", "తెలుగు"),  # Telugu
    # ("th", "ภาษาไทย"),  # Thai
    ("tr", "Türkçe"),  # Turkish
    # ("tt", "татар теле"),  # Tatar
    # ("udm", "удмурт кыл"),  # Udmurt
    ("uk", "Українська"),  # Ukrainian
    # ("ur", "اردو‏"),  # Urdu
    ("vi", "Tiếng Việt"),  # Vietnamese
    ("zh-hans", "中文(简体)"),  # Simplified Chinese
    ("zh-hant", "中文(香港)"),  # Traditional Chinese
]

# Languages using BiDi (right-to-left) layout
LANGUAGES_BIDI = ["he", "ar", "fa", "ur"]

LOCALE_PATHS = (
    os.path.join(BASE_DIR, "locale"),
)


#restframework settings
REST_FRAMEWORK = {
    "NON_FIELD_ERRORS_KEYS": "errors", #this is what prints out when we send a bad request
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication', #for the restframework tokenauthentication
        'rest_framework_simplejwt.authentication.JWTAuthentication', #third party token auth system, simpleJWT to be exact
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.IsAutheticated', 
    ],
   
}

#simpleJWT setting
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(hours=2),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "SIGNING_KEY": SECRET_KEY,
    "AUTH_HEADER_TYPES": ("Bearer",), #bearer is same as <token>
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
