from django.shortcuts import render 
from .models import Post
from .forms import PostForm

# # Functions

# def post_list(request):
#     data = Post.objects.all()    # model : query
#     return render(request,'posts_list.html',{'posts':data}) #2-template:frontend 3-context {}

# 1: Class
# 4:

from django.views.generic import ListView , DetailView , CreateView , UpdateView ,DeleteView

class PostList(ListView):
    model = Post  # 1-model : query   2-post_list.html  3-post_list 




# 6 : DetailView

class PostDetail(DetailView):
    model =Post                              #context:post



#8 : CreateView !

class PostCreate(CreateView):
    model = Post
    #fields = '__all__'
    success_url='/blog'        
    form_class = PostForm


#10:PostCreate 
    
class PostEdit(UpdateView):
    model = Post
    #fields = '__all__'
    success_url='/blog'
    template_name ='posts/edit_post.html'  
    form_class = PostForm


# 11. DeleteView 

class PostDelete(DeleteView):
    model = Post
    success_url ='/blog'       




