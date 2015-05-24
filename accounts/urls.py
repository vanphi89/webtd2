from django.conf.urls import url

from .import views

urlpatterns = [
    url(r'^$', views.view_account, name='view_account'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^password_change/$',views.password_change, name='password_change'),
    
    url(r'^password_reset/$', views.password_reset, name='password_reset'),
    url(r'^password_reset_done/$', views.password_reset_done, name='password_reset_done'),
    url(r'^password_reset_confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^password_reset_complete/$', views.password_reset_complete, name='password_reset_complete'),
]