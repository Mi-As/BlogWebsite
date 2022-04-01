from django.shortcuts import render
from django.views import generic
from .models import Post

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
