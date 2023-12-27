from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['id','name','created_at']
    list_filter =['created_at']
    search_fields =['name','content']


admin.site.register(Post,PostAdmin)
