from django.conf import settings

EDITOR = getattr(settings, 'BLOG_EDITOR', 'markitup')
