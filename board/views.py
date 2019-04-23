from django.shortcuts import render
from django.views import generic
from django.utils import timezone

from .models import Post

# function based view
def post_list(request):
    posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'board/post_list.html', {'posts':posts})

# class vased view
class DetailView(generic.DetailView):
    model = Post
    template_name = 'board/post_detail.html'