Travitter
=========

Twitter App for finding all travel related Content

Settings Specific for Social Auth - 

Add the following settings to Settings.py


AUTHENTICATION_BACKENDS = (
    'social_auth.backends.twitter.TwitterBackend',
    'django.contrib.auth.backends.ModelBackend',
)


TWITT_CONFIG = None
with open((os.path.join(BASE_DIR,"travels","config.json")),"r") as text:
	TWITT_CONFIG = json.load(text)
	
TWITTER_CONSUMER_KEY         = TWITT_CONFIG['TWITTER_CONSUMER_KEY']
TWITTER_CONSUMER_SECRET      = TWITT_CONFIG['TWITTER_CONSUMER_SECRET']

LOGIN_URL = '/login/'

INSTALLED_APPS = (
    …,
    'social_auth',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'social_auth.context_processors.social_auth_by_type_backends',
    'django.contrib.auth.context_processors.auth',
)

SOCIAL_AUTH_ENABLED_BACKENDS = ('twitter', ...)
SOCIAL_AUTH_DEFAULT_USERNAME = 'new_social_auth_user'


Prototype project for making Twitter a most effictive tool for traveling purposes. 
Later to be developed into a mobile app 

