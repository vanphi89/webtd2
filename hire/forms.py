from django import forms
from django.forms import ModelForm, Textarea
from django.utils.translation import ugettext_lazy as _
from .models import hire_article, userpostt
from django.template.defaultfilters import slugify
from django.db import models
from django.contrib import admin
from .models import category, localwork, salary, exp_year, degree, sex, language, mode_work, applymode, married
from django.utils import timezone

# CHOICES =( ('all', category.objects.all()), ('blue', 'Blue')    )
class postform(forms.ModelForm):
    # checkbox = forms.CharField(widget=forms.CheckboxInput)
    # comment = forms.CharField(widget=forms.Textarea)
    # RadioSelect = comment = forms.CharField(widget=forms.RadioSelect)
    # comment2 = forms.CharField(widget=forms.Textarea(attrs={'cols': 80, 'rows': 20}))
     	
   
    hiring = forms.CharField(widget=forms.TextInput(attrs={'size': '77'}),  label='Vị trí tuyển:')
    
    category = forms.ModelChoiceField(queryset=category.objects.all(),label='Ngành nghề:')
    localwork = forms.ModelChoiceField(queryset=localwork.objects.all(),label='Địa điểm:')
    salary = forms.ModelChoiceField(queryset=salary.objects.all(),label='Mức lương:')
    exp_year = forms.ModelChoiceField(queryset=exp_year.objects.all(),label='Kinh nghiệm:')
    degree = forms.ModelChoiceField(queryset=degree.objects.all(),label='Bằng cấp:')
    sex= forms.ModelChoiceField(queryset=sex.objects.all(),label='Giới tính:')
    language= forms.ModelChoiceField(queryset=language.objects.all(),label='Ngoại ngữ:')
    mode_work= forms.ModelChoiceField(queryset=mode_work.objects.all(),label='Chế độ làm việc:')
    timeover= forms.DateField(label='Hạn nộp:', initial=timezone.now)
    applymode= forms.ModelChoiceField(queryset=applymode.objects.all(),label='Hình thức nộp:')
    number= forms.IntegerField(label='Số lượng:')
    more_require = forms.CharField(widget=forms.Textarea(attrs={'cols': 100}) , required=False, label='Yêu cầu khác:')
    benefit = forms.CharField(widget=forms.Textarea(attrs={'cols': 100}), required=False, label='Chế độ đãi ngộ:')
    document = forms.CharField(widget=forms.Textarea(attrs={'cols': 100}), required=False, label='Hồ sơ gồm:' )
    infomation = forms.CharField(widget=forms.Textarea(attrs={'cols': 100}), required=False, label='Về công ty:')
    namecompany = forms.CharField(widget=forms.TextInput(attrs={'size': '60'}),  label='Tên công ty:')
    email = forms.CharField(widget=forms.EmailInput(attrs={'size': '50'}), required=False, label='Email:')
    
    website = forms.URLField(widget=forms.TextInput(attrs={'size': '69'}), required=False, label='Website:')
    class Meta:
        model = hire_article
        exclude = ['slug', 'whopost']
        
    
        
    
    # category = forms.ModelChoiceField(queryset=category.objects.all(), empty_label=None)
    # category = forms.ModelChoiceField( queryset=category.objects.all(), widget=forms.Select())
        

    
        
class userpostform(forms.ModelForm):
    
    name = forms.CharField(widget=forms.TextInput(attrs={'size': '69'}), label='Họ tên:')
    sex= forms.ModelChoiceField(queryset=sex.objects.all(),label='Giới tính:')
    married= forms.ModelChoiceField(queryset=married.objects.all(),label='Hôn nhân:')
    category = forms.ModelChoiceField(queryset=category.objects.all(),label='Ngành nghề:')
    email = forms.CharField(widget=forms.EmailInput(attrs={'size': '50'}), required=False, label='Email:')
    facebook=forms.URLField(widget=forms.TextInput(attrs={'size': '69'}), required=False, label='Website:')
    localwork = forms.ModelChoiceField(queryset=localwork.objects.all(),label='Địa điểm:')
    salary = forms.ModelChoiceField(queryset=salary.objects.all(),label='Mức lương:')
    exp_year = forms.ModelChoiceField(queryset=exp_year.objects.all(),label='Kinh nghiệm:')
    degree = forms.ModelChoiceField(queryset=degree.objects.all(),label='Bằng cấp:')
    detail = forms.CharField(widget=forms.Textarea(attrs={'cols': 100}) , required=False, label='Thông tin về bản thân:')
    skill = forms.CharField(widget=forms.Textarea(attrs={'cols': 100}) , required=False, label='Kỹ năng:')
    referencer = forms.CharField(widget=forms.Textarea(attrs={'cols': 100}) , required=False, label='Người tham khảo:')
    class Meta:
        model = userpostt
        exclude = ['slug']
class searchform(forms.ModelForm):
    class Meta:
        model = hire_article
        fields = ('category', 'localwork')
        
# class subsearchform(searchform):
#     class Meta(searchform.Meta):
#         
#         fields = ('category', 'localwork')
    

class searchformuser(forms.ModelForm):
    class Meta:
        model = userpostt
        fields =('category', 'localwork')
