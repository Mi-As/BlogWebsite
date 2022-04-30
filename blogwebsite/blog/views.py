from django.shortcuts import render
from django.views import generic
from .models import Post, Comment

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/post_list.html'


class PostDetail(generic.DetailView):
    model = Post

    def get_template_names(self):

        context = self.get_context_data()

        if (context["object"].status == 1 or self.request.user.is_superuser):
            return'blog/post_detail.html'

        return 'page/404_page.html'

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        context["comment_list"] = Comment.objects.filter(post_slug=context["object"].slug).values()
        return context