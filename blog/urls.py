"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from posts.views import post_list , post_detail , add_post , edit_post , delete_post

#2class
from posts.views2 import PostList ,PostDetail,PostCreate,PostEdit,PostDelete


from django.conf import settings
from django.conf.urls.static import static

#3class (PostList.as_view)
#7:PostDetail
#bei class muss ich pk benutzen
#9: PostCreate
urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', PostList.as_view()),
    path('blog/new', PostCreate.as_view()),
    path('blog/<int:pk>', PostDetail.as_view()),
    path('blog/<int:pk>/edit' , PostEdit.as_view()),
    path('blog/<int:pk>/delete' , PostDelete.as_view()),

    path('summernote/', include('django_summernote.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
