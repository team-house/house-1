# coding: utf-8

import os
import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SECRET_KEY = 'q8@+pm33!e*!5zisvxx_k+^-p1byx0aaypj&^6_gwwefm*90x&'

DEBUG = True

ALLOWED_HOSTS = []


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'guardian',
    'web',
    'website',
    'wechatapi'
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'house.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'frontend', 'dist')],
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


WSGI_APPLICATION = 'house.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'house',
        'USER': 'root',
        'PASSWORD': 'yijia',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {'charset': 'utf8mb4'},
    }
}

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'guardian.backends.ObjectPermissionBackend',
    # 'web.auth_backends.mobile.MobileBackend',
)


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

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
        # 'rest_framework.permissions.AllowAny',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'rest_framework.authentication.SessionAuthentication',
        # 'rest_framework.authentication.BasicAuthentication',
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
}

JWT_AUTH = {
    'JWT_ENCODE_HANDLER': 'rest_framework_jwt.utils.jwt_encode_handler',
    'JWT_DECODE_HANDLER': 'rest_framework_jwt.utils.jwt_decode_handler',
    'JWT_PAYLOAD_HANDLER': 'rest_framework_jwt.utils.jwt_payload_handler',
    'JWT_PAYLOAD_GET_USER_ID_HANDLER': 'rest_framework_jwt.utils.jwt_get_user_id_from_payload_handler',
    'JWT_RESPONSE_PAYLOAD_HANDLER': 'rest_framework_jwt.utils.jwt_response_payload_handler',
    'JWT_SECRET_KEY': SECRET_KEY,
    'JWT_ALGORITHM': 'HS256',
    'JWT_VERIFY': True,
    'JWT_VERIFY_EXPIRATION': True,
    'JWT_LEEWAY': 0,
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=30),
    'JWT_AUDIENCE': None,
    'JWT_ISSUER': None,
    'JWT_ALLOW_REFRESH': False,
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=60),
    'JWT_AUTH_HEADER_PREFIX': 'JWT',
}


LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

BACK_PAGE_COUNT = 15

# 后台提醒
FILED_CHECK_MSG = '<b class="error_msg">字段不能为空</b>'

# 过滤不可添加的父级栏目
COLUMN_NOT_LIST = [
    # {'id': 1, 'name': '内容服务'},
]
# 是否可以创建父栏目
COLUMN_IS_ADD = True
COLUMN_IS_EDIT = True

# redis
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 0
REDIS_TIMEOUT = 7*24*60*60

# 加密前缀
DB_PREFIX = 'house_'


# 微信
WECHAT_APP_ID = 'wx80d7ef667ec4ee53'
WECHAT_APP_SECRET = '6389d5eb5637a2241d10914e010c8641'

# 云通讯
SMS_ACCOUNT_SID = '8aaf07085d106c7f015d4660f8c015cb'
SMS_ACCOUNT_TOKEN = 'e91031fce3f948efb7549308d709ba19'
SMS_SUB_ACCOUNT_SID = '8aaf07085d106c7f015d4660faa615d1'
SMS_SUB_ACCOUNT_TOKEN = 'a48f2a39778715aa270e5028f5843cba'
SMS_APP_ID = '8aaf07085d106c7f015d4660faa615d1'
SMS_TEMPLATE_CODE_ID = 236748
SMS_TEMPLATE_CODE_RESET = 236749
SMS_TEMPLATE_CODE_H5 = 243758

# 云通讯
# SMS_ACCOUNT_SID = '8a216da85b602cda015b6650215a044a'
# SMS_ACCOUNT_TOKEN = 'a8a50ceb783c4611896c5b8a165bdbea'
# SMS_SUB_ACCOUNT_SID = 'a1eb8b67976611e69b876c92bf2c142d'
# SMS_SUB_ACCOUNT_TOKEN = 'c2c7a073d888513461a4f7439f110951'
# SMS_APP_ID = '8a216da85b602cda015b6650235e0450'
# # 验证码模板
# SMS_TEMPLATE_CODE_ID = 178808

# qiniu
QINIU_DOMAIN = 'oxaoo4ur4.bkt.clouddn.com'
QINIU_ACCESS_KEY = 'uUpyGla7DTbzVG7BKjgMlsT8QEx0RsFuY8ofxY7r'
QINIU_SECRET_KEY = 'J0FdHNr6i1PdwlVzoxs-sqR5IeJgqjTFmqbWubuC'
BUCKET_NAME = 'yueju'

# ping++
API_KEY = 'sk_live_DKyPiDvnn1qTeDyzPK98W1e5'
APP_ID = 'app_SOGGKKPaLafDq1aH'

# QQ地图

QQ_MAP_API_URL = 'https://map.qq.com/api/js?v=2.exp&libraries=drawing,geometry,autocomplete,convertor'


# 跨域增加忽略
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = (
    '*',
)

CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
    'VIEW',
)

CORS_ALLOW_HEADERS = (
    'XMLHttpRequest',
    'X_FILENAME',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'Pragma',
)

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'frontend/dist/static'),
]

UPLOAD_DIR = os.path.join(BASE_DIR, 'static', 'upload')

MEDIA_URL = '/media/'
MEDIA_ROOT = UPLOAD_DIR

DOMAIN = 'http://www.yuejuweb.com'

# setting_local
ROOT = os.path.abspath(os.path.dirname(__file__))
if os.path.exists(os.path.join(ROOT, 'settings_local.py')):
    execfile(os.path.join(ROOT, 'settings_local.py'))

