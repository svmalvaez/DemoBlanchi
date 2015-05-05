from django.conf.urls import patterns, include, url
from demo_app import views as  appviews
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Blanchi.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', appviews.index, name="index"),
    url(r'^pedidos/', appviews.pedidos, name="pedidos"),
    url(r'^sign-in/', appviews.sign_in, name="signin"),
)
