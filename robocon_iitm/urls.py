# From django
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# From settings
import settings

# From python
import os.path

# For DajaxIce to work
from misc.dajaxice.core import dajaxice_autodiscover, dajaxice_config
dajaxice_autodiscover()

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
    
    url(r'^$', 'misc.views.home', name='home'),
    url(r'^blur$', 'misc.views.blur', name='blur'),
    url(r'^template$', 'misc.views.template', name='template'),
    
    url(r'^blog/new$', 'blog.views.newblog', name='newblog'),
    url(r'^blog$', 'blog.views.blog', name='blog'),
    url(r'^blog/(\d+)$', 'blog.views.blogpost', name='blogpost'),

    (r'^comments', include('django.contrib.comments.urls')),

    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}), # for media urls
                 
    url(dajaxice_config.dajaxice_url, include('misc.dajaxice.urls')), # For dajaxice to function corrently
)

urlpatterns += staticfiles_urlpatterns() # To enable serving static files
