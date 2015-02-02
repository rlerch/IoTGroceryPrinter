from django.conf.urls import patterns, include, url

from django.contrib import admin
from ListManager import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'PiListPrinter.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.list_manager),
    url(r'^print/$', views.print_list),

    url(r'^admin/', include(admin.site.urls)),
)
