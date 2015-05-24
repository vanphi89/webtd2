from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone
import datetime
from django.views.generic import ListView, DetailView #for pagination old: from django.views.generic.list_detail import object_list 
from accounts.models import UserProfile
from django.contrib.auth.models import User
from django.db.models.options import Options
from django.core.urlresolvers import reverse

class category(models.Model):
    category_field = models.CharField(max_length=128)
    def __str__(self):  #For Python 2, use __str__ on Python 3
        return self.category_field
    class Meta:
        ordering = ["category_field"]

class salary(models.Model):
    salary = models.CharField(max_length=15)
    def __str__(self):     
        return self.salary
    class Meta:
        ordering = ["salary"]

class mode_work(models.Model):
    mode_work = models.CharField(max_length=15)
    def __str__(self):     
        return self.mode_work

class localwork(models.Model):
    localwork = models.CharField(max_length=30)
    def __str__(self):     
        return self.localwork
    slug = models.SlugField(max_length=300)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.localwork)
        super(localwork, self).save(*args, **kwargs)
    class Meta:
        ordering = ["localwork"]
        
class exp_year(models.Model):
    exp_year = models.CharField(max_length=15)
    def __str__(self):     
        return self.exp_year
    class Meta:
        ordering = ["exp_year"]

class degree(models.Model):
    degree = models.CharField(max_length=20)
    def __str__(self):     
        return self.degree

class sex(models.Model):
    sex = models.CharField(max_length=20)
    def __str__(self):     
        return self.sex

class language(models.Model):
    language = models.CharField(max_length=20)
    def __str__(self):     
        return self.language

class applymode(models.Model):
    applymode = models.CharField(max_length=20)
    def __str__(self):     
        return self.applymode

class married(models.Model):
    married = models.CharField(max_length=15)
    def __str__(self):     
        return self.married

class hire_article(models.Model):
    hiring = models.CharField(max_length=250)
    category = models.ForeignKey(category)
    localwork = models.ForeignKey(localwork)
    salary = models.ForeignKey(salary)
    exp_year = models.ForeignKey(exp_year)
    degree = models.ForeignKey(degree)
    sex = models.ForeignKey(sex)
    language = models.ForeignKey(language)
    more_require = models.TextField(max_length=1000, blank=True)
    benefit = models.TextField(max_length=1000, blank=True)
    document = models.TextField(max_length=1000, blank=True)
    number = models.IntegerField(default=0, blank=True)
    mode_work = models.ForeignKey(mode_work)
    timeover = models.DateField(default=timezone.now, blank=True)
    applymode = models.ForeignKey(applymode)
    #### COmpany infomation
    namecompany = models.CharField(max_length=200)
    phone = models.CharField(max_length=15,default="0")
    email = models.EmailField(max_length=100,blank=True)
    website = models.URLField(max_length=200, blank=True)
    infomation = models.TextField(max_length=1000, blank=True)
    #######timepost
    publication_date = models.DateField(auto_now=True)
    
    # def get_absolute_url(self):
    #     return reverse('hire.views.detail', self.id ,self.slug)
    # whopost = models.ForeignKey(UserProfile, null=True)
#    , default =UserProfile.objects.get(id=a)
# # # # # #     Co the add editable=False
    slug = models.SlugField(max_length=300)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.hiring)
        super(hire_article, self).save(*args, **kwargs)
    def ID(self, obj):
        return obj.id
    # class Meta:
    #     ordering = ["-hiring"]
    def __str__(self):      
        return self.hiring
    

class userpostt(models.Model):
    image = models.ImageField(upload_to='static/avatas', null=True, blank=True)
    name = models.CharField(max_length=100)
    birthday = models.DateField(auto_now=True)
    sex = models.ForeignKey(sex)
    married = models.ForeignKey(married)
    category = models.ForeignKey(category)
    localwork = models.ForeignKey(localwork)
    salary = models.ForeignKey(salary)
    degree = models.ForeignKey(degree)
    exp_year = models.ForeignKey(exp_year)
    detail = models.TextField(max_length=1000, blank=True)
    skill = models.TextField(max_length=1000, blank=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=100,blank=True)
    facebook = models.URLField(max_length=300, blank=True)
    referencer =  models.TextField(max_length=2000, blank=True)
    
    
    publication_date = models.DateField(auto_now=True)
    
    slug = models.SlugField(max_length=300)
    # def was_published_recently(self):
    #     return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(userpostt, self).save(*args, **kwargs)
    def ID(self, obj):
        return obj.id
    
    def __str__(self):      
        return self.name

class the_documents(models.Model):
    name = models.CharField(max_length=200)
    article_s = models.TextField(max_length=5000)
    publication_date = models.DateField(auto_now=True)
    
    slug = models.SlugField(max_length=300)
    # def was_published_recently(self):
    #     return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(the_documents, self).save(*args, **kwargs)
    def ID(self, obj):
        return obj.id
    
    def __str__(self):      
        return self.name
class the_about(models.Model):
    article_s = models.TextField(max_length=5000)
