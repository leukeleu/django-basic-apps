from django.contrib import admin
from basic.blog.models import *
from basic.blog import settings as blog_settings

if blog_settings.EDITOR == 'markitup':
    from django.contrib.admin import ModelAdmin as EditorAdmin
    from markitup.widgets import AdminMarkItUpWidget
elif blog_settings.EDITOR == 'wmdeditor':
    from admin_wmdeditor import WmdEditorModelAdmin as EditorAdmin

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Category, CategoryAdmin)

class PostAdmin(EditorAdmin):
    list_display  = ('title', 'publish', 'status')
    list_filter   = ('publish', 'categories', 'status')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}

    def __init__(self, *args, **kwargs):
        super(PostAdmin, self).__init__(*args, **kwargs)

        if blog_settings.EDITOR == 'wmdeditor':
            self.wmdeditor_fields = ('tease','body')

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name in ['body', 'tease'] and blog_settings.EDITOR == 'markitup':
            kwargs['widget'] = AdminMarkItUpWidget()
        return super(PostAdmin, self).formfield_for_dbfield(db_field, **kwargs)
admin.site.register(Post, PostAdmin)

class BlogRollAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'sort_order',)
    list_editable = ('sort_order',)
admin.site.register(BlogRoll)

admin.site.register(Image)
