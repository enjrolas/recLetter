import os
import sys

path = '/home/japhy/recLetter/'

if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'recLetter.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()