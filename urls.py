from django.conf.urls.defaults import *
from firetracker.fires.views import index, fire, person

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(
        regex   = r'^firetracker/$',
        view    = index,
        kwargs  = {},
        name    = 'firetracker_index',
    ),
    url(
        regex   = r'^firetracker/fire/(?P<un_id>[-\w]+)/(?P<address>[-\w]+)/$',
        view    = fire,
        kwargs  = {},
        name    = 'firetracker_fire_detail',
    ),
    url(
        regex   = r'^firetracker/person/(?P<un_id>[-\w]+)/(?P<slug>[-\w]+)/$',
        view    = person,
        kwargs  = {},
        name    = 'firetracker_person_detail',
    ),
    
    #admin
    url(r'^firetracker/admin/', include(admin.site.urls)),
)
