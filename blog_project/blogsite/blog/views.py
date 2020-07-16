from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from blog.models import Post, Comment
from django.utils import timezone
from django.urls import reverse_lazy
from blog.forms import PostForm, CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.
class AboutView(TemplateView):
    template_name = 'about.html'


# ======================= POST START CRUD (Create Retrieve Update Delete) =======================

class PostListView(ListView):
    model = Post

    def get_queryset(self):
        """
        1. __lte after published_date means the 'less than equal' condition for published_date
           compare with timezone.now() -> look up to the Django documentation for "Field lookups"
        2. min (-) character before published_date means descending order
        """
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post

class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog:postlist')

class PostDraftView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('created_date')

# ======================== POST END CRUD (Create Retrieve Update Delete) ========================

@login_required
def add_comment(request, pk):
    p = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        f = CommentForm(request.POST)
        if f.is_valid():
            c = f.save(commit=False)
            c.post = p
            c.save()
            return redirect('blog:postdetail', pk=p.pk)
    else:
        f = CommentForm()
    return render(request, 'blog/comment_form.html',{'form':f})

@login_required
def approve_comment(request, pk):
    c = get_object_or_404(Comment, pk=pk)
    p_pk = c.post.pk
    c.approve()
    return redirect('blog:postdetail', pk=p_pk)

@login_required
def remove_comment(request, pk):
    c = get_object_or_404(Comment, pk=pk)
    p_pk = c.post.pk
    c.delete()
    return redirect('blog:postdetail', pk=p_pk)

@login_required
def post_publish(request, pk):
    p = get_object_or_404(Post, pk=pk)
    p.publish()
    return redirect('blog:postdetail', pk=pk)