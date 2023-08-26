# 'production.py' will be selected for online-server
# since 'local.py' is in gitigonre

# select 'development' or 'production' server
try:
    from .development import *
except:
    from .production import *
