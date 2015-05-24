from django import template
register = template.Library()

@register.filter
def page_filter(value, arg):
    if arg>=5:
        return value[arg-5:arg+4]
    else:
        return value[0:9]
@register.filter    
def result_filter(value):
    if "&page=" in value:
        i=value.index("&page")
        return value[0:i]
    else:
        return value
    
    
    

    
    
    
    
    