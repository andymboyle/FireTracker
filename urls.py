from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^firetracker/$', 'firetracker.fires.views.index'),
    (r'^firetracker/fire/(?P<un_id>[-\w]+)/(?P<address>[-\w]+)/$', 'firetracker.fires.views.fire'),
    (r'^firetracker/person/(?P<un_id>[-\w]+)/(?P<slug>[-\w]+)/$', 'firetracker.fires.views.person'),
    (r'^firetracker/admin/', include(admin.site.urls)),
)