"""
Import a local configuration file (not in version control) which will pull in
dev or prod settings and add private details.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "website.settings.local")

application = get_wsgi_application()
