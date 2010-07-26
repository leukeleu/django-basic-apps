from django.contrib import admin
from basic.blog.models import *
from markitup.widgets import AdminMarkItUpWidget

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Category, CategoryAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display  = ('title', 'publish', 'status')
    list_filter   = ('publish', 'categories', 'status')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name in ['body', 'tease']:
            kwargs['widget'] = AdminMarkItUpWidget()
        return super(PostAdmin, self).formfield_for_dbfield(db_field, **kwargs)
admin.site.register(Post, PostAdmin)

class BlogRollAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'sort_order',)
    list_editable = ('sort_order',)
admin.site.register(BlogRoll)

admin.site.register(Image)
