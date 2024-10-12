from django.contrib import admin
from .models import Blog, About, Contact, Comment, Tag, Subsription, Home


# @admin.register(Blog)

class BlogAdmin(admin.ModelAdmin):
    fields = ['title', 'image', 'description', 'description2', 'tag', 'create_date', 'update_date']
    list_display = ['title', 'create_date']
    readonly_fields = ('create_date', 'update_date')


# @admin.register(Contact)

class ContactAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'phone', 'create_date', 'is_published']
    list_filter = ['id', 'is_published']


admin.site.register(Blog, BlogAdmin)
admin.site.register(About)
admin.site.register(Comment)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Tag)
admin.site.register(Subsription)
admin.site.register(Home)

