from django import template
import pandas as pd

register = template.Library()


@register.filter
def addclass(field, css):
    return field.as_widget(attrs={'class': css})


@register.filter()
def as_table(queryset):
    table = pd.DataFrame.from_dict(list(queryset), orient='columns')
    html_table = table.groupby(['pupil']).code__subj.mean().agg(list)
    print(html_table)
    #for key, value in queryset.items():
    #    try:
    #        field = value
    #        if field:
    #            ret += '<tr><th>'+key+'</th></tr><tr><td>'+value+'</td></tr>'
    #    except AttributeError:
    #        pass
    return html_table
