from .base import *
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('DJANGO_SECRET_KEY', default='n!$^cr6d3u6cm$)c901(ms8gk4ojxct4aj-pk5_7u74i7jkivp')
DEBUG = True