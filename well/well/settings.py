"""
Django settings for well project.

Generated by 'django-admin startproject' using Django 5.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-s=x3w0dyptw#r)_vjt*bj(947n_wd^_mu3@3jce3d#au&!w&w="

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    # "jazzmin",
    "pages.apps.PagesConfig",
    "addon.apps.AddonConfig",
    "resort.apps.ResortConfig",
    "user_dashboard.apps.UserDashboardConfig",
    "userauths.apps.UserauthsConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "pages.booking_functions",
    'crispy_forms',
    'django_countries',
    'ckeditor_uploader',
    'django_ckeditor_5',
    'import_export',
    'mathfilters',
    'taggit',
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

ROOT_URLCONF = "well.urls"
CRISPY_TEMPLATE_PACK ='bootstrap4'

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = "well.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "project5",
        "USER": "root",
        "PASSWORD": "00000",
        "HOST": "localhost",
        "PORT": "3306",
    }
}


# DATABASES = {
#     "default": {
#         "ENGINE": 'django.db.backends.mysql',
#         "NAME": "project2",
#         "USER": "root",
#         "PASSWORD": "00000",
#         "HOST": "127.0.0.1",
#         "PORT": "3306",
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = "/static/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, "well/static")]
# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
AUTH_USER_MODEL = "userauths.User"

MEDIA_ROOT = os.path.join(BASE_DIR, "well/media")
MEDIA_URL = "/media/"


LOGIN_REDIRECT_URL = '/pages'
LOGOUT_REDIRECT_URL = '/pages'





# JAZZMIN_SETTINGS = {
#     "site_header": "EG-MedT",
#     "site_brand": "EG-MedT" ,
#     "site_logo": "images/logooo.png",
#     "login_logo": None,
#     "login_logo_dark": None,
#     "site_logo_classes": "img-circle",
#     "site_icon": None,
#     "welcome_sign": "Welcome to the EG-MedT",
#     "copyright": "All Right Reserved 2024 EG-MedT",
#     "search_model": ["auth.User", "auth.Group"],
#     "user_avatar": None,

#     ############
#     # Top Menu #
#     ############

#     # Links to put along the top menu
#     "topmenu_links": [

#         # Url that gets reversed (Permissions can be added)
#         {"name": "Home",  "url": "admin:index", "permissions": ["auth.view_user"]},

#         # external url that opens in a new window (Permissions can be added)
#         {"name": "Company", "url": "/admin/addons/company/"},
#         {"name": "Users", "url": "/admin/userauths/user/"},

#         # model admin to link to (Permissions checked against model)
#         {"model": "AUTH_USER_MODEL.User"},
#     ],
# "order_with_respect_to":[
#     "resort",
#     "resort.Hotel",
#     "resort.Room",
#     "resort.Booking",
#     "resort.BookingDetail",
#     "resort.Guest",
#     "resort.RoomServices",
#     "userauths",
#     "addons",
# ],

# "icons":{
#     "auth" : "fas fa-users-cog",
#     "auth.user": "fas fa-user",
#     "admin.LogEntry" : "fas fa-file",
#     "userauths.User" :"fas fa-user",
#     "userauths.Profile" : "fas fa-address-card",
#     "resort.Hotel": "fas fa-th",
#     "resort.Booking" : "fas fa-calendar-week",
#     "resort.BookingDetail" : "fas fa-calendar-alt",
#     "resort.Guest" : "fas fa-user",
#     "resort.Room" : "fas fa-bed",
#     "resort.RoomServices" : "fas fa-user-cog",
#     "resort.Notification" : "fas fa-bell",
#     "resort.Coupon" : "fas fa-tag",
#     "resort.Bookmark" : "fas fa-heart",
# },

# "show_ui_builder" : True
# }
# JAZZMIN_UI_TWEAKS = {
#     "navbar_small_text" : False,
#     "footer_small_text" :False,
#     "body_small_text" : True,
#     "brand_small_text" : False,
#     "brand_color" : "navbar-indigo",
#     "accent" : "accent-olive",
#     "navbar" : "navbar_indigo navbar-dark",
#     "no_navbar_border" : False,
#     "navbar_fixed" : False,
#     "layout_boxed" :False,
#     "footer_fixed" : False,
#     "sidebar_fixed" : False,
#     "sidebar" : "sidebar-dark-indigo",
#     "sidebar_nav_small_text" : False,
#     "sidebar_disable_expand" :False,
#     "sidebar_nav_child_indent" : False,
#     "sidebar_nav_compact_style" : False,
#     "sidebar_nav_legacy_style" :False,
#     "sidebar_nav_flat_style" :False,
#     "theme" : "cyborg",
#     "dark_mode_theme" : "cyborg",
#     "button_classes" : {
#         "primary" : "btn-primary",
#         "secondary" : "btn-secondary",
#         "info" : "btn-info",
#         "warning" : "btn-warning",
#         "danger" : "btn-danger",
#         "success" : "btn-success"
#     }
# }
