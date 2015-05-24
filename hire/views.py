from accounts.models import UserProfile
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, RequestContext
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import postform, searchform, userpostform, searchformuser
from accounts.forms import UserForm, UserProfileForm
from django import template
from .models import hire_article, the_documents, userpostt, the_about, localwork
from django.views.generic import ListView, DetailView #for pagination old: from django.views.generic.list_detail import object_list 
# from .forms import PropertyFilter #for search view


@login_required(login_url='/accounts/login/')
def post(request):
    # a=request.user
    # b=UserProfile.objects.get(id=a.id)
    # hire_article.objects.all().update(whopost=b)     
    if request.method == 'POST':
        form = postform(request.POST)
        
        if form.is_valid():
            
            form.save(commit=True)
            return HttpResponseRedirect('/hire/thanks/')
        else:
            print (form.errors)
            # return render(request, '/accounts/login.html', {'notlogin': True})

    
    else:
        form = postform()

    return render(request, 'companys/post.html', {'form': form})

@login_required(login_url='/accounts/login/')
def userpost(request):
    if request.method == 'POST':
        form = userpostform(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/hire/thanks/')
        else:
            print (form.errors)
            # return render(request, '/accounts/login.html', {'notlogin': True})

    
    else:
        form = userpostform()

    return render(request, 'users/userpost.html', {'form': form})
@login_required(login_url='/accounts/login/')
def thanks(request):
     return render(request, 'thanks/jobs_thank.html')
 
def jobs(request):
     
    hire_article_list = hire_article.objects.all().order_by('-id')[0:500]
    paginator = Paginator(hire_article_list, 50) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        hire_article_s = paginator.page(page)
        
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        hire_article_s = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        
        hire_article_s = paginator.page(paginator.num_pages)
        
    #return render_to_response('hire/list.html', {"page_list": page_list})
    form = searchform()
    context = {'hire_article_s': hire_article_s, 'form':form}
    return render(request, 'companys/list.html', context)


def users(request):
    
    userlist = userpostt.objects.all().order_by('-id')[0:500]
    paginator = Paginator(userlist, 50) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        userlist_s = paginator.page(page)
        
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        userlist_s = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        
        userlist_s = paginator.page(paginator.num_pages)
        
    #return render_to_response('hire/list.html', {"page_list": page_list})
    form = searchformuser()
    context = {'userlist_s': userlist_s, 'form':form}
    return render(request, 'users/userpostlist.html', context)



def locals(request, slug):
    
    hire_article_list = hire_article.objects.filter(localwork__slug=slug).order_by('-id')[:500]
    
    # locals_list=localwork.objects.all()
    
    # return render_to_response('companys/detail.html', {'hire_article': p, 'form':form})


    paginator = Paginator(hire_article_list, 50) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        hire_article_s = paginator.page(page)
        
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        hire_article_s = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        
        hire_article_s = paginator.page(paginator.num_pages)
        
    #return render_to_response('hire/list.html', {"page_list": page_list})
    # p = get_object_or_404(hire_article,slug=slug)
    
    form = searchform()
    context = {'hire_article_s': hire_article_s, 'form':form}
    return render(request, 'localslist/localslist.html', context)
    
    
    
    
def search(request):
    if request.method == 'GET':
        form = searchform(request.GET)  
        if form.is_valid():
            category = form.cleaned_data['category']
            localwork = form.cleaned_data['localwork']
            
            results = hire_article.objects.filter(category = category).filter(localwork= localwork).order_by('-id')[:500]
            paginator = Paginator(results, 50)
            page = request.GET.get('page')
            try:
                hire_article_s = paginator.page(page)
                
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                hire_article_s = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                
                hire_article_s = paginator.page(paginator.num_pages)
            return render(request,'companys/search-result.html',{'form': form, 'hire_article_s': hire_article_s})
    else:
        form = searchform()    
    return render(request, 'home/home.html',{'form': form})
 
def searchuser(request):
    if request.method == 'GET':
        form = searchformuser(request.GET)  
        if form.is_valid():
            category = form.cleaned_data['category']
            localwork = form.cleaned_data['localwork']
            
            results = userpostt.objects.filter(category = category).filter(localwork= localwork).order_by('-id')[:500]
            paginator = Paginator(results, 50)
            page = request.GET.get('page')
            try:
                userlist_s = paginator.page(page)
                
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                userlist_s = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                
                userlist_s = paginator.page(paginator.num_pages)
            return render(request,'users/search-result_users.html',{'form': form, 'userlist_s': userlist_s})
    else:
        form = searchformuser()    
    return render(request, 'home/home.html',{'form': form})


def get_documents(request):
    documents_list = the_documents.objects.all().order_by('-id')[0:500]
    paginator = Paginator(documents_list, 50) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        documents_list_s = paginator.page(page)
        
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        documents_list_s = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        
        documents_list_s = paginator.page(paginator.num_pages)
        
    #return render_to_response('hire/list.html', {"page_list": page_list})
    context = {'documents_list_s': documents_list_s}
    return render(request, 'documents/get_documents.html', context)

def get_documents_detail(request, slug, id):
    p = get_object_or_404(the_documents,slug=slug, pk=id)
    return render_to_response('documents/get_documents_detail.html', {'the_documents': p})   
    
def detail(request, slug, id):
    p = get_object_or_404(hire_article,slug=slug, pk=id)
    form = searchform()
    
    return render_to_response('companys/detail.html', {'hire_article': p, 'form':form})
def users_detail(request, slug, id):
    p = get_object_or_404(userpostt,slug=slug, pk=id)
    form = searchformuser()
    return render_to_response('users/users_detail.html', {'userpostt': p, 'form':form})    


def get_the_about(request):
    # get_the_about=the_about.objects.all()
    # return render(request,'hire/the_about.html', {'get_the_about':get_the_about})
    p = get_object_or_404(the_about)
    return render_to_response('about/about.html', {'the_about': p})

