from django.shortcuts import render
from .models import Post
# Create your views here.

'''
view :
    - url
    - model
    - template
'''







def post_list(request):
    data = Post.objects.all()    # model
    return render(request,'posts_list.html',{'posts':data})

