from django.db import models
from django import template
from django.template.defaultfilters import stringfilter
import re

Post = models.get_model('blog', 'post')
register = template.Library()

@register.tag
def get_latests_months(parser, token):
    """
    Gets the latest months and stores them in a variable

    Syntax::

        {% get_latest_months [limit] as [var_name] %}

    Example usage::

        {% get_latest_months 10 as latest_months %}
    
    """
    try:
        tag_name, arg = token.contents.split(None, 1)
    except ValueError:
        raise template.TemplateSyntaxError, "%s tag requires arguments" % token.contents.split()[0]
    m = re.search(r'(.*?) as (\w+)', arg)
    if not m:
        raise template.TemplateSyntaxError, "%s tag had invalid arguments" % tag_name
    format_string, var_name = m.groups()
    return LatestMonths(format_string, var_name)

class LatestMonths(template.Node):
    def __init__(self, limit, var_name):
        self.limit = limit
        self.var_name = var_name
    
    def render(self, context):
        context[self.var_name] = Post.objects.dates("publish", "month", order="DESC")[:int(self.limit)]
        return ''

@register.filter
@stringfilter
def locale_month(value):
    """ Return the us format for url usage """
    MONTHS = (
        ("mrt", "mar"),
        ("mei", "may"),
        ("okt", "oct"),
        )

    month = [(x[1]) for x in MONTHS if x[0] == value]

    try:
        return month[0]
    except:
        return value
