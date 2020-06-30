from django.shortcuts import render, get_object_or_404
from . import models
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from django.views.generic import ListView


class PostListView(ListView):
    """ class based view """
    queryset = models.Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'

    # In order to keep pagination working, you have to use the right page object that object that is passed to the
    # template. Django's ListView generic view passes the selected page in a variable called `page_obj`, so you have
    # to edit your post/list.html template accordingly to include the paginator using the right variable, as follows:

# class based views is a generic solution to define views better than the code below

# def post_list(request):
#     object_list = models.Post.published.all()
#
#     paginator = Paginator(object_list, 3)
#     page = request.GET.get('page')
#     try:
#         posts = paginator.page(page)
#     except PageNotAnInteger:
#         posts = paginator.page(1)
#     except EmptyPage:
#         posts = paginator.page(paginator.num_pages)
#
#     return render(request, 'blog/post/list.html', {'page': page, 'posts': posts})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(models.Post, slug=post, publish__year=year, publish__month=month, publish__day=day)
    return render(request, 'blog/post/detail.html', {'post': post})
