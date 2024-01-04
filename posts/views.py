from django.shortcuts import render , redirect
from .models import Post
from .forms import PostForm

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


def add_post(request):
    if request.method =='POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/blog/')


    else:    
        form = PostForm()

    return render(request,'new_post.html',{'form': form})

def edit_post(request,id):
    post = Post.objects.get(id=id)

    if request.method =='POST':
        form = PostForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            form.save()


    else:    
        form = PostForm(instance=post)

    return render(request,'edit_post.html',{'form': form})


def delete_post(request,id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect('/blog/')

