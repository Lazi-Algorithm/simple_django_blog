from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from django.contrib.auth.views import PasswordChangeView
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from .forms import PostForm, EditForm, CommentForm, PasswordChangingForm, UserRegistrationForm
from django.http import HttpResponseRedirect


# Create your views here.
# Creating Home and detailed view using class-based view
class HomeView(ListView):
    model = Post
    context_object_name = "posts"
    template_name = "home.html"
    ordering = ['-post_date']

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('article-detail', args = [str(pk)]))

class PostDetailView(DetailView):
    model = Post
    template_name = "post_details.html"
    
    def get_context_data(self, *args, **kwargs):
        context = super(PostDetailView, self).get_context_data(
            *args, **kwargs)
        post = get_object_or_404(Post, id=self.kwargs['pk']) #This is to get a particular post
        total_likes = post.total_likes() 
        
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
            
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    

class UpdatePostView(UpdateView):
    model = Post
    template_name = 'update_post.html'
    form_class = EditForm

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)


    success_url = reverse_lazy('home')    
    


class UserRegisterView(CreateView):
    form_class = UserRegistrationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

# class UserEditView(UpdateView):
#     form_class = EditForm
#     template_name = 'registration/edit_profile.html'   
#     success_url = reverse_lazy('home')
     
#     def get_object(self):
#         return self.request.user
    
class PasswordsChangeView(PasswordChangeView):
    form_class= PasswordChangingForm
    template_name = 'registration/change_password.html'
    success_url = reverse_lazy('password_success')

def password_success(request):
    return render(request, 'registration/password_success.html', {} )