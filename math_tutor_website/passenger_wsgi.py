# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/home/n/nikol2hr/nikol2hr.beget.tech/HelloDjango')
sys.path.insert(1, '/home/n/nikol2hr/nikol2hr.beget.tech/djangoenv/lib/python3.11/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'HelloDjango.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
