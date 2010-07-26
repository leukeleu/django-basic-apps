from django.core.exceptions import ImproperlyConfigured
from basic.blog import settings as blog_settings

if blog_settings.EDITOR == 'markitup':
    try:
        import markitup
    except ImportError:
        raise ImproperlyConfigured('You need to install django-markitup')
elif blog_settings.EDITOR == 'wmdeditor':
    try:
        import admin_wmdeditor
    except ImportError:
        raise ImproperlyConfigured('You need to install admin_wmdeditor')
