from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.http import FileResponse, Http404
import os
def frontend(request):
 if os.environ.get('SERVE_FRONTEND') != '1': raise Http404()
 return FileResponse(open(settings.BASE_DIR / 'frontend_dist' / 'index.html','rb'),content_type='text/html')
urlpatterns = [path('admin/', admin.site.urls), path('api/', include('core.urls')), re_path(r'^(?!api/|admin/|static/).*$', frontend)]
