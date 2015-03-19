from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
admin.autodiscover()
from django.contrib.auth.models import User, Group
from django.http import Http404, HttpResponse

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'KA_django.apps.KA_app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
