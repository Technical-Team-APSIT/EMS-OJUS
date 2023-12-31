"""
WSGI config for EMS project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os, sys
# add the hellodjango project path into the sys.path
sys.path.append('/home/meetjamsutkar645_apsit_edu_in/EMS')

# add the virtualenv site-packages path to the sys.path
sys.path.append('/home/meetjamsutkar645_apsit_edu_in/EMS')


from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EMS.settings.prod')

application = get_wsgi_application()
