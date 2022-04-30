from django.shortcuts import render, redirect
from django.views import generic, View

from .models import Post, Comment
from .forms import CommentForm

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/post_list.html'


class PostView(View):

    def get(self, request, *args, **kwargs):
        post_data = Post.objects.get(slug=kwargs.get("slug"))

        if (post_data.status == 1 or self.request.user.is_superuser):
            context = {}
            context["post"] = post_data
            context["comment_list"] = \
                Comment.objects.filter(post_slug=post_data.slug).values()
            return render(request,'blog/post_detail.html', context)

        return render(request,'page/404_page.html')

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        # if form.is_valid():
        return redirect(f'/blog/{kwargs.get("slug")}#comments')

