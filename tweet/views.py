from django.views.generic import ListView, CreateView
from .models import Post


class PostListView(ListView):
    model = Post
    template_name = "tweet/index.html"
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


class PostCreateView(CreateView):
    model = Post
    fields = ['content']
    template_name = 'tweet/post_create.html'
    success_url = '/'
