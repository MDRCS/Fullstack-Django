from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class PublishedManager(models.Manager):
    """ Custom QuerySet Manager"""

    def get_queryset(self):
        """ override queryset to return just posts that have `publish` status """
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Post(models.Model):

    objects = models.Manager()
    published = PublishedManager()

    STATUS_CHOICE = (('draft', 'DRAFT'), ('published', 'PUBLISHED'))

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICE, default='draft')

    class Meta:
        ordering = ('-publish',)  # display Posts in a desc order
        db_table = 'Posts'

    def __str__(self):
        return self.title
