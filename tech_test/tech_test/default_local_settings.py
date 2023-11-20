DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'tech_test_db',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

SITE_ID = 1

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''


LOGIN_REDIRECT_URL = '/google-auth/'
LOGOUT_REDIRECT_URL = '/google-auth/'

# Facebook configuration
SOCIAL_AUTH_FACEBOOK_KEY = '685852533437489'
SOCIAL_AUTH_FACEBOOK_SECRET = '20c79907ba89671738042daf6acbe242'

SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    'fields': 'id, name, email'
}