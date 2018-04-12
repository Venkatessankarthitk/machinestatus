from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^searchdata/$', 'searchdata.views.index'),
    url(r'^searchdata1/$', 'searchdata.views.index1'),
    url(r'^search_quarantine/$', 'searchdata.views.search_quarantine'),
    url(r'^unquarantine_factory/$', 'searchdata.views.unquarantine_factory'),
    url(r'^machines/$', 'searchdata.views.machines'),
    url(r'^start_assimilate/$','searchdata.views.start_assimilate' ),
    url(r'^assmililate_running/$','searchdata.views.assimilate_running_status'),
    url(r'^assmililate_status_json/$','searchdata.views.assimilate_status_json'),
    # url(r'^tintri/', include('tintri.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
