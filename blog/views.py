from django.views import generic

from .models import BlogPost, Comment

class IndexView(generic.ListView):
    model = BlogPost
    template_name = 'blog/index.html'
    context_object_name = 'blog_posts'