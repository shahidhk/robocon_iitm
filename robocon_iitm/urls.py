from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^robocon_iitm/', include('robocon_iitm.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^$', 'robocon_iitm.views.home', name='home'),
    url(r'^blur$', 'robocon_iitm.views.blur', name='blur'),
    url(r'^template$', 'robocon_iitm.views.template', name='template'),
    url(r'^blog$', 'robocon_iitm.views.blog', name='blog'),

)
