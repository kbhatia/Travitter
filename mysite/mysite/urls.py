from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

#urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
#)

from django.conf.urls import patterns, url
from travels import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'', include('social_auth.urls')),
)
        
