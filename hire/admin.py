from django.contrib import admin
from .models import category, hire_article, localwork, salary, mode_work, exp_year, degree, sex, language, applymode, userpostt, married, the_documents, the_about



class hire_articleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("hiring",)}
    list_display = ('id', 'hiring', 'publication_date', 'phone', )
    list_filter = ('hiring',)
    search_fields = ('hiring',)
    # fieldsets = (
    #     (None, {
    #         'fields': ('hiring','category', 'localwork', 'salary', 'mode_work', 'exp_year', 'degree', 'sex', 'language', 'applymode','slug')
    #     }),
    #     )
    
#      code below to sort field in class models

class userpostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('id', 'name', 'publication_date', 'phone', )

class the_documentsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('id', 'name', 'publication_date' )
    
class categoryAdmin(admin.ModelAdmin):
    list_filter = ('category_field',)
    search_fields = ('category_field',)
    
class localworkAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("localwork",)}
    
admin.site.register(category, categoryAdmin)
admin.site.register(localwork, localworkAdmin)
admin.site.register(salary)
admin.site.register(exp_year)
admin.site.register(degree)
admin.site.register(sex)
admin.site.register(language)
admin.site.register(mode_work)
admin.site.register(hire_article, hire_articleAdmin)

admin.site.register(applymode)
admin.site.register(userpostt, userpostAdmin)
admin.site.register(married)
admin.site.register(the_documents, the_documentsAdmin)
admin.site.register(the_about)
