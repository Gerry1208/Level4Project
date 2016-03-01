from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from tastypie.api import Api
from names.api import cardResource, groupResource, pictureResource, bulkResource

names_api = Api(api_name="name")

names_api.register(cardResource())
names_api.register(groupResource())
names_api.register(pictureResource())
names_api.register(bulkResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^names/', include('names.urls')),
    url(r'^api/', include(names_api.urls)),

)

if settings.DEBUG:
    urlpatterns += patterns('django.views.static',
                            (r'^media/(?P<path>.*)',
                           'serve',
                            {'document_root': settings.MEDIA_ROOT}),)
