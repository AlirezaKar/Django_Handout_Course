from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Post, PostDetail, Comment, User, MultiMedia

admin.site.unregister(Group)

admin.site.register([User,MultiMedia])

admin.site.index_title = "Tutorial Website" 
admin.site.site_title = "Admin"
admin.sites.AdminSite.site_header = 'Tutorial Website'

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['content', 'user', 'status', 'text']
    list_display_links = ['text', 'user', 'content']
    list_filter = ['user', 'status']
    list_editable = ['status']
    search_fields = ['text']

# class PostDetailInline(admin.TabularInline):
#     model = PostDetail
#     extra = 1  
#     can_delete = True
#     fields = ['field_name', 'field_content']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # inlines = [PostDetail]
    list_display = ['title', 'user', 'status']
    list_display_links = ['title', 'user']
    list_filter = ['status', 'user']
    list_editable = ['status']
    search_fields = ['title', 'description']