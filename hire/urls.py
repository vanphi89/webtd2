from django.conf.urls import url

from .import views

urlpatterns = [
    url(r'^jobs/$', views.jobs, name='jobs'),
    url(r'^locals/(?P<slug>[-\w\d]+)/$', views.locals, name='locals'),
    url(r'^users/$', views.users, name='users'),
    url(r'^users/(?P<slug>[-\w\d]+)-(?P<id>\d+)/$', views.users_detail, name='users_detail'),
    url(r'^jobs/(?P<slug>[-\w\d]+)-(?P<id>\d+)/$', views.detail, name='detail'),
    url(r'^documents/$', views.get_documents, name='get_documents'),
    url(r'^documents/(?P<slug>[-\w\d]+)-(?P<id>\d+)/$', views.get_documents_detail, name='get_documents_detail'),
    url(r'^post/$', views.post, name='post'),
    url(r'^userpost/$', views.userpost, name='userpost'),
    url(r'^thanks/$', views.thanks, name='thanks'),
    url(r'^jobs/search/$', views.search, name= 'search'),
    url(r'^users/search/$', views.searchuser, name= 'searchuser'),
    url(r'^about/$', views.get_the_about, name= 'get_the_about'),
    
   
]