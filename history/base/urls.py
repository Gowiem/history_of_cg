from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'base.views.home', name='home'),
    # url(r'^base/', include('base.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'historyofcg.views.home'),
    url(r'^about/$', 'historyofcg.views.about'),
    url(r'^accounts/', include('registration.backends.default.urls')),

    url(r'^pages/(?P<s>[-\w]+)/$', 'historyofcg.views.view_source_entries'),
    url(r'^add/page/$', 'historyofcg.views.add_page', name="add_page"),
    url(r'^edit/page/(?P<vanity_url>[-\w]+)/$', 'historyofcg.views.edit_page'),
    url(r'^unpublish/page/(?P<vanity_url>[-\w]+)/$', 'historyofcg.views.unpublish_page'),
    url(r'^publish/page/(?P<vanity_url>[-\w]+)/$', 'historyofcg.views.publish_page'),

    url(r'^edit/story/(?P<type>[-\w]+)/(?P<id>\d+)/$', 'historyofcg.views.edit_story'),
    url(r'^publish/story/(?P<id>\d+)/$', 'historyofcg.views.publish_story'),
    url(r'^unpublish/story/(?P<id>\d+)/$', 'historyofcg.views.unpublish_story'),
    url(r'^save/story/(?P<story_type>[-\w]+)/(?P<vanity_url>[-\w]+)/$', 'historyofcg.views.new_story'),
    url(r'^delete/story/(?P<id>\d+)/$', 'historyofcg.views.delete_story'),
    url(r'^vote/up/(?P<story_id>\d+)/$', 'historyofcg.views.up_vote_story'),
    url(r'^vote/down/(?P<story_id>\d+)/$', 'historyofcg.views.down_vote_story'),
    url(r'^vote/none/(?P<story_id>\d+)/$', 'historyofcg.views.no_vote_story'),

    url(r'^tags/(?P<app_label>[-\w]+)/(?P<model>[-\w]+)$', "historyofcg.views.search", name="djtokeninput_search"),
    url(r'^get/pages/$', 'historyofcg.views.get_pages', name='get_pages'),

    url(r'^add/connection/(?P<connect_to>[-\w]+)/(?P<to_connect>[-\w]+)/$', 'historyofcg.views.add_connection', name='add_connection'),
    url(r'^remove/connection/(?P<remove_to>[-\w]+)/(?P<to_remove>[-\w]+)/$', 'historyofcg.views.remove_connection', name='remove_connection'),

    url(r'^user/(?P<i>\d+)/$', 'historyofcg.views.user_page')
)

urlpatterns += staticfiles_urlpatterns()