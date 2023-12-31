from django.shortcuts import render
from .models import Post

'''
view :
    - url
    - model
    - template
'''

def post_list(request):
    data = Post.objects.all()    # model
    return render(request,'posts_list.html',{'posts':data})



def post_detail(request,id):
    data = Post.objects.get(id=id)
    return render(request,'post_detail.html',{'post':data})

