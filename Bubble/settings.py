#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Bubble Copyright © 2017 Il'ya Semyonov
# License: https://www.gnu.org/licenses/gpl-3.0.en.html
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/'

SECRET_KEY = 'zph8*z8s%8jva0k*6y7i*2i&2@kv$3%0^m9ahntdxr@+_je$om'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bubble',
        'USER': 'root',
        'PASSWORD': 'BubbleLocalHost',
        'HOST': 'localhost',
        'PORT': '3306'
    }
}


PAYMENT = {
    'aggregator': 'free-kassa',
    'publicKey': '50552',
    'secretKey': 't03dnpt2',
    'secretKey2': 'd2uykhf7'    # only for free-kassa
}


BUBBLE = {
    'siteName': 'Bubble',
    'serverIP': 'BUBBLE.LOCALHOST',
    'description': 'Donation system written with Django',
    'descriptionOfPurchase': 'Покупка %s для %s на %s'  # account, item, siteName
}

DEBUG = True

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '[::1]'
]


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'basic',
    'unitpay'
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


ROOT_URLCONF = 'Bubble.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR + 'templates',
            BASE_DIR + 'basic/templates',
            BASE_DIR + PAYMENT['aggregator'] + '/templates'
        ],
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


WSGI_APPLICATION = 'Bubble.wsgi.application'


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


LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    BASE_DIR + 'static/',
]
