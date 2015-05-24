from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from django.http import HttpResponse
from .views import hire_articleSitemap
from django.contrib.sitemaps.views import sitemap
# from django.conf import settings
# from django.conf.urls.static import static
sitemaps = {'hire_article': hire_articleSitemap}

urlpatterns = [
    # Examples:
    url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^$', views.home.as_view(), name='home'),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^hire/', include('hire.urls', namespace="hire")),
    url(r'^about/$', TemplateView.as_view(template_name="home/about.html")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    url(r'^robots\.txts', lambda r: HttpResponse("User-agent: *\nDisallow:", content_type="text/plain"))
]


