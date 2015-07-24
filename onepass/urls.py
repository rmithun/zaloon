from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from user_accounts import views as uac_view

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'onepass.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^account/', include("user_accounts.urls")),
    url(r'^studios/', include("studios.urls")),
    url(r'^booking/', include("booking.urls")),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^$', TemplateView.as_view(template_name='user_accounts/index.html'), name="home"),
    url(r'^register/(?P<backend>[^/]+)/$',
        uac_view.register_by_access_token),
    url(r'^home/$',TemplateView.as_view(template_name='user_accounts/home.html'),name = 'home'),
    url(r'^iframe/$',TemplateView.as_view(template_name='user_accounts/iframe.html'),name = 'iframe'),

    url(r'^search/$',TemplateView.as_view(template_name='user_accounts/search.html'),name = 'search'),
    



)
