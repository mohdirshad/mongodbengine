from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'blog.views.post_view', name='home'),
     url(r'createpost/$', 'blog.views.create_post', name='post'),
     url(r'createcomment/(?P<id>\w+)/$', 'blog.views.create_comment', name='comment'),
     url(r'detail/(?P<id>\w+)/$', 'blog.views.detail', name='detail'),
    # url(r'^mongoproject/', include('mongoproject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'$', include('blog.urls')),
)
