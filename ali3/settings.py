from pathlib import Path
import os
import cloudinary
import cloudinary.uploader
import cloudinary.api

# المسار الأساسي للمشروع
BASE_DIR = Path(__file__).resolve().parent.parent

# إعداد Cloudinary
cloudinary.config(
    cloud_name='dasaivoam',
    api_key='354892438553333',
    api_secret='BmSGP2539EmN1-D5PWoDvzKHPCs'
)

# إعدادات عامة
SECRET_KEY = 'django-insecure-n&#9f9#w2xgcqy#z5_qv^gd7pf$aai86ji_2+ai#_pf1xls#3*'
DEBUG = True
ALLOWED_HOSTS = []

# التطبيقات المثبتة
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # تطبيقاتك الخاصة
    'store',
    'dashboard',
    'accounts',

    # Cloudinary
    'cloudinary',
    'cloudinary_storage',
]

# الوسيطات (Middleware)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ملفات urls الرئيسية
ROOT_URLCONF = 'ali3.urls'

# إعدادات القوالب
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

# WSGI
WSGI_APPLICATION = 'ali3.wsgi.application'

# قاعدة البيانات
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# التحقق من كلمات المرور
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# إعدادات اللغة والوقت
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# الملفات الثابتة
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Cloudinary للوسائط
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'dasaivoam',
    'API_KEY': '354892438553333',
    'API_SECRET': 'BmSGP2539EmN1-D5PWoDvzKHPCs',
}
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# إعدادات البريد الإلكتروني باستخدام Gmail
# إعدادات البريد الإلكتروني باستخدام Gmail مباشرة
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'mutamieza.op@gmail.com'
EMAIL_HOST_PASSWORD = 'yqzm jokc rfjz qrif'  # ← ضع هنا كلمة مرور التطبيق (App Password) كاملة
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# المفتاح الأساسي الافتراضي
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
