from django.shortcuts import render
from hire.models import hire_article, localwork
from hire.forms import searchform
from django.views import generic
from django.views.generic.list import ListView
from django.contrib.sitemaps import Sitemap
from hire.models import hire_article


def home(request):
    hire_article_list = hire_article.objects.order_by('-id')[:50]
    form = searchform()
    list_city1=localwork.objects.all()[:20]
    list_city2=localwork.objects.all()[20:40]
    list_city3=localwork.objects.all()[40:60]
    context = {'hire_article_list': hire_article_list, 'form':form, 'list_city1':list_city1, 'list_city2':list_city2, 'list_city3':list_city3 }
    return render(request, 'home/home.html', context)
# class home(ListView):
#     template_name = 'home/home.html'
#     context_object_name = 'hire_article_list'
# 
#     def get_queryset(self):
#         """Return the last five published questions."""
#         return hire_article.objects.order_by('-id')[:10]
#


#FOR SITEMAP

class hire_articleSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5
    

    def items(self):
        return hire_article.objects.all()

    def lastmod(self, obj):
        return obj.publication_date
    def location(self, obj):
        return '/'