from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'letter.views.home'),
    url(r'^recommendation/', 'letter.views.recommendation'),
    url(r'^recondemnation/', 'letter.views.recondemnation'),
    url(r'^recLetter/', 'letter.views.recLetter'),
    url(r'^conLetter/', 'letter.views.conLetter'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
