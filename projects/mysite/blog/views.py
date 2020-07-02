from django.shortcuts import render, get_object_or_404
from . import models
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from django.core.mail import send_mail
from django.views.generic import ListView
from .forms import EmailPostForm, CommentForm
from taggit.models import Tag
from django.db.models import Count

# class PostListView(ListView):
#     """ class based view """
#     queryset = models.Post.published.all()
#     context_object_name = 'posts'
#     paginate_by = 3
#     template_name = 'blog/post/list.html'

    # In order to keep pagination working, you have to use the right page object that object that is passed to the
    # template. Django's ListView generic view passes the selected page in a variable called `page_obj`, so you have
    # to edit your post/list.html template accordingly to include the paginator using the right variable, as follows:


# class based views is a generic solution to define views better than the code below

def post_list(request, tag_slug=None):
    object_list = models.Post.published.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])

    paginator = Paginator(object_list, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/post/list.html', {'page': page, 'posts': posts, 'tag': tag})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(models.Post, slug=post, publish__year=year, publish__month=month, publish__day=day)
    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = models.Post.published.filter(tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags', '-publish')[:4]
    # comments is the relative_name of the relationship between Post and Comment
    # list active comments for this post
    comments = post.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # create a Comment object without saving into database.
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, 'blog/post/detail.html', {'post': post, 'comments': comments, 'new_comment': new_comment, 'comment_form': comment_form, 'similar_posts': similar_posts})


def post_share(request, post_id):
    post = get_object_or_404(models.Post, id=post_id, status='published')

    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # send the email
            # If your form data does not validate, cleaned_data will contain only the valid fields.
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} recommands you to read {post.title}"
            message = f"Read {post.title} at {post_url} \n\n {cd['name']} is comments \n \n {cd['comments']}"

            send_mail(subject, message, 'elrahali.md@gmail.com', [cd['to']])
            send = True
    else:
        form = EmailPostForm()

    return render(request, 'blog/post/share.html', {'post': post, 'form': form})
