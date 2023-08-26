# coolsite/settings/development.py

# import everything from base.py
from .base import *

# overwrite necessary items

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# since DEBUG is False ALLOWED_HOSTS is compulsory
# add correct hostname i.e. website name
ALLOWED_HOSTS = ['*']

# Database : Add production database details here
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'cookiejar.db'),
    }
}
