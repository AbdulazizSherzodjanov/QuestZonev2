from django.contrib import admin
from blog.models import PostModel,Comment







class PostModelAdmin(admin.ModelAdmin):
    list_display = ['title','author','create_at']


admin.site.register(PostModel,PostModelAdmin)
admin.site.register(Comment)