

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', "soccer.views.homeClube"),
    (r'^jogadores/$', "soccer.views.homeJogador"),
    (r'^novo-clube/$', "soccer.views.adicionaClube"),
    (r'^clube/(?P<nr_clube>\d+)/$', "soccer.views.infoClube"),
    (r'^novo-jogador/$', "soccer.views.adicionaJogador"),
    # Examples:
    # url(r'^$', 'ff.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
                (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                 {'document_root': settings.MEDIA_ROOT}),
    )
