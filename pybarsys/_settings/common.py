"""
Django settings for pybarsys project.

Generated by 'django-admin startproject' using Django 1.10.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__ + "/..")))

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'bootstrap3',
    'barsys.apps.BarsysConfig',
    'django_filters',
    'crispy_forms',
]

STATIC_URL = '/static/'

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

ROOT_URLCONF = 'pybarsys.urls'
LOGIN_REDIRECT_URL = 'user_home'

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

WSGI_APPLICATION = 'pybarsys.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

AUTH_USER_MODEL = 'barsys.User'  # custom Barsys user model

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Berlin'

USE_I18N = True

USE_L10N = True

USE_TZ = True

CRISPY_TEMPLATE_PACK = 'bootstrap3'

BOOTSTRAP3 = {
    # The URL to the jQuery JavaScript file
    'jquery_url': '/static/barsys/jquery/jquery.min.js',

    # The Bootstrap base URL
    'base_url': '/static/barsys/bootstrap-3.3.7-dist/',

    # The complete URL to the Bootstrap CSS file (None means no theme)
    'theme_url': '/static/barsys/bootstrap-3.3.7-dist/css/bootstrap-theme.css',

}

from decimal import Decimal


class PybarsysPreferences:
    """ Default preferences of pybarsys
        They can be overridden in your production or dev settings file.
    """

    class EMAIL:
        # subfolder in barsys/templates
        TEMPLATE_DIR = 'email'

        # Subject of an invoice mail
        INVOICE_SUBJECT = 'Invoice from Barsys bar'

        # Subject of a purchase notification to dependants
        PURCHASE_NOTIFICATION_SUBJECT = 'Purchase notification from Barsys bar'

        # Subject of a payment reminder mail
        PAYMENT_REMINDER_SUBJECT = 'Payment reminder from Barsys bar'

        # Bar contact email address
        CONTACT_EMAIL = "bar@example.com"

        # Name of bar in default templates
        NAME_OF_BAR = "Barsys bar"

        BANK_ACCOUNT_RECIPIENT = "Barsys bar"
        BANK_ACCOUNT_NUMBER = "55542"
        BANK_ACCOUNT_ROUTING_NUMBER = "2718"
        BANK_ACCOUNT_BANK = "Royal Bank of Moldova"
        # (Display name of the invoice recipient is always appended to payment reference)
        BANK_ACCOUNT_PAYMENT_REFERENCE = "Bar debts"


    class Misc:
        # Number of purchases to show on user history page
        NUM_USER_PURCHASE_HISTORY = 15
        # Whether to show total cost of unbilled purchases on user history page
        SUM_COST_USER_PURCHASE_HISTORY = True
        # User should transfer money if balance is below this value
        BALANCE_BELOW_TRANSFER_MONEY = Decimal('0')
        # Number of purchases to show on main page
        NUM_MAIN_LAST_PURCHASES = 5
        # Number of users to show in a StatsDisplay on main page
        NUM_MAIN_USERS_IN_STATSDISPLAY = 5
