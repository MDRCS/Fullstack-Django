# Django-REST

    + setting up dev environment :

    1- virtualenv venv --python=python3.7
    2- source ./venv/bin/activate

    + create Django project :

    3- mkdir src && cd src
    4- django-admin startproject django_project

    + generate django project :

    5- cd django_project
    6- python manage.py startapp django_restapi


    + enable restframework :

    8- go to settings.py -> INSTALLED_APPS -> add
       'rest_framework',
       'rest_framework.authtoken'
        'django_restapi'

    + run django app :
    - if you had a problem with import rest_framework run ->  pip3 install djangorestframework
    - python manage.py migrate
    9- python manage.py runserver


    + set our Custom Model for Auth in settings.py :

    - after creating UserProfile and UserProfileManager in models.py i should config the Auth settings in settings.py
    - add this line in the end of settings.py -> AUTH_USER_MODEL = 'django_restapi.UserProfile'

    - make a migration
    + python manage.py makemigrations
    django_restapi/migrations/0001_initial.py

    + python manage.py migrate
    ! if you had a problem with migration delete db.sqlite3

    - Django Admin Panel
    + create a superuser :

    1- python manage.py createsuperuser
    2- go to admin.py add :
        from . import models
        admin.site.register(models.UserProfile)

    3- python manage.py runserver
       check localhost:8080/admin


    APIView allow us to define functions that match standard HTTP methods like GET,POST,PUT,PATCH,etc.
    Viewsets allow us to define functions that match to common API object actions like :LIST, CREATE, RETRIEVE, UPDATE, etc.

    Vieewsets are also used to write logic to perform standard database operations and to interface with a database back-end.And are usually used for existing database model to manage predefined objects
        "token": "9262352dbe2f2c8d3f908da5c6034499a6ed6fbc"

    + To Test Authorization :

    1- we built an ViewSet for login, defined create/Post operation and made it return a token for a Login Email/Password.
    2- run django server, go to /api/login enter infos and click post you will got a token save it.
    3- go to chrome extensions download mod header, add this two headers :

![](./static/mod_header.png)

    4- go to /api/profile/1
     -> now you can update the field not like before now you have a valid permissions.


    - we create a new model called ProfileFeedItem
    ++ now we should run a migration

    $ python manage.py makemigrations
    $ python manage.py migrate


    + Deployements :

    1- Create an EC2 instance
    2- login into and run wget github_account/setup.sh
    3- chmod +x setup.sh and run sudo ./setup.sh
    4- activate venv and run migration
    5- add domain name into profiles_project/settings.py
        ALLOWED_HOSTS = [
            'ec2-18-130-20-217.eu-west-2.compute.amazonaws.com',
            '127.0.0.1'
        ]
    6- supervisorctl restart all

    - Test you api

    1- /profile create one
    2- login get the token and test all operations

### + Django - The Easy Way :

    - create a new django project
    + django-admin startproject mysite . # create a skelton of a django project
    + python manage.py runserver # run the project
    + python manage.py makemigrations
    + python manage.py startapp myapp

    - Edit mysite app settings.py file and add myapp to the INSTALLED_APPS list:
     INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'myapp', # < here
        ]

    9.3 Creating template files
    Create index.html file in the myapp templates folder. You have to create the templates and myapp folders too:

        Folder structure for templates
        ├── 09-Hello-World
        │   ├── db.sqlite3
        │   ├── manage.py
        │   ├── myapp
        │   │   ├── templates <-- here
        │   │   │   └── myapp <-- here
        │   │   │       └── index.html <-- here”

    9.4 Creating views
    Edit myapp app views.py file and add an index function:

    -> myapp/views.py

    from django.shortcuts import render

    def index(request): # < here
        return render(request, 'myapp/index.html')

    Edit mysite app urls.py file add the index path to the urlpatterns list:

    -> mysite/urls.py

    from django.contrib import admin
    from django.urls import path

    from myapp import views as myapp_views # < here

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', myapp_views.index, name='index'), # < here
    ]

    + python manage.py runserver

    For example the default database configuration looks like this:

        -> mysite/settings.py
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            }
        }

        This allows you to start working with a database immediately.

        - For PostgreSQL database we would do something like this:

        PostgreSQL configuration example
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'NAME': 'mysitedb',
                'USER': 'username',
                'PASSWORD': 'password',
                'HOST': 'localhost',
                'PORT': '',
            }
        }”


### + Building a Blog Application

    This chapter will cover the following topics:

    Installing Django
    Creating and configuring a Django project
    Creating a Django application
    Designing models and generating model migrations
    Creating an administration site for your models
    Working with QuerySets and managers
    Building views, templates, and URLs
    Adding pagination to list views
    Using Django's class-based views


    create new project :

    - django-admin startproject mysite
    - cd mysite
    - python manage.py migrate

    ++ Remember that this server is only intended for development and is not suitable for production use. In order to deploy
       Django in a production environment, you should run it as a WSGI application using a web server, such as Apache,
       Gunicorn, or uWSGI, or as an ASGI application using a server like Uvicorn or Daphne. You can find more information
       on how to deploy Django with different web servers at https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/.

    - settings.py
    The following settings are worth looking at:

    + DEBUG is a Boolean that turns the debug mode of the project on and off. If it is set to True, Django will display detailed error pages when an uncaught
    exception is thrown by your application. When you move to a production environment, remember that you have to set it to False. Never deploy a site into
    production with DEBUG turned on because you will expose sensitive project-related data.

    + ALLOWED_HOSTS is not applied while debug mode is on or when the tests are run. Once you move your site to production and set DEBUG to False, you will
      have to add your domain/host to this setting in order to allow it to serve your Django site.

    + INSTALLED_APPS is a setting you will have to edit for all projects. This setting tells Django which applications are active for this site.


    - Creating an application
    Now let's create your first Django application. You will create a blog application from scratch. From the project's root directory, run the following command:

    + python manage.py startapp blog

    - When you create a model, Django will provide you with a practical API to query objects in the database easily.”

    - models.py
    - describing  model `Post` is fields :

    slug: This is a field intended to be used in URLs. A slug is a short label that contains only letters,
          numbers, underscores, or hyphens. You will use the slug field to build beautiful, SEO-friendly URLs
          for your blog posts. You have added the unique_for_date parameter to this field so that you can build
          URLs for posts using their publish date and slug. Django will prevent multiple posts from having
          the same slug for a given date.

    author: This field defines a many-to-one relationship, meaning that each post is written by a user, and a user
            can write any number of posts. For this field, Django will create a foreign key in the database using the primary
            key of the related model. In this case, you are relying on the User model of the Django authentication system.
            The on_delete parameter specifies the behavior to adopt when the referenced object is deleted. This is not specific
            to Django; it is an SQL standard. Using CASCADE, you specify that when the referenced user is deleted, the database
            will also delete all related blog posts. You can take a look at all the possible options
            at https://docs.djangoproject.com/en/3.0/ref/models/fields/#django.db.models.ForeignKey.on_delete.
            You specify the name of the reverse relationship, from User to Post, with the related_name attribute.
            This will allow you to access related objects easily.

    created: This datetime indicates when the post was created. Since you are using auto_now_add here, the date will be saved automatically when creating an object.
    updated: This datetime indicates the last time the post was updated. Since you are using auto_now here, the date will be updated automatically when saving an object.
    status: This field shows the status of a post. You use a choices parameter, so the value of this field can only be set to one of the given choices.”

    The Meta class inside the model contains metadata. You tell Django to sort results by the publish field in descending order by default when you query the database.
    You specify the descending order using the negative prefix. By doing this, posts published recently will appear first.

    Activating the application
    In order for Django to keep track of your application and be able to create database tables for its models, you have to activate it. To do this, edit the settings.py
    file and add blog.apps.BlogConfig to the INSTALLED_APPS setting.

    The BlogConfig class is your application configuration. Now Django knows that your application is active for this project and will be able to load its models.

    Creating and applying migrations
    Now that you have a data model for your blog posts, you will need a database table for it. Django comes with a migration system that tracks the changes made to models
    and enables them to propagate into the database. As mentioned, the migrate command applies migrations for all applications listed in INSTALLED_APPS; it synchronizes
    the database with the current models and existing migrations.

    + python manage.py makemigrations blog

    - Let's take a look at the SQL code that Django will execute in the database to create the table for your model. The sqlmigrate command takes the migration names and returns
      their SQL without executing it.

    + python manage.py sqlmigrate blog 0001

    - The exact output depends on the database you are using. The preceding output is generated for SQLite. As you can see in the output, Django generates the table names by combining
      the application name and the lowercase name of the model (blog_post), but you can also specify a custom database name for your model in the Meta class of the model using the db_table attribute.

    + python manage.py migrate

    - Creating an administration site for models
    Now that you have defined the Post model, you will create a simple administration site to manage your blog posts. Django comes with a built-in administration interface that is very useful for editing content.

    - Creating a superuser :
    + python manage.py createsuperuser

    Adding models to the administration site
    Let's add your blog models to the administration site. Edit the admin.py file of the blog application and make it look like this:

    from django.contrib import admin
    from .models import Post
    admin.site.register(Post)

    Adding models to the administration site
    Let's add your blog models to the administration site. Edit the admin.py file of the blog application and make it look like this:

    from django.contrib import admin
    from .models import Post
    admin.site.register(Post)

    Customizing the way that models are displayed
    Now, we will take a look at how to customize the administration site. Edit the admin.py file of your blog application and change it, as follows:

    from django.contrib import admin
    from .models import Post

    @admin.register(Post)
    class PostAdmin(admin.ModelAdmin):
        list_display = ('title', 'slug', 'author', 'publish', 'status')

    You are telling the Django administration site that your model is registered in the site using a custom class that inherits from”

    ModelAdmin. In this class, you can include information about how to display the model in the site and how to interact with it.

    The list_display attribute allows you to set the fields of your model that you want to display on the administration object list page. The @admin.register() decorator performs the same function as the admin.site.register() function that you replaced, registering the ModelAdmin class that it decorates.

    Let's customize the admin model with some more options, using the following code:

    @admin.register(Post)
    class PostAdmin(admin.ModelAdmin):
        list_display = ('title', 'slug', 'author', 'publish', 'status')
        list_filter = ('status', 'created', 'publish', 'author')
        search_fields = ('title', 'body')
        prepopulated_fields = {'slug': ('title',)}
        raw_id_fields = ('author',)
        date_hierarchy = 'publish'
        ordering = ('status', 'publish')

+ this is the result of our Custom admin panel :

![](./static/custom_admin_panel.png)

    You can see that the fields displayed on the post list page are the ones you specified in the list_display attribute. The list page now includes a right sidebar that allows you to filter the results by the fields included in the list_filter attribute.
    A search bar has appeared on the page. This is because you have defined a list of searchable fields using the search_fields attribute. Just below the search bar, there are navigation links to navigate through a date hierarchy; this has been defined by the date_hierarchy attribute.
    You can also see that the posts are ordered by STATUS and PUBLISH columns by default. You have specified the default sorting criteria using the ordering attribute.
    Next, click on the ADD POST link. You will also note some changes here. As you type the title of a new post, the slug field is filled in automatically. You have told Django to prepopulate

    the slug field with the input of the title field using the prepopulated_fields attribute.
    Also, the author field is now displayed with a lookup widget that can scale much better than a drop-down select input when you have thousands of users. This is achieved with the raw_id_fields attribute and it looks like this:

    - Working with QuerySets and managers

    The Django ORM is based on QuerySets. A QuerySet is a collection of database queries to retrieve objects from your database. You can apply filters to QuerySets to narrow down the query results based on given parameters.

    Creating objects
    Open the terminal and run the following command to open the Python shell:

    + python manage.py shell

    Then, type the following lines:

    >>> from django.contrib.auth.models import User
    >>> from blog.models import Post
    >>> user = User.objects.get(username='mdrahali')
    >>> post = Post(title='Another post',
    ...             slug='another-post',
    ...             body='Post body.',
    ...             author=user)
    ... post.save()

    The preceding action performs an INSERT SQL statement behind the scenes. You have seen how to create an object
    in memory first and then persist it to the database, but you can also create the object and persist it into the
    database in a single operation using the create() method, as follows:

    Post.objects.create(title='One more post',
                        slug='one-more-post',
                        body='Post body.',
                        author=user)
    Updating objects
    Now, change the title of the post to something different and save the object again:

    >>> post.title = 'New title'
    >>> post.save()
    This time, the save() method performs an UPDATE SQL statement.

    >>> all_posts = Post.objects.all()
    This is how you create a QuerySet that returns all objects in the database. Note that this QuerySet has not been executed yet.
    Django QuerySets are lazy, which means they are only evaluated when they are forced to be. This behavior makes QuerySets very
    efficient. If you don't set the QuerySet to a variable, but instead write it directly on the Python shell, the SQL statement
    of the QuerySet is executed because you force it to output results:

    >>> all_posts

    Using the filter() method

    To filter a QuerySet, you can use the filter() method of the manager. For example, you can retrieve all posts published in the year 2020 using the following QuerySet:

    >>> Post.objects.filter(publish__year=2020)
    You can also filter by multiple fields. For example, you can retrieve all posts published in 2020 by the author with the username admin:

    >>> Post.objects.filter(publish__year=2020, author__username='admin')

    Using exclude()

    You can exclude certain results from your QuerySet using the exclude() method of the manager. For example, you can retrieve all posts published in 2020 whose titles don't start with Why:

    >>> Post.objects.filter(publish__year=2020) \
    >>>             .exclude(title__startswith='Why')

    Using order_by()

    You can order results by different fields using the order_by() method of the manager. For example, you can retrieve all objects ordered by their title, as follows:

    >>> Post.objects.order_by('title')
    Ascending order is implied. You can indicate descending order with a negative sign prefix, like this:

    >>> Post.objects.order_by('-title')
    Deleting objects
    If you want to delete an object, you can do it from the object instance using the delete() method:

    >>> post = Post.objects.get(id=1)
    >>> post.delete()
    Note that deleting objects will also delete any dependent relationships for ForeignKey objects defined with on_delete set to CASCADE.


    - Creating model managers
    As I previously mentioned, objects is the default manager of every model that retrieves all objects in the database. However, you can also define custom managers
    for your models. You will create a custom manager to retrieve all posts with the published status.
    There are two ways to add or customize managers for your models: you can add extra manager methods to an existing manager,
    or create a new manager by modifying the initial QuerySet that the manager returns. The first method provides you with a QuerySet
    API such as Post.objects.my_manager(), and the latter provides you with Post.my_manager.all(). The manager will allow you to
    retrieve posts using Post.published.all().

    The get_queryset() method of a manager returns the QuerySet that will be executed. You override this method to include your custom filter in the final QuerySet.

    - test it :
    + python manage.py shell

    >>> from blog.models import Post
    >>> Post.published.filter(title__startswith='Another')

    - Building list and detail views
    A Django view is just a Python function that receives a web request and returns

    a web response. All the logic to return the desired response goes inside the view.
    First, you will create your application views, then you will define a URL pattern for each view, and finally, you will create HTML templates to render the data generated by the views. Each view will render a template, passing variables to it, and will return an HTTP response with the rendered output.”

    Creating list and detail views
    Let's start by creating a view to display the list of posts. Edit the views.py file of your blog application and make it look like this:

    from django.shortcuts import render, get_object_or_404
    from .models import Post
    def post_list(request):
        posts = Post.published.all()
        return render(request,
                     'blog/post/list.html',
                     {'posts': posts})

    You just created your first Django view. The post_list view takes the request object as the only parameter. This parameter is required by all views. In this view, you retrieve all the posts with the published status using the published manager that you created previously

    AAdding URL patterns for your views
    URL patterns allow you to map URLs to views. A URL pattern is composed of a string pattern, a view, and, optionally, a name that allows you to name the URL project-wide. Django runs through each URL pattern and stops at the first one that matches the requested URL. Then,
    Django imports the view of the matching URL pattern and executes it,

    Create a urls.py file in the directory of the blog application and add the following lines to it:

    from django.urls import path
    from . import views
    app_name = 'blog'
    urlpatterns = [
        # post views
        path('', views.post_list, name='post_list'),
        path('<int:year>/<int:month>/<int:day>/<slug:post>/',
             views.post_detail,
             name='post_detail'),
    ]

    - In the preceding code, you define an application namespace with the app_name variable. This allows you to organize URLs by application and use the name when referring to them. You define two different patterns using the path() function.

    Next, you have to include the URL patterns of the blog application in the main URL patterns of the project.

    Edit the urls.py file located in the mysite directory of your project and make it look like the following:

    from django.urls import path, include
    from django.contrib import admin
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('blog/', include('blog.urls', namespace='blog')),
    ]

    - Canonical URLs for models
    A canonical URL is the preferred URL for a resource. You may have different pages in your site where you display posts, but there is a single URL that
    you use as the main URL for a blog post. The convention in Django is to add a get_absolute_url() method to the model that returns the canonical URL for the object.

    Edit the models.py file of the blog application and add the following code:

    from django.urls import reverse
    class Post(models.Model):
        # ...
        def get_absolute_url(self):
            return reverse('blog:post_detail',
                           args=[self.publish.year,
                                 self.publish.month,
                                 self.publish.day, self.slug])


    You will use the get_absolute_url() method in your templates to link to specific posts.”

    + Creating templates for your views
    You have created views and URL patterns for the blog application. URL patterns map URLs to views, and views decide which data gets returned to the user.
    Templates define how the data is displayed; they are usually written in HTML in combination with the Django template language.

    Create the following directories and files inside your blog application directory:

    templates/
        blog/
            base.html
            post/
                list.html
                detail.html

    Django has a powerful template language that allows you to specify how data is displayed. It is based on template tags, template variables, and template filters:

    Template tags control the rendering of the template and look like {% tag %}
    Template variables get replaced with values when the template is rendered and look like {{ variable }}
    Template filters allow you to modify variables for display and look like {{ variable|filter }}.

    {% load static %} tells Django to load the static template tags that are provided by the django.contrib.staticfiles application, which is contained in the INSTALLED_APPS setting.
    After loading them, you are able to use the {% static %} template tag throughout this template. With this template tag, you can include the static files, such as the blog.css file

    + python manage.py runserver
    check http://127.0.0.1:8000/blog/ in the browser


    for the post details :
    + Take a look at the URL—it should be /blog/2020/1/1/who-was-django-reinhardt/. You have designed SEO-friendly URLs for your blog posts.”

    + Adding pagination

    When you start adding content to your blog, you might easily reach the point where tens or hundreds of posts are stored in your database. Instead of displaying all the posts on a single page, you may want to split the list of posts across several pages. This can be achieved through pagination. You can define the number of posts you want to be displayed per page and retrieve the posts that correspond to the page requested by the user. Django has a built-in pagination class that allows you to manage paginated data easily.
    Edit the views.py file of the blog application to import the Django paginator classes and modify the post_list view, as follows:

    This is how pagination works:

    You instantiate the Paginator class with the number of objects that you want to display on each page.
    You get the page GET parameter, which indicates the current page number.
    You obtain the objects for the desired page by calling the page() method of Paginator.
    If the page parameter is not an integer, you retrieve the first page of results. If this parameter is a number higher than the last page of results, you retrieve the last page.
    You pass the page number and retrieved objects to the template.


    Now you have to create a template to display the paginator so that it can be included in any template that uses pagination. In the templates/ folder of the blog application, create a new
    file and name it pagination.html. Add the following HTML code to the file:

    <div class="pagination">
      <span class="step-links">
        {% if page.has_previous %}
          <a href="?page={{ page.previous_page_number }}">Previous</a>
        {% endif %}
        <span class="current">
          Page {{ page.number }} of {{ page.paginator.num_pages }}.
        </span>
        {% if page.has_next %}
          <a href="?page={{ page.next_page_number }}">Next</a>
        {% endif %}
      </span>
    </div>

    The pagination template expects a Page object in order to render the previous and next links, and to display the current page and total pages of results.
    Let's return to the blog/post/list.html template and include the pagination.html template at the bottom of the {% content %} block, as follows:

    {% block content %}
      ...
      {% include "pagination.html" with page=posts %}
    {% endblock %}

    “Edit the views.py file of your blog application and add the following code:

    from django.views.generic import ListView
    class PostListView(ListView):
        queryset = Post.published.all()
        context_object_name = 'posts'
        paginate_by = 3
        template_name = 'blog/post/list.html'
    This class-based view is analogous to the previous post_list view. In the preceding code, you are telling ListView to do the following things:

    Use a specific QuerySet instead of retrieving all objects. Instead of defining a queryset attribute, you could have specified model = Post and Django would have built the generic Post.objects.all() QuerySet for you.
    Use the context variable posts for the query results. The default variable is object_list if you don't specify any context_object_name.
    Paginate the result, displaying three objects per page.
    Use a custom template to render the page. If you don't set a default template, ListView will use blog/post_list.html.
    Now open the urls.py file of your blog application, comment the preceding post_list URL pattern, and add a new URL pattern using the PostListView class, as follows:

    urlpatterns = [
        # post views
        # path('', views.post_list, name='post_list'),
        path('', views.PostListView.as_view(), name='post_list'),
        path('<int:year>/<int:month>/<int:day>/<slug:post>/',
            views.post_detail,
            name='post_detail'),
    ]

    In order to keep pagination working, you have to use the right page object that object that is passed to the template. Django's ListView generic view passes the selected page in a variable called `page_obj`,
    so you have to edit your post/list.html template accordingly to include the paginator using the right variable, as follows:

    {% include "pagination.html" with page=page_obj %}

    + Open http://127.0.0.1:8000/blog/ in your browser and verify that everything works the same way as with the previous post_list view. This is a simple example of a class-based view that uses a generic class provided by Django.

    Enhancing Your Blog with Advanced Features

    - Features that i am going to implement are :

    - Sharing posts via email: When readers like an article, they might want to share it with somebody else. You will implement the functionality to share posts via email.
    - Adding comments to a post: Many people want to allow their audience to comment on posts and create discussions. You will let your readers add comments to your blog posts.
    - Tagging posts: Tags allow you to categorize content in a non-hierarchical manner, using simple keywords. You will implement a tagging system, which is a very popular feature for blogs.
    - Recommending similar posts: Once you have a classification method in place, such as a tagging system, you can use it to provide content recommendations to your readers. You will build a
      system that recommends other posts that share tags with a certain blog post.
    - These functionalities will turn your application into a fully featured blog.

    + Sharing posts by email Create a form for users to fill in their name, their email, the email recipient, and optional comments
    + Create a view in the views.py file that handles the posted data and sends the email
    + Add a URL pattern for the new view in the urls.py file of the blog application
    + Create a template to display the form


    + Creating forms with Django
    Let's start by building the form to share posts. Django has a built-in forms framework that allows you to create forms in an easy manner. The forms framework makes it simple to define the fields of your form, specify how they have to be displayed, and indicate how they have to validate input data. The Django forms framework offers a flexible way to render forms and handle data.

    Django comes with two base classes to build forms:

    Form: Allows you to build standard forms
    ModelForm: Allows you to build forms tied to model instances
    First, create a forms.py file inside the directory of your blog application and make it look like this:

    from django import forms

    class EmailPostForm(forms.Form):
        name = forms.CharField(max_length=25)
        email = forms.EmailField()
        to = forms.EmailField()
        comments = forms.CharField(required=False, widget=forms.Textarea)

    NOTE: Forms can reside anywhere in your Django project. The convention is to place them inside a forms.py file for each application.

    - The name field is CharField. This type of field is rendered as an <input type="text"> HTML element. Each field type has a default widget that determines how the field is rendered in HTML.
      The default widget can be overridden with the widget attribute. In the comments field, you use a Textarea widget to display it as a <textarea> HTML element instead of the default <input> element.

    - Field validation also depends on the field type. For example, the email and to fields are EmailField fields. Both fields require a valid email address; the field validation will otherwise raise a
      forms.ValidationError exception and the form will not validate. Other parameters are also taken into account for form validation: you define a maximum length of 25 characters for the name field
      and make the comments field optional with required=False. All of this is also taken into account for field validation.

    Sending emails with Django
    Sending emails with Django is pretty straightforward. First, you need to have a local Simple Mail Transfer Protocol (SMTP) server, or you need to define the configuration of an external SMTP server by
    adding the following settings to the settings.py file of your project:

    EMAIL_HOST: The SMTP server host; the default is localhost
    EMAIL_PORT: The SMTP port; the default is 25

    EMAIL_HOST_USER: The username for the SMTP server
    EMAIL_HOST_PASSWORD: The password for the SMTP server
    EMAIL_USE_TLS: Whether to use a Transport Layer Security (TLS) secure connection
    EMAIL_USE_SSL: Whether to use an implicit TLS secure connection

    If you can't use an SMTP server, you can tell Django to write emails to the console by adding the following setting to the settings.py file:

    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    By using this setting, Django will output all emails to the shell. This is very useful for testing your application without an SMTP server.

    If you want to send emails but you don't have a local SMTP server, you can probably use the SMTP server of your email service provider. The following sample configuration is valid for sending emails via Gmail servers using a Google account:

    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_HOST_USER = 'your_account@gmail.com'
    EMAIL_HOST_PASSWORD = 'your_password'
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True


    Run the python manage.py shell command to open the Python shell and send an email, as follows:

    >>> from django.core.mail import send_mail
    >>> send_mail('Django mail', 'This e-mail was sent with Django.', 'your_account@gmail.com', ['your_account@gmail.com'], fail_silently=False)
    The send_mail() function takes the subject, message, sender, and list of recipients as required arguments. By setting the optional argument fail_silently=False,
    you are telling it to raise an exception if the email couldn't be sent correctly. If the output you see is 1, then your email was successfully sent.

    If you are sending emails using Gmail with the preceding configuration, you will have to enable access for less secure applications at https://myaccount.google.com/lesssecureapps.
    In some cases, you may also have to disable Gmail captcha at https://accounts.google.com/displayunlockcaptcha in order to send emails with Django.

    -> share.html

    {% csrf_token %}
    The {% csrf_token %} template tag introduces a hidden field with an autogenerated token to avoid cross-site request forgery (CSRF) attacks. These attacks consist of a malicious website
    or program performing an unwanted action for a user on your site.

    By default, Django checks for the CSRF token in all POST requests. Remember to include the csrf_token tag in all forms that are submitted via POST.”

    Edit the blog/post/detail.html template and add the following link to the share post URL after the {{ post.body|linebreaks }} variable:

    <p>
      <a href="{% url "blog:post_share" post.id %}">
        Share this post
      </a>
    </p>


    Creating a comment system
    You will build a comment system wherein users will be able to comment on posts. To build the comment system, you need to do the following:

    Create a model to save comments
    Create a form to submit comments and validate the input data
    Add a view that processes the form and saves a new comment to the database
    Edit the post detail template to display the list of comments and the form to add a new comment”

    post = models.ForeignKey(models.Post, on_delete=models.CASCADE, related_name='comments')

    The related_name attribute allows you to name the attribute that you use for the relationship from the related object back to this one. After defining this,
    you can retrieve the post of a comment object using comment.post and retrieve all comments of a post using post.comments.all(). If you don't define the
    related_name attribute, Django will use the name of the model in lowercase, followed by _set (that is, comment_set) to name the relationship of the related
    object to the object of the model, where this relationship has been defined.

    + make the migration for the new model :
    python manage.py makemigrations blog
    python manage.py migrate

    - Creating forms from models
    You still need to build a form to let your users comment on blog posts. Remember that Django has two base classes to build forms: Form and ModelForm. You used the first one previously
    to let your users share posts by email. In the present case, you will need to use ModelForm because you have to build a form dynamically from your Comment model. Edit the forms.py file
    of your blog application and add the following lines:

    from .models import Comment
    class CommentForm(forms.ModelForm):
        class Meta:
            model = Comment
            fields = ('name', 'email', 'body')
    To create a form from a model, you just need to indicate which model to use to build the form in the Meta class of the form. Django introspects the model and builds the form dynamically for you.

    Each model field type has a corresponding default form field type. The way that you define your model fields is taken into account for form validation. By default, Django builds a form field for each field
    contained in the model. However, you can explicitly tell the framework which fields you want to include in your form using a fields list, or define which fields you “want to include in your form using a fields list,
    or define which fields you want to exclude using an exclude list of fields. For your CommentForm form, you will just use the name, email, and body fields, because those are the only fields that your users will be able to fill in.

    Handling ModelForms in views
    You will use the post detail view to instantiate the form and process it, in order to keep it simple. Edit the views.py file, add imports for the Comment model and the CommentForm form, and modify the post_detail view.


    First, you will add the total comments. Open the post/detail.html template and append the following code to the content block:

    {% with comments.count as total_comments %}
      <h2>
        {{ total_comments }} comment{{ total_comments|pluralize }}
      </h2>
    {% endwith %}
    You are using the Django ORM in the template, executing the QuerySet comments.count(). Note that the Django template language doesn't use parentheses for calling methods. The {% with %} tag allows you to assign a value to a new variable that will be available to be used until the {% endwith %} tag.

    The {% with %} template tag is useful for avoiding hitting the database or accessing expensive methods multiple times.
    The pluralize template filter returns a string with the letter "s" if the value is different from 1. The preceding text will be rendered as 0 comments, 1 comment, or N comments. Django includes plenty of template tags and filters that can help you to display information in the way that you want.

    You enumerate comments with the {{ forloop.counter }} variable, which contains the loop counter in each iteration. Then, you display the name of the user who posted the comment, the date, and the body of the comment.

    Adding the tagging functionality

    After implementing your comment system, you need to create a way to tag your posts. You will do this by integrating a third-party Django tagging application into your project. django-taggit is a reusable application that primarily
    offers you a Tag model and a manager to easily add tags to any model.

    “First, you need to install django-taggit via pip by running the following command:

    pip install django_taggit==1.2.0
    Then, open the settings.py file of the mysite project and add taggit to your INSTALLED_APPS setting, as follows:

    INSTALLED_APPS = [
        # ...
        'blog.apps.BlogConfig',
        'taggit',
    ]

    Open the models.py file of your blog application and add the TaggableManager manager provided by django-taggit to the Post model using the following code:

    from taggit.managers import TaggableManager
    class Post(models.Model):
        # ...
        tags = TaggableManager()

    The tags manager will allow you to add, retrieve, and remove tags from Post objects.

    Run the following command to create a migration for your model changes:

    $ python manage.py makemigrations blog

    You should get the following output:

    Migrations for 'blog':
      blog/migrations/0003_post_tags.py
        - Add field tags to post
    Now, run the following command to create the required database tables for django-taggit models and to synchronize your model changes:

    $ python manage.py migrate

    “Let's explore how to use the tags manager. Open the terminal with the python manage.py shell command and enter the following code. First, you will retrieve one of your posts (the one with the 1 ID):

    >>> from blog.models import Post
    >>> post = Post.objects.get(id=1)
    “Then, add some tags to it and retrieve its tags to check whether they were successfully added:

    >>> post.tags.add('music', 'jazz', 'django')
    >>> post.tags.all()

    >>> post.tags.remove('django')
    >>> post.tags.all()

    Now, you need to edit your blog posts to display tags. Open the blog/post/list.html template and add the following HTML code below the post title:
    <p class="tags">Tags: {{ post.tags.all|join:", " }}</p>

    Retrieving posts by similarity

    Now that you have implemented tagging for your blog posts, you can do many interesting things with tags. Tags allow you to categorize posts in a non-hierarchical manner.
    Posts about similar topics will have several tags in common. You will build a functionality to display similar posts by the number of tags they share. In this way, when a user
    reads a post, you can suggest to them that they read other related posts.
    In order to retrieve similar posts for a specific post, you need to perform the following steps:

    1- Retrieve all tags for the current post
    2- Get all posts that are tagged with any of those tags
    3- Exclude the current post from that list to avoid recommending the same post
    4- Order the results by the number of tags shared with the current post
    5- In the case of two or more posts with the same number of tags, recommend the most recent post
    6- Limit the query to the number of posts you want to recommend

    Add the following lines inside the post_detail view before the render() function, with the same indentation level:

    # List of similar posts
    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.published.filter(tags__in=post_tags_ids)\
                                  .exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags'))\
                                .order_by('-same_tags','-publish')[:4]

    The preceding code is as follows:

    You retrieve a Python list of IDs for the tags of the current post. The values_list() QuerySet returns tuples with the values for the given fields.
    You pass flat=True to it to get single values such as [1, 2, 3, ...] instead of one-tuples such as [(1,), (2,), (3,) ...].
    You get all posts that contain any of these tags, excluding the current post itself.
    You use the Count aggregation function to generate a calculated field—same_tags—that contains the number of tags shared with all the tags queried.
    You order the result by the number of shared tags (descending order) and by publish to display recent posts first for the posts with the same number of shared tags.
    You slice the result to retrieve only the first four posts.


    + Extending Your Blog Application :

    - adding a template tag :
    -> /templatetags/blog_tags.py

    Django provides the following helper functions that allow you to create your own template tags in an easy manner:

    simple_tag: Processes the data and returns a string
    inclusion_tag: Processes the data and returns a rendered template


    Before using custom template tags, you have to make them available for the template using the {% load %} tag. As mentioned before, you need to use the name of the Python module
    containing your template tags and filters.

    Open the blog/templates/base.html template and add {% load blog_tags %} at the top of it to load your template tags module. Then, use the tag you created to display your total.
    posts. Just add {% total_posts %} to your template.
    The power of custom template tags is that you can process any data and add it to any template regardless of the view executed. You can perform QuerySets or process any data to display results in your templates.

    Django has a variety of built-in template filters that allow you to alter variables in templates. These are Python functions that take one or two parameters, the value of the variable that the filter is applied to,
    and an optional argument. They return a value that can be displayed or treated by another filter. A filter looks like {{ variable|my_filter }}. Filters with an argument look like {{ variable|my_filter:"foo" }}.
    For example, you can use the capfirst filter to capitalize the first character of the value, like {{ value|capfirst }}. If value is "django", the output will be "Django". You can apply as many filters as you like to a
    variable, for example, {{ variable|filter1|filter2 }}, and each of them will be applied to the output generated by the preceding filter.

    You can find the list of Django's built-in template filters at https://docs.djangoproject.com/en/3.0/ref/templates/builtins/#built-in-filter-reference.

    You will create a custom filter to enable you to use markdown syntax in your blog posts and then convert the post contents to HTML in the templates. Markdown is a plain-text formatting syntax that is very simple to use,
    and it's intended to be converted into HTML. You can write posts using simple markdown syntax and get the content automatically converted into HTML code. Learning markdown syntax is much easier than learning HTML. By using
    markdown, you can get other non-tech savvy contributors to easily write posts for your blog. You can learn the basics of the markdown format at https://daringfireball.net/projects/markdown/basics.

    First, install the Python markdown module via pip using the following command:

    pip install markdown==3.2.1
    Then, edit the blog_tags.py file and include the following code:

    from django.utils.safestring import mark_safe
    import markdown
    @register.filter(name='markdown')
    def markdown_format(text):
        return mark_safe(markdown.markdown(text))

    - Change Filters inside html files :

    Now, load your template tags module in the post list and detail templates. Add the following line at the top of the blog/post/list.html and blog/post/detail.html templates after the {% extends %} tag:

    {% load blog_tags %}
    In the post/detail.html template, look for the following line:

    {{ post.body|linebreaks }}
    Replace it with the following one:

    {{ post.body|markdown }}
    Then, in the post/list.html template, find the following line:

    {{ post.body|truncatewords:30|linebreaks }}
    Replace it with the following one:

    {{ post.body|markdown|truncatewords_html:30 }}
    The truncatewords_html filter truncates a string after a certain number of words, avoiding unclosed HTML tags.

    Now open http://127.0.0.1:8000/admin/blog/post/add/ in your browser and add a post with the following body:

    This is a post formatted with markdown
    --------------------------------------
    *This is emphasized* and **this is more emphasized**.
    Here is a list:
    * One
    * Two
    * Three
    And a [link to the Django website](https://www.djangoproject.com/)


