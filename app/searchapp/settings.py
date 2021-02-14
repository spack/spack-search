__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021, Vanessa Sochat"
__license__ = "Apache-2.0 OR MIT"

from django.core.management.utils import get_random_secret_key
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# The term to highlight, etc.
SEARCH_TERM = "dlopen"

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/


def generate_secret_keys(filename):
    """A helper function to write a randomly generated secret key to file"""
    key = get_random_secret_key()
    with open(filename, "w") as fd:
        fd.writelines("SECRET_KEY = '%s'\n" % key)


# Generate secret keys if do not exist, and not defined in environment
SECRET_KEY = os.environ.get("SECRET_KEY")

if not SECRET_KEY:
    try:
        from .secret_key import SECRET_KEY
    except ImportError:
        SETTINGS_DIR = os.path.abspath(os.path.dirname(__file__))
        generate_secret_keys(os.path.join(SETTINGS_DIR, "secret_key.py"))
        from .secret_key import SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "searchapp.apps.source",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "haystack",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "searchapp.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "searchapp.wsgi.application"


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": "postgres",
        "NAME": "postgres",
        "USER": "postgres",
        "PASSWORD": "postgres",
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = []


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = "static"

HAYSTACK_CONNECTIONS = {
    "default": {
        "ENGINE": "haystack.backends.elasticsearch2_backend.Elasticsearch2SearchEngine",
        "URL": "http://elasticsearch:9200/",
        "INDEX_NAME": "haystack",
    },
}

HAYSTACK_SEARCH_RESULTS_PER_PAGE = 25

# Update Search index in realtime (using models.db.signals)
HAYSTACK_SIGNAL_PROCESSOR = "haystack.signals.RealtimeSignalProcessor"
