import os
from pathlib import Path

# المسار الرئيسي للمشروع
BASE_DIR = Path(__file__).resolve().parent.parent

# حيلة ذكية لمعرفة اسم المجلد الحالي تلقائياً لتفادي خطأ ModuleNotFoundError
CURRENT_APP_NAME = Path(__file__).resolve().parent.name

# مفتاح الأمان (سكريت كي)
SECRET_KEY = 'django-insecure-your-custom-secret-key-here'

# وضع التطوير
DEBUG = True

# السماح لجميع النطاقات بالدخول للموقع عند الرفع
ALLOWED_HOSTS = ['*']

# التطبيقات المثبتة في المشروع
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'showcase', # تطبيق المعرض والمنتدى
]

# البرمجيات الوسيطة (Middleware)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # مكتبة تشغيل الملفات الثابتة
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# تم ربطها بالمتغير التلقائي لمنع أي خطأ في المسميات
ROOT_URLCONF = f'{CURRENT_APP_NAME}.urls'

# إعدادات القوالب (Templates)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

# تم ربطها بالمتغير التلقائي لمنع أي خطأ في المسميات
WSGI_APPLICATION = f'{CURRENT_APP_NAME}.wsgi.application'


# قاعدة البيانات المحلية (SQLite)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# التحقق من كلمات المرور
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


# إعدادات اللغة والوقت
LANGUAGE_CODE = 'ar' # تحويل لوحة التحكم للغة العربية
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# إعدادات الملفات الثابتة (CSS, JavaScript)
STATIC_URL = '/static/'

# المجلد الذي يجمع فيه Django الملفات الثابتة عند الرفع للسيرفر
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# إعداد WhiteNoise لضغط ملفات الـ CSS والـ JS وتشغيلها بدون مشاكل
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# الحقل الافتراضي للمفاتيح الأساسية في قاعدة البيانات
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'