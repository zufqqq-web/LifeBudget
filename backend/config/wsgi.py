import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE','config.settings')
application = get_wsgi_application()
if os.environ.get('SERVE_FRONTEND') == '1':
 from whitenoise import WhiteNoise
 from django.conf import settings
 application = WhiteNoise(application, root=str(settings.BASE_DIR / 'frontend_dist'))
