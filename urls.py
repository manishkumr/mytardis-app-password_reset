from django.conf.urls import patterns, url
from django.contrib.auth import views as auth_views

from . import views


# Password reset
urlpatterns = [
    url(r'^$', views.admin_password_reset,
        {'template_name': 'registration/tardis_password_reset_form.html',
         'email_template_name': 'registration/tardis_password_reset_email.txt'},
        name='password_reset'),
    url(r'^done/$', auth_views.password_reset_done,
        {'template_name': 'registration/tardis_password_reset_sent.html'},
        name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm,
        {'template_name': 'registration/tardis_password_reset_confirm.html'},
        name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete,
        {'template_name': 'registration/tardis_password_reset_complete.html'},
        name='password_reset_complete'),
]
