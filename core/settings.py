"""
Copyright (c) 2015 - present Sdata.ir
"""

from pathlib import Path, os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# ------------------------- Configs -------------------------
# ------------------------------------------------------------
SECRET_KEY = os.getenv('SECRET_KEY', 'full_amniat')
DEBUG = os.getenv('DEBUG', True)
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

CSRF_TRUSTED_ORIGINS = []

ROOT_URLCONF = "core.urls"


# ----------------- Applications -----------------
# ------------------------------------------------
DEFAULT_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
]

LOCAL_APPS = [
    'main',
    'accounts',
    'demo',
]

THIRD_PARTY_APPS = [
    'jalali_date',
    'admin_interface',
    'colorfield',
]

INSTALLED_APPS = THIRD_PARTY_APPS + LOCAL_APPS + DEFAULT_APPS


# ----------------- Middlewares ------------------
# ------------------------------------------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",

    # Admin Access 
    'accounts.middlewares.AdminUserMiddleWare',
    # /Admin Access
]


# ----------------- Templates -------------------
# -----------------------------------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
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

WSGI_APPLICATION = "core.wsgi.application"


# ------------------------- DATABASE -------------------------
# ------------------------------------------------------------
if os.getenv('DB_ENGINE', 'DB_ENGINE is not set.') == 'sqlite3' and os.getenv('DEBUG'):
    DATABASES = {
        'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
        } 
}


# ------------------ Password validation ---------------------
# ------------------------------------------------------------
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


# ---------------------- Internationalization ----------------------
# ------------------------------------------------------------------
LANGUAGE_CODE = "fa-ir"
TIME_ZONE = "Asia/Tehran"
USE_I18N = True
USE_TZ = True


# ------------------------- STATIC -------------------------
# ------------------------------------------------------------
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "core/static_files"),
]


# ------------------------- MEDIA -------------------------
# ------------------------------------------------------------
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# ------------------- Other Configs --------------------
# ------------------------------------------------------
from django.contrib.messages import constants as messages

AUTH_USER_MODEL = 'accounts.User'

X_FRAME_OPTIONS = 'same-origin'

MESSAGE_TAGS = {
    messages.DEBUG: 'info',
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'danger',
}

# LOGIN_URL = reverse_lazy('accounts:login')
LOGOUT_REDIRECT_URL = '/'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

# ckeditor
CKEDITOR_UPLOAD_PATH = "ckeditor/uploads/"
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
    },
}
# /ckeditor

DEFAULT_PAGINATE_NUMBER = 10


# ------------------------- EMAIL -------------------------
# ------------------------------------------------------------
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_PORT = os.getenv('EMAIL_PORT', '')
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS')
DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL')


# ------------------------- REXAN API CONFIGS ----------------
# ------------------------------------------------------------
RESERVATION_API_BASE_URL = os.getenv('API_BASE_URL', 'https://rexan.megagasht.ir')
RESERVATION_API_KEY = os.getenv('RESERVATION_API_KEY', 'testapikey')


# ------------------- SECURITY CONFIGS -------------------
# --------------------------------------------------------
if not bool(DEBUG):
    # security.W016
    CSRF_COOKIE_SECURE = True

    # security.W012
    SESSION_COOKIE_SECURE = True


    # security.W004
    SECURE_HSTS_SECONDS = 31536000 # One year in seconds


    # Another security settings
    # SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    # SECURE_HSTS_PRELOAD = True
    # SECURE_CONTENT_TYPE_NOSNIFF = True
