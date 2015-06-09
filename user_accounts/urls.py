from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'onepass.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^home/$', views.home , name="home"),
    url(r'^logout/$', views.logout_view , name="logout"),
    url(r'^login/$', views.login_view , name="login"),
    url(r'^user_details/$', views.GetUserDetail.as_view(), name = 'user_details'),
    url(r'^user_auth/$', views.AuthView.as_view(), name = 'user_auth'),
    url(r'^user_name/$', views.GetUserDetail.as_view(), name = 'user_details'),


)
