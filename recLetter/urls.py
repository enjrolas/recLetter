from django.conf.urls import include, patterns, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('letter.views',                       
    url(r'^$', 'home', name='home'),
    url(r'^recondemnation/', 'recondemnation',name='recondemnation'),
    url(r'^recLetter/', 'recLetter', name='recLetter'),
    url(r'^conLetter/', 'conLetter',name='conLetter'),
    url(r'^submit/', 'submit', name='submit'),
)

urlpatterns += patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
