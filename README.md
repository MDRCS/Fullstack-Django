# Fullstack Django :

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


    Adding a sitemap to your site
    Django comes with a sitemap framework, which allows you to generate sitemaps for your site dynamically.
    A sitemap is an XML file that tells search engines the pages of your website, their relevance, and how
    frequently they are updated. Using a sitemap will make your site more visible in search engine rankings:
    sitemaps help crawlers to index your website's content.

    Edit the settings.py file of your project and add django.contrib.sites and django.contrib.sitemaps to the INSTALLED_APPS setting. Also, define a new setting for the site ID, as follows:

    SITE_ID = 1
    # Application definition
    INSTALLED_APPS = [
        # ...
        'django.contrib.sites',
        'django.contrib.sitemaps',
    ]

    Now run the following command to create the tables of the Django site application in the database:
    python manage.py migrate

    - after adding url_pattern and view and model -> go check http://127.0.0.1:8000/sitemaps.xml

    Adding full-text search to your blog
    Next, you will add search capabilities to your blog. Searching for data in the database with user input is a common task for web applications. The Django ORM allows you to perform simple matching operations using, for example, the contains filter (or its case-insensitive version, icontains). You can use the following query to find posts that contain the word framework in their body:

    from blog.models import Post
    Post.objects.filter(body__contains='framework')

    You also need to install the psycopg2 PostgreSQL adapter for Python. Run the following command in the shell to install it:

    pip install psycopg2-binary==2.8.4
    Let's create a user for your PostgreSQL database. Open the shell and run the following commands:

    psql postgres
    CREATE USER blog WITH ENCRYPTED PASSWORD 'yourpass';
    You will be prompted for a password for the new user. Enter the desired password and then create the blog database and give ownership to the blog user you just created with the following command:

    CREATE DATABASE blog ENCODING 'UTF8' OWNER=blog;

    - because we user a new database we should create a new superuser :
    + create a superuser :

    $ python manage.py createsuperuser

    Now you can search against a single field using the search QuerySet lookup, like this:

    from blog.models import Post
    Post.objects.filter(body__search='django')
    This query uses PostgreSQL to create a search vector for the body field and a search query from the term django. Results are obtained by matching the query with the vector.

    Searching against multiple fields
    You might want to search against multiple fields. In this case, you will need to define a SearchVector object. Let's build a vector that allows you to search against the title and body fields of the Post model:

    from django.contrib.postgres.search import SearchVector
    from blog.models import Post
    Post.objects.annotate(
        search=SearchVector('title', 'body'),
    ).filter(search='django')

    + Stemming and ranking results :

    Stemming is the process of reducing words to their word stem, base, or root form. Stemming is used by search engines to reduce indexed words to their stem, and to be able to match inflected or derived words.
    For example, "music" and "musician" can be considered similar words by a search engine.
    Django provides a SearchQuery class to translate terms into a search query object. By default, the terms are passed through stemming algorithms, which helps you to obtain better matches. You also want to order
    results by relevancy. PostgreSQL provides a ranking function that orders results based on how often the query terms appear and how close together they are.

    Weighting queries
    You can boost specific vectors so that more weight is attributed to them when ordering results by relevancy. For example, you can use this to give more relevance to posts that are matched by title rather than by content.

    Edit the previous lines of the views.py file of your blog application and make them look like this:

    search_vector = SearchVector('title', weight='A') + \
                    SearchVector('body', weight='B')
    search_query = SearchQuery(query)
    results = Post.published.annotate(
     rank=SearchRank(search_vector, search_query)
     ).filter(rank__gte=0.3).order_by('-rank')
    In the preceding code, you apply different weights to the search vectors built using the title and body fields. The default weights are D, C, B, and A, and they refer to the numbers 0.1, 0.2, 0.4, and 1.0, respectively. You apply a weight of 1.0 to the title search vector and a weight of 0.4 to the body vector. Title matches will prevail over body content matches. You filter the results to display only the ones with a rank higher than 0.3.

    Searching with trigram similarity
    Another search approach is trigram similarity. A trigram is a group of three consecutive characters. You can measure the similarity of two strings by counting the number of trigrams that they share. This approach turns out to be very effective for measuring the similarity of words in many languages.

    In order to use trigrams in PostgreSQL, you will need to install the pg_trgm extension first. Execute the following command from the shell to connect to your database:

    psql blog
    Then, execute the following command to install the pg_trgm extension:

    CREATE EXTENSION pg_trgm;
    Let's edit your view and modify it to search for trigrams. Edit the views.py file of your blog application and add the following import:

    from django.contrib.postgres.search import TrigramSimilarity
    Then, replace the Post search query with the following lines:

    results = Post.published.annotate(
        similarity=TrigramSimilarity('title', query),
    ).filter(similarity__gt=0.1).order_by('-similarity')

### + Building a Social Network Website

    This chapter will cover the following topics:

    $ Using the Django authentication framework
    $ Creating user registration views
    $ Extending the user model with a custom profile model
    $ Adding social authentication with Python Social Auth

    Creating a social website project
    You are going to create a social application that will allow users to share images that they find on the Internet.
    You will need to build the following elements for this project:

    An authentication system for users to register, log in, edit their profile, and change or reset their password
    A follow system to allow users to follow each other on the website
    A functionality to display shared images and implement a bookmarklet for users to share images from any website
    An activity stream that allows users to see the content uploaded by the people that they follow

    “Starting your social website project
    Open the terminal and use the following commands to create a virtual environment for your project and activate it:

    mkdir env
    python3 -m venv env/bookmarks
    source env/bookmarks/bin/activate

    The shell prompt will display your active virtual environment, as follows:

    (bookmarks)laptop:~ zenx$
    Install Django in your virtual environment with the following command:

    pip install Django==3.0.*
    Run the following command to create a new project:

    django-admin startproject bookmarks
    The initial project structure has been created. Use the following commands to get into your project directory and create a new application named account:

    cd bookmarks/
    django-admin startapp account
    Remember that you should add the new application to your project by adding the application's name to the INSTALLED_APPS setting in the settings.py file. Place it in the INSTALLED_APPS list before any of the other installed apps:

    INSTALLED_APPS = [
        'account.apps.AccountConfig',
        # ...
    ]

    python manage.py migrate

    - Django comes with a built-in authentication framework that can handle user authentication, sessions, permissions, and user groups. The authentication system includes views for common user actions such as log in, log out, password change, and password reset.

    The authentication framework also includes the following models:

    User: A user model with basic fields; the main fields of this model are username, password, email, first_name, last_name, and is_active
    Group: A group model to categorize users
    Permission: Flags for users or groups to perform certain actions.

    Django includes several forms and views in the authentication framework that you can use right away. The login view you have created is a good exercise to understand the process of user authentication in Django.
    However, you can use the default Django authentication views in most cases.

    Django provides the following class-based views to deal with authentication. All of them are located in django.contrib.auth.views:

    LoginView: Handles a login form and logs in a user
    LogoutView: Logs out a user
    Django provides the following views to handle password changes:

    PasswordChangeView: Handles a form to change the user's password
    PasswordChangeDoneView: The success view that the user is redirected to after a successful password change
    Django also includes the following views to enable users to reset their password:

    PasswordResetView: Allows users to reset their password. It generates a one-time-use link with a token and sends it to a user's email account.
    PasswordResetDoneView: Tells users that an email—including a link to reset their password—has been sent to them.
    PasswordResetConfirmView: Allows users to set a new password.
    PasswordResetCompleteView: The success view that the user is redirected to after successfully resetting their password.

    Edit the settings.py file of your project and add the following code to it:

    LOGIN_REDIRECT_URL = 'dashboard'
    LOGIN_URL = 'login'
    LOGOUT_URL = 'logout'
    The settings defined in the preceding code are as follows:

    LOGIN_REDIRECT_URL: Tells Django which URL to redirect the user to after a successful login if no next parameter is present in the request
    LOGIN_URL: The URL to redirect the user to log in (for example, views using the login_required decorator)
    LOGOUT_URL: The URL to redirect the user to log out

    You are using the names of the URL patterns that you previously defined using the name attribute of the path() function. Hardcoded URLs instead of URL names can also be used for these settings.”

    try to login using this url -> after login you will be redirected to account html pages and not admin ones.
    http://127.0.0.1:8000/account/login/?next=/account/

    social network platform login :

    Several social services will not allow redirecting users to 127.0.0.1 or localhost after a successful authentication; they expect a domain name. In order to make social authentication work, you will need a domain. To fix this on Linux or macOS, edit your /etc/hosts file and add the following line to it:

    $ sudo vi /etc/hosts
    $ add this line -> 127.0.0.1 mysite.com

    Edit the settings.py file of your project and edit the ALLOWED_HOSTS setting as follows:

    ALLOWED_HOSTS = ['mysite.com', 'localhost', '127.0.0.1']
    Besides the mysite.com host, you explicitly include localhost and 127.0.0.1. This is in order to be able to access the site through localhost, which is the default Django behavior when DEBUG is True and ALLOWED_HOSTS is empty. Now you should be able to open http://mysite.com:8000/account/login/ in your browser.”

    Running the development server through HTTPS
    Some of the social authentication methods you are going to use require an HTTPS connection. The Transport Layer Security (TLS) protocol is the standard for serving websites through a secure connection. The TLS predecessor is the Secure Sockets Layer (SSL).
    Although SSL is now deprecated, in multiple libraries and online documentation you will find references to both the terms TLS and SSL. The Django development server is not able to serve your site through HTTPS, since that is not its intended use. In ”

    order to test the social authentication functionality serving your site through HTTPS, you are going to use the RunServerPlus extension of the package Django Extensions. Django Extensions is a third-party collection of custom extensions for Django. Please note that this is never the method you should use to serve your site in a real environment; this is a development server.

    Use the following command to install Django Extensions:

    pip install django-extensions==2.2.5
    Now you need to install Werkzeug, which contains a debugger layer required by the RunServerPlus extension. Use the following command to install it:

    pip install werkzeug==0.16.0
    Finally, use the following command to install pyOpenSSL, which is required to use the SSL/TLS functionality of RunServerPlus:

    pip install pyOpenSSL==19.0.0
    Edit the settings.py file of your project and add Django Extensions to the INSTALLED_APPS setting, as follows:

    INSTALLED_APPS = [
        # ...
        'django_extensions',
    ]
    Use the management command runserver_plus provided by Django Extensions to run the development server, as follows:

    python manage.py runserver_plus --cert-file cert.crt
    You provide a file name to the runserver_plus command for the SSL/TLS certificate. Django Extensions will generate a key and certificate automatically.

    Open https://mysite.com:8000/account/login/ in your browser. Now you[…]”

    pip install social-auth-app-django
    pip install django-extensions==2.2.5
    pip install werkzeug==0.16.0
    pip install pyOpenSSL==19.0.0
    pip install Pillow

![](./social-logins/fb-1.png)
![](./social-logins/fb-2.png)
![](./social-logins/fb-3.png)
![](./social-logins/fb-4.png)
![](./social-logins/fb-5.png)
![](./social-logins/twitter-1.png)
![](./social-logins/twitter-2.png)
![](./social-logins/twitter-3.png)
![](./social-logins/twitter-4.png)
![](./social-logins/google-1.png)
![](./social-logins/google-2.png)
![](./social-logins/google-3.png)
![](./social-logins/google-4.png)
![](./social-logins/google-5.png)
![](./social-logins/google-6.png)

    # run the server using a certificate ssl self-generated :
    python manage.py runserver_plus --cert-file cert.crt

    - Sharing Content on Your Website :

    Creating an image bookmarking website

    In this chapter, you will learn how to allow users to bookmark and share images that they find on other websites and on your site. For this, you will need to do the following tasks:

    Define a model to store images and their information
    Create a form and a view to handle image uploads
    Build a system for users to be able to post images that they find on external websites
    First, create a new application inside your bookmarks project directory with the following command:

    django-admin startapp images

    Creating many-to-many relationships
    Next, you will add another field to the Image model to store the users who like an image. You will need a many-to-many relationship in this case because a user might like multiple images and each image can be liked by multiple users.

    python manage.py makemigrations images
    python manage.py migrate images

    python manage.py runserver_plus --cert-file cert.crt

    Posting content from other websites
    You will allow users to bookmark images from external websites. The user will provide the URL of the image, a title, and an optional description. Your application will download the image and create a new Image object in the database.

    Users will not enter the image URL directly in the form. Instead, you will provide them with a JavaScript tool to choose an image from an external site, and your form will receive its URL as a parameter.

    In order to use the urllib to retrieve images from URLs served through HTTPS, you need to install the Certifi Python package. Certifi is a collection of root certificates for validating the trustworthiness of SSL/TLS certificates.

    Install certifi with the following command:

    pip install --upgrade certifi


    https://127.0.0.1:8000/images/create/?title=%20Django%20and%20Duke&url=https://upload.wikimedia.org/wikipedia/commons/8/85/Django_Reinhardt_and_Duke_Ellington_%28Gottlieb%29.jpg

    + Building a bookmarklet with jQuery

    - This is how your users will add a bookmarklet to their browser and use it:

    The user drags a link from your site to their browser's bookmarks. The link contains JavaScript code in its href attribute. This code will be stored in the bookmark.
    The user navigates to any website and clicks on the bookmark. The JavaScript code of the bookmark is executed.”

    For security reasons, your browser will prevent you from running the bookmarklet over HTTP on a site served through HTTPS. You will need to be able to load the bookmarklet on any site, including sites secured through HTTPS. To run your development server using an auto-generated SSL/TLS certificate, you will use RunServerPlus from Django Extensions, which you installed in the previous chapter.

    Run the RunServerPlus development server with the following command:

    python manage.py runserver_plus --cert-file cert.crt
    Open https://127.0.0.1:8000/account/ in your browser.

    pip install easy-thumbnails==2.7

    Creating image thumbnails using easy-thumbnails

    You are displaying the original image on the detail page, but dimensions for different images may vary considerably. Also, the original files for some images may be huge, and loading them might take too long. The best way to display optimized images in a uniform way is to generate thumbnails. Let's use a Django application called easy-thumbnails for this purpose.

    Open the terminal and install easy-thumbnails using the following command:

    pip install easy-thumbnails==2.7
    Edit the settings.py file of the bookmarks project and add easy_thumbnails to the INSTALLED_APPS setting, as follows:

    INSTALLED_APPS = [
        # ...
        'easy_thumbnails',
    ]
    Then, run the following command to sync the application with your database:

    python manage.py migrate

    The easy-thumbnails application offers several options to customize your thumbnails, including cropping algorithms and different effects that can be applied.
    If you have any difficulty generating thumbnails, you can add THUMBNAIL_DEBUG = True to the settings.py file in order to obtain debug information. You can
    read the full documentation of easy-thumbnails at https://easy-thumbnails.readthedocs.io/.

    - Likes Feature :

    + Adding AJAX actions with jQuery :
    You are going to add a link to the image detail page to let users click on it in order to like an image. You will perform this action
    with an AJAX call to avoid reloading the whole page.


    - Explaining List_ajax for infinite scrolling / pagination :

    You define the following variables:
    page: Stores the current page number.
    empty_page: Allows you to know whether the user is on the last page and retrieves an empty page. As soon as you get an empty page, you will stop sending additional AJAX requests because you will assume that there are no more results.
    block_request: Prevents you from sending additional requests while an AJAX request is in progress.
    You use $(window).scroll() to capture the scroll event and also to define a handler function for it.
    You calculate the margin variable to get the difference between the total document height and the window height, because that's the height of the remaining content for the user to scroll. You subtract a value of 200 from the result so
    that you load the next page when the user is closer than 200 pixels to the bottom of the page.
    You only send an AJAX request if no other AJAX request is being done (block_request has to be false) and the user didn't get to the last page of results (empty_page is also false).
    You set block_request to true to avoid a situation where the scroll event triggers additional AJAX requests, and increase the page counter by one, in order to retrieve the next page.
    You perform an AJAX GET request using $.get() and receive the HTML response in a variable called data. The following are the two scenarios:
    The response has no content: You got to the end of the results, and there are no more pages to load. You set empty_page to true to prevent additional AJAX requests.
    The response contains data: You append the data to the HTML element with the image-list ID. The page content expands vertically, appending results when the user approaches the bottom of the page.”

    Tracking User Actions

    Building a follow system

    Let's build a follow system in your project. This means that your users will be able to follow each other and track what other users share on the platform. The relationship between users is a many-to-many relationship: a user can follow multiple users and they, in turn, can be followed by multiple users.

    - Using signals for denormalizing counts

    There are some cases when you may want to denormalize your data. Denormalization is making data redundant in such a way that it optimizes read performance. For example, you might be copying related data to an object to avoid expensive read queries to the database when retrieving the related data. You have to be careful about denormalization and only start using it when you really need it. The biggest issue you will find with denormalization is that it's difficult to keep your denormalized data updated.
    Let's take a look at an example of how to improve your queries by denormalizing counts. You will denormalize data from your Image model and use Django signals to keep the data updated.

    Working with signals
    Django comes with a signal dispatcher that allows receiver functions to get notified when certain actions occur. Signals are very useful when you need your code to do something every time something else happens. Signals allow you to decouple logic: you can capture a certain action, regardless of the application or code that triggered that action, and implement logic that gets executed whenever that action occurs. For example, you can build a signal[…]”

    Storing item views in Redis
    Let's find a way to store the total number of times an image has been viewed. If you implement this using the Django ORM, it will involve a SQL UPDATE query every time an image is displayed. If you use Redis instead, you just need to increment a counter stored in memory, resulting in a much better performance and less overhead.”

    def image_detail(request, id, slug):
        image = get_object_or_404(Image, id=id, slug=slug)
        # increment total image views by 1
        total_views = r.incr(f'image:{image.id}:views')
        # increment image ranking by 1
        r.zincrby('image_ranking', 1, image.id)
        return render(request,
                      'images/image/detail.html',
                      {'section': 'images',
                       'image': image,
                       'total_views': total_views})

    You use the zincrby() command to store image views in a sorted set with the image:ranking key. You will store the image id and a related score of 1, which will be added to the total score of this element in the sorted set. This will allow you to keep track of all image views globally and have a sorted set ordered by the total number of views.”

    “Now, create a new view to display the ranking of the most viewed images. Add the following code to the views.py file of the images application:

    @login_required
    def image_ranking(request):
        # get image ranking dictionary
        image_ranking = r.zrange('image_ranking', 0, -1,
                                 desc=True)[:10]
        image_ranking_ids = [int(id) for id in image_ranking]
        # get most viewed images
        most_viewed = list(Image.objects.filter(
                               id__in=image_ranking_ids))
        most_viewed.sort(key=lambda x: image_ranking_ids.index(x.id))
        return render(request,
                      'images/image/ranking.html',
                      {'section': 'images',
                       'most_viewed': most_viewed})
    The image_ranking view works like this:

    You use the zrange() command to obtain the elements in the sorted set. This command expects a custom range according to the lowest and highest score. Using 0 as the lowest and -1 as the highest score, you are telling Redis to return all elements in the sorted set. You also specify desc=True to retrieve the elements ordered by descending score. Finally, you slice the results using [:10] to get the first 10 elements with the highest score.
    You build a list of returned image IDs and store it in the image_ranking_ids variable as a list of integers. You retrieve the Image objects for those IDs and force the query to be executed using the list() function. It[…]”

    the image ranking. Now you can use the most_viewed list in your template to display the 10 most viewed images.”

    ++ use cases of REDIS :

    Redis is not a replacement for your SQL database, but it does offer fast in-memory storage that is more suitable for certain tasks. Add it to your stack and use it when you really feel it's needed. The following are some scenarios in which Redis could be useful:
    Counting: As you have seen, it is very easy to manage counters with Redis. You can use incr() and incrby() for counting stuff.”
    Storing latest items: You can add items to the start/end of a list using lpush() and rpush(). Remove and return the first/last element using lpop() / rpop(). You can trim the list's length using ltrim() to maintain its length.
    Queues: In addition to push and pop commands, Redis offers the blocking of queue commands.
    Caching: Using expire() and expireat() allows you to use Redis as a cache. You can also find third-party Redis cache backends for Django.
    Pub/sub: Redis provides commands for subscribing/unsubscribing and sending messages to channels.
    Rankings and leaderboards: Redis sorted sets with scores make it very easy to create leaderboards.
    Real-time tracking: Redis's fast I/O makes it perfect for real-time scenarios.

    - Building a shopping cart :

    After building the product catalog, the next step is to create a shopping cart so that users can pick the products that they want to purchase. A shopping cart allows users to select products and set the amount they want to order, and then store this information temporarily while they browse the site, until they eventually place an order. The cart has to be persisted in the session so that the cart items are maintained during a user's visit.
    You will use Django's session framework to persist the cart. The cart will be kept in the session until it finishes or the user checks out of the cart. You will also need to build additional Django models for the cart and its items.”

    To use sessions, you have to make sure that the MIDDLEWARE setting of your project contains 'django.contrib.sessions.middleware.SessionMiddleware'. This middleware manages sessions. It's added by default to the MIDDLEWARE setting when you create a new project using the startproject command.

    - Using Django sessions
    Django provides a session framework that supports anonymous and user sessions. The session framework allows you to store arbitrary data for each visitor. Session data is stored on the server side, and cookies contain the session ID unless you use the cookie-based session engine. The session middleware manages the sending and receiving of cookies.
    The default session engine stores session data in the database, but you can choose other session engines.

    When users log in to the site, their anonymous session is lost and a new session is created for authenticated users. If you store items in an anonymous session that you need to keep after the user logs in, you will have to copy the old session data into the new session. You can do this by retrieving the session data before you log in the user using the login()
    function of the Django authentication system and storing it in the session after that.

    Session settings
    There are several settings you can use to configure sessions for your project. The most important is SESSION_ENGINE. This setting allows you to set the place where sessions are stored. By default, Django stores sessions in the database using the Session model of the django.contrib.sessions application.

    Django offers the following options for storing session data:

    Database sessions: Session data is stored in the database. This is the default session engine.
    File-based sessions: Session data is stored in the filesystem.
    Cached sessions: Session data is stored in a cache backend. You can specify cache backends using the CACHES setting. Storing session data in a cache system provides the best performance.
    Cached database sessions: Session data is stored in a write-through cache and database. Reads only use the database if the data is not already in the cache.
    Cookie-based sessions: Session data is stored in the cookies that are sent to the browser.”

    For better performance use a cache-based session engine. Django supports Memcached out of the box and you can find third-party cache backends for Redis and other cache systems.

    You can customize sessions with specific settings. Here are some of the important session-related settings:

    SESSION_COOKIE_AGE: The duration of session cookies in seconds. The default value is 1209600 (two weeks).
    SESSION_COOKIE_DOMAIN: The domain used for session cookies. Set this to mydomain.com to enable cross-domain cookies or use None for a standard domain cookie.
    SESSION_COOKIE_SECURE: A Boolean indicating that the cookie should only be sent if the connection is an HTTPS connection.
    SESSION_EXPIRE_AT_BROWSER_CLOSE: A Boolean indicating that the session has to expire when the browser is closed.
    SESSION_SAVE_EVERY_REQUEST: A Boolean that, if True, will save the session to the database on every request. The session expiration is also updated each time it's saved.
    You can see all the session settings and their default values at https://docs.djangoproject.com/en/3.0/ref/settings/#sessions.

    Session expiration
    You can choose to use browser-length sessions or persistent sessions using the SESSION_EXPIRE_AT_BROWSER_CLOSE setting. This is set to False by default,
    forcing the session duration to the value stored in the SESSION_COOKIE_AGE setting. If you set SESSION_EXPIRE_AT_BROWSER_CLOSE to True, the session will
    expire when the user closes the browser, and the SESSION_COOKIE_AGE setting will not have any effect.

    Storing shopping carts in sessions
    You need to create a simple structure that can be serialized to JSON for storing cart items in a session. The cart has to include the following data for each item contained in it:

    The ID of a Product instance
    The quantity selected for the product
    The unit price for the product

    Since product prices may vary, let's take the approach of storing the product's price along with the product itself when it's added

    to the cart. By doing so, you use the current price of the product when users add it to their cart, no matter whether the product's price is changed afterwards. This means that the price that the item has when the client adds it to the cart is maintained for that client in the session until checkout is completed or the session finishes.

    Next, you have to build functionality to create shopping carts and associate them with sessions. This has to work as follows:

    When a cart is needed, you check whether a custom session key is set. If no cart is set in the session, you create a new cart and save it in the cart session key.
    For successive requests, you perform the same check and get the cart items from the cart session key. You retrieve the cart items from the session and their related Product objects from the database.
    Edit the settings.py file of your project and add the following setting to it:

    CART_SESSION_ID = 'cart'
    This is the key that you are going to use to store the cart in the user session. Since Django sessions are managed per visitor, you can use the same


    Creating shopping cart views
    Now that you have a Cart class to manage the cart, you need to create the views to add, update, or remove items from it. You need to create the following views:

    A view to add or update items in the cart that can handle current and new quantities
    A view to remove items from the cart
    A view to display cart items and totals

    ** Creating a context processor for the current cart
    You might have noticed that the message Your cart is empty is displayed in the header of the site, even when the cart contains items. You should display the total number of
    items in the cart and the total cost instead. Since this has to be displayed on all pages, you need to build a context processor to include the current cart in the request context, regardless of the view that processes the request.

    Context processors

    A context processor is a Python function that takes the request object as an argument and returns a dictionary that gets added to the request context. Context processors come in handy when you need to make something available globally to all templates.

    By default, when you create a new project using the startproject command, your project contains the following template context processors in the context_processors option inside the TEMPLATES setting:

    django.template.context_processors.debug: This sets the Boolean debug and sql_queries variables in the context, representing the list of SQL queries executed in the request
    django.template.context_processors.request: This sets the request variable in the context
    django.contrib.auth.context_processors.auth: This sets the user variable in the request
    django.contrib.messages.context_processors.messages: This sets a messages variable in the context containing all the messages that have been generated using the messages framework
    Django also enables django.template.context_processors.csrf to avoid cross-site request forgery (CSRF) attacks. This context processor is not present in the settings, but it is always enabled and can't be turned off for security reasons.”


    Context processors are executed in all the requests that use RequestContext. You might want to create a custom template tag instead of a context processor if your functionality
    is not needed in all templates, especially if it involves database queries.

    Registering customer orders
    When a shopping cart is checked out, you need to save an order into the database. Orders will contain information about customers and the products they are buying.

    Creating customer orders
    You will use the order models that you created to persist the items contained in the shopping cart when the user finally places an order. A new order will be created following these steps:

    Present a user with an order form to fill in their data
    Create a new Order instance with the data entered, and create an associated OrderItem instance for each item in the cart
    Clear all the cart's contents and redirect the user to a success page

    Launching asynchronous tasks with Celery

    Everything you execute in a view affects response times. In many situations, you might want to return a response to the user as quickly as possible and let the server execute some process
    asynchronously. This is especially relevant for time-consuming processes or processes subject to failure, which might need a retry policy. For example, a video sharing platform allows users
    to upload videos but requires a long time to transcode uploaded videos. The site might return a response to users to inform them that the transcoding will start soon, and start transcoding
    the video asynchronously. Another example is sending emails to users. If your site sends email notifications from a view, the Simple Mail Transfer Protocol (SMTP) connection might fail or slow down the response.
    Launching asynchronous tasks is essential to avoid blocking the code execution.
    Celery is a distributed task queue that can process vast amounts of messages. Using Celery, not only can you create asynchronous tasks easily and let them be executed by workers as soon as possible, but you can
    also schedule them to run at a specific time.

    pip install celery==4.4.2

    Celery requires a message broker in order to handle requests from an external source. A message broker is used to translate messages to a formal messaging protocol and manage message queues for multiple receivers,
    providing reliable storage and guaranteed message delivery. You use a message broker to send messages to Celery workers, which process tasks as they receive them.

    - Setting up RabbitMQ :
    brew install rabbitmq
    rabbitmq-server start
    brew services start rabbitmq
    brew services list

    + url to access to Rabbitmq -> http://localhost:15672/
    + login -> guest/guest

    Finally, you tell Celery to auto-discover asynchronous tasks for your applications. Celery will look for a tasks.py file in each application directory of applications added to INSTALLED_APPS in order to load asynchronous tasks defined in it.
    You need to import the celery module in the __init__.py file of your project to make sure it is loaded when Django starts. Edit the myshop/__init__.py file and add the following code to it:

    # import celery
    from .celery import app as celery_app
    Now you can start programming asynchronous tasks for your applications.

    The CELERY_ALWAYS_EAGER setting allows you to execute tasks locally in a synchronous way, instead of sending them to the queue. This is useful for running unit tests or executing the application in your local environment without running Celery.

    Adding asynchronous tasks to your application
    Next, you are going to create an asynchronous task to send an email notification to your users when they place an order.

    convention is to include asynchronous tasks for your application in a tasks module within your application directory.

    ++ Use asynchronous tasks not only for time-consuming processes, but also for other processes that do not take so much time to be executed but which are subject to connection failures or require a retry policy.

    in views.py OrderCreate add :
    OrderCreated.delay(order.id)

    You call the delay() method of the task to execute it asynchronously. The task will be added to the queue and will be executed by a worker as soon as possible.”

    to launch a celery worker run -> celery -A online_shop worker -l info

    Monitoring Celery
    You might want to monitor the asynchronous tasks that are executed. Flower is a web-based tool for monitoring Celery. You can install Flower using this command:

    pip install flower==0.9.3
    Once installed, you can launch Flower by running the following command from your project directory:

    celery -A online_shop flower
    Open http://localhost:5555/dashboard in your browser.

    Summary
    In this chapter, you created a basic shop application. You made a product catalog and built a shopping cart using sessions. You implemented a custom context processor to make
    the cart available to your templates and created a form for placing orders. You also learned how to launch asynchronous tasks with Celery.
    In the next chapter, you will discover how to integrate a payment gateway into your shop, add custom actions to the administration site, export data in CSV format, and generate PDF files dynamically.

    Managing Payments and Orders
    In this chapter, you will learn how to integrate a payment gateway into your site to let users pay by credit card. You will also extend the administration site with different features.

    In this chapter, you will:

    Integrate a payment gateway into your project
    Export orders to CSV files
    Create custom views for the administration site
    Generate PDF invoices dynamically

    Integrating a payment gateway
    A payment gateway allows you to process payments online. Using a payment gateway, you can manage customers' orders and delegate payment processing to a reliable, secure third party. You won't have to worry about processing credit cards in your own system.

    Braintree provides an API that allows you to process online payments with multiple payment methods, such as credit card, PayPal, Google Pay, and Apple Pay. You can learn more about Braintree at https://www.braintreepayments.com/.

    Installing the Braintree Python module
    Braintree provides a Python module that simplifies dealing with its API. You are going to integrate the payment gateway into your project using the braintree module.

    Install the braintree module from the shell using the following command:

    $ pip install braintree==3.59.0
    Add the following settings to the settings.py file of your project:

    # Braintree settings
    BRAINTREE_MERCHANT_ID = 'XXX'  # Merchant ID
    BRAINTREE_PUBLIC_KEY = 'XXX'   # Public Key
    BRAINTREE_PRIVATE_KEY = 'XXX'  # Private key
    import braintree
    BRAINTREE_CONF = braintree.Configuration(
        braintree.Environment.Sandbox,
        BRAINTREE_MERCHANT_ID,
        BRAINTREE_PUBLIC_KEY,
        BRAINTREE_PRIVATE_KEY
    )

    Replace the BRAINTREE_MERCHANT_ID, BRAINTREE_PUBLIC_KEY, and BRAINTREE_PRIVATE_KEY values with the ones for your account.

    You use Environment.Sandbox for integrating the sandbox. Once you go live and create a real account, you will need to change this to Environment.Production. Braintree will provide you with a new merchant ID and private/public keys
    for the production environment. In Chapter 14, Going Live, you will learn how to configure settings for multiple environments.

    The checkout process will work as follows:

    1- Add items to the shopping cart
    2- Check out the shopping cart
    3- Enter credit card details and pay

    Integrating Braintree using Hosted Fields

    The Hosted Fields integration allows you to create your own payment form using custom styles and layouts. An iframe is added dynamically to the page using the Braintree JavaScript software development kit (SDK). The iframe includes the Hosted Fields payment form. When the customer submits the form, Hosted Fields collects the card details securely and attempts to tokenize them. If tokenization succeeds, you can send the generated token nonce to your view to make a transaction using the Python braintree module. A token nonce is a secure, one-time-use reference to payment information. It allows you to send sensitive payment information to Braintree without touching the raw data.

    Let's create a view for processing payments. The whole checkout process will work as follows:

    In the view, a client token is generated using the braintree Python module. This token is used in the next step to instantiate the Braintree JavaScript client; it's not the payment token nonce.
    The view renders the checkout template. The template loads the Braintree JavaScript SDK using the client token and generates the iframe with the hosted payment form fields.
    Users enter their credit card details and submit the form, A payment token nonce is generated with the Braintree JavaScript client. You send the token to your view with a POST request.
    The payment view receives the token nonce and you use it to generate a transaction using the braintree Python module.

    These are especially useful to know why a transaction might have been declined. You can obtain a response code using result.transaction.processor_response_code and its associated response text using result.transaction.processor_response_text. You can find the list of payment
    authorization responses at https://developers.braintreepayments.com/reference/general/processor-responses/authorization-responses.

    - Remember ! :

    -- Going live --
    Once you have tested your environment, you can create a real Braintree account at https://www.braintreepayments.com. Once you are ready to move into production, remember to change your live environment credentials in the settings.py file of your project and use braintree.Environment.Production
    to set up your environment. All steps to go live are summarized at https://developers.braintreepayments.com/start/go-live/python.

    Exporting orders to CSV files
    Sometimes, you might want to export the information contained in a model to a file so that you can import it in another system. One of the most widely used formats to export/import data is comma-separated values (CSV). A CSV file is a plain text file consisting of a number of records.
    There is usually one record per line and some delimiter character, usually a literal comma, separating the record fields. You are going to customize the administration site to be able to export orders to CSV files.

    You are going to create a custom administration action to download a list of orders as a CSV file. Edit the admin.py file of the orders application and add the following code before the OrderAdmin class. "csv code'

    Extending the administration site with custom views

    Sometimes, you may want to customize the administration site beyond what is possible through configuring ModelAdmin, creating administration actions, and overriding administration templates. You might want to implement additional functionalities that are not available in existing administration views or
    templates. If this is the case, you need to create a custom administration view. With a custom view, you can build any functionality you want; you just have to make sure that only staff users can access your view and that you maintain the administration look and feel by making your template extend an administration template.
    Let's create a custom view to display information about an order. Edit the views.py file of the orders application and add the following code to it

    This is the template to display the details of an order on the administration site. This template extends the admin/base_site.html template of Django's administration site, which contains the main HTML structure and CSS styles.
    brew install python cairo pango gdk-pixbuf libxml2 libxslt libffi
    pip install WeasyPrint==51

    + Generate Static files :
    $ python manage.py collectstatic

    The collectstatic command copies all static files from your applications into the directory defined in the STATIC_ROOT setting. This allows each application to provide its own static files using a static/ directory containing them.
    You can also provide additional static files sources in the STATICFILES_DIRS

    Sending PDF files by email
    When a payment is successful, you will send an automatic email to your customer including the generated PDF invoice. You will create an asynchronous task to perform this action.

    Extending Your Shop

    In this chapter, you will add a coupon system to your shop. You will also learn how internationalization and localization work, and you will build a recommendation engine.

    This chapter will cover the following points:

    Creating a coupon system to apply discounts
    Adding internationalization to your project
    Using Rosetta to manage translations
    Translating models using django-parler
    Building a product recommendation engine

    Creating a coupon system

    Many online shops give out coupons to customers that can be redeemed for discounts on their purchases. An online coupon usually consists of a code that is given to users and is valid for a specific time frame.
    You are going to create a coupon system for your shop. Your coupons will be valid for customers in a certain time frame. The coupons will not have any limitations in terms of the number of times they can be redeemed, and they will be applied
    to the total value of the shopping cart. For this functionality, you will need to create a model to store the coupon code, a valid time frame, and the discount to apply.

    Applying a coupon to the shopping cart
    You can store new coupons and make queries to retrieve existing coupons. Now you need a way for customers to apply coupons to their purchases. The functionality to apply a coupon would be as follows:

    1- The user adds products to the shopping cart.
    2- The user can enter a coupon code in a form displayed on the shopping cart detail page.
    3- When the user enters a coupon code and submits the form, you look for an existing coupon with the given code that is currently valid. You have to check that the coupon code matches the one entered by the user, that the active attribute is True, and that the current datetime is between the valid_from and valid_to values.
    4- If a coupon is found, you save it in the user's session and display the cart, including the discount applied to it and the updated total amount.
    5- When the user places an order, you save the coupon to the given order.

    Adding internationalization and localization

    Django offers full internationalization and localization support. It allows you to translate your application into multiple languages and it handles locale-specific formatting for dates, times, numbers, and timezones. Let's clarify the difference between internationalization and localization. Internationalization (frequently abbreviated to i18n)
    is the process of adapting software for the potential use of different languages and locales, so that it isn't hardwired to a specific language or locale. Localization (abbreviated to l10n) is the process of actually translating the software and adapting it to a particular locale. Django itself is translated into more than 50 languages using its internationalization framework.

    Internationalization and localization settings

    Django provides several settings for internationalization. The following settings are the most relevant ones:

    USE_I18N: A Boolean that specifies whether Django's translation system is enabled. This is True by default.
    USE_L10N: A Boolean indicating whether localized formatting is enabled. When active, localized formats are used to represent dates and numbers. This is False by default.
    USE_TZ: A Boolean that specifies whether datetimes are timezone-aware. When you create a project with the startproject command, this is set to True.
    LANGUAGE_CODE: The default language code for the project. This is in standard language ID format, for example, 'en-us' for American English, or 'en-gb' for British English. This setting requires USE_I18N to be set to True in order to take effect. You can find a list of valid

    language IDs at http://www.i18nguy.com/unicode/language-identifiers.html.
    LANGUAGES: A tuple that contains available languages for the project. They come in two tuples of a language code and language name. You can see the list of available languages at django.conf.global_settings. When you choose which languages your site will be available in, you set LANGUAGES to a subset of that list.
    LOCALE_PATHS: A list of directories where Django looks for message files containing translations for the project.
    TIME_ZONE: A string that represents the timezone for the project. This is set to 'UTC' when you create a new project using the startproject command. You can set it to any other timezone, such as 'Europe/Madrid'.
    These are some of the internationalization and localization settings available. You can find the full list at https://docs.djangoproject.com/en/3.0/ref/settings/#globalization-i18n-l10n.”

    ++ Internationalization management commands :

    Django includes the following management commands to manage translations:

    makemessages: This runs over the source tree to find all strings marked for translation and creates or updates the .po message files in the locale directory. A single .po file is created for each language.
    compilemessages: This compiles the existing .po message files to .mo files that are used to retrieve translations.
    You will need the gettext toolkit to be able to create, update, and compile message files. Most Linux distributions include the gettext toolkit. If you are using macOS, probably the simplest way to install it is via Homebrew, at https://brew.sh/, with the command brew install gettext. You might also need to force link it
    with the command brew link --force gettext. For Windows, follow the steps at https://docs.djangoproject.com/en/3.0/topics/i18n/translation/#gettext-on-windows.

    How to add translations to a Django project

    Let's take a look at the process of internationalizing your project. You will need to do the following:

    1- Mark strings for translation in your Python code and your templates
    2- Run the makemessages command to create or update message files that include all translation strings from your code
    3- Translate the strings contained in the message files and compile them using the compilemessages management command

    How Django determines the current language

    Django comes with a middleware that determines the current language based on the request data. This is the LocaleMiddleware middleware that resides in django.middleware.locale.LocaleMiddleware performs the following tasks:

    If you are using i18n_patterns, that is, you are using translated URL patterns, it looks for a language prefix in the requested URL to determine the current language.
    If no language prefix is found, it looks for an existing LANGUAGE_SESSION_KEY in the current user's session.
    If the language is not set in the session, it looks for an existing cookie with the current language. A custom name for this cookie can be provided in the LANGUAGE_COOKIE_NAME setting. By default, the name for this cookie is django_language.
    If no cookie is found, it looks for the Accept-Language HTTP header of the request.
    If the Accept-Language header does not specify a language, Django uses the language defined in the LANGUAGE_CODE setting.
    By default, Django will use the language defined in the LANGUAGE_CODE setting unless you are using LocaleMiddleware. The process described here only applies when using this middleware.

    Preparing your project for internationalization
    Let's prepare your project to use different languages. You are going to create an English and a Spanish version for your shop. Edit the settings.py file of your project and add the following LANGUAGES setting to it. Place it next to the LANGUAGE_CODE setting:

    LANGUAGES = (
        ('en', 'English'),
        ('es', 'Spanish'),
    )

    “The LANGUAGES setting contains two tuples that consist of a language code and a name. Language codes can be locale-specific, such as en-us or en-gb, or generic, such as en. With this setting, you specify that your application will only be available in English and Spanish. If you don't define a custom LANGUAGES setting, the site will be available in all the languages that Django is translated into.

    Make your LANGUAGE_CODE setting look as follows:

    LANGUAGE_CODE = 'en'
    Add 'django.middleware.locale.LocaleMiddleware' to the MIDDLEWARE setting. Make sure that this middleware comes after SessionMiddleware because LocaleMiddleware needs to use session data. It also has to be placed before CommonMiddleware because the latter needs an active language to resolve the requested URL. The MIDDLEWARE setting should now look as follows:

    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.locale.LocaleMiddleware',
        'django.middleware.common.CommonMiddleware',
        # ...
    ]

    +++ The order of middleware classes is very important because each middleware can depend on data set by other middleware executed previously. Middleware is applied for requests in order of appearance in MIDDLEWARE, and in reverse order for responses.

    Create the following directory structure inside the main project directory, next to the manage.py file:

    locale/
        en/
        es/
    The locale directory is the place where message files for your application will reside. Edit the settings.py file again and add the following setting to it:

    LOCALE_PATHS = (
        os.path.join(BASE_DIR, 'locale/'),
    )

    Translating Python code
    To translate literals in your Python code, you can mark strings for translation using the gettext() function included in django.utils.translation. This function translates the message and returns a string. The convention is to import this function as a shorter alias named _ (underscore character).

    You can find all the documentation about translations at https://docs.djangoproject.com/en/3.0/topics/i18n/translation/.

    Standard translations

    The following code shows how to mark a string for translation:

    from django.utils.translation import gettext as _
    output = _('Text to be translated.')

    Django includes lazy versions for all of its translation functions, which have the suffix _lazy(). When using the lazy functions, strings are translated when the value is accessed, rather than when the function is called (this is why they are translated lazily). The lazy translation functions come
    in handy when strings marked for translation are in paths that are executed when modules are loaded.

    ++ Using gettext_lazy() instead of gettext() means that strings are translated when the value is accessed. Django offers a lazy version for all translation functions.

    Translations including variables

    The strings marked for translation can include placeholders to include variables in the translations. The following code is an example of a translation string with a placeholder:

    from django.utils.translation import gettext as _
    month = _('April')
    day = '14'
    output = _('Today is %(month)s %(day)s') % {'month': month,
                                                'day': day}
    By using placeholders, you can reorder the text variables. For example, an English translation of the previous example might be today is April 14, while the Spanish one might be hoy es 14 de Abril. Always use string interpolation instead of positional interpolation when you have more than one parameter
    for the translation string. By doing so, you will be able to reorder the placeholder text.

    Plural forms in translations

    For plural forms, you can use ngettext() and ngettext_lazy(). These functions translate singular and plural forms depending on an argument that indicates the number of objects. The following example shows how to use them:

    output = ngettext('there is %(count)d product',
                      'there are %(count)d products',
                      count) % {'count': count}
    Now that you know the basics about translating literals in your Python code, it's time to apply translations to your project.

    Translating your own code

    Edit the settings.py file of your project, import the gettext_lazy() function, and change the LANGUAGES setting as follows to translate the language names:

    from django.utils.translation import gettext_lazy as _
    LANGUAGES = (
        ('en', _('English')),
        ('es', _('Spanish')),
    )

    Here, you use the gettext_lazy() function instead of gettext() to avoid a circular import, thus translating the languages' names when they are accessed.

    Open the shell and run the following command from your project directory:

    $ django-admin makemessages --all

    You should see the following output:

    processing locale es
    processing locale en
    Take a look at the locale/ directory. You should see a file structure like the following:

    en/
        LC_MESSAGES/
            django.po
    es/
        LC_MESSAGES/
            django.po
    A .po message file has been created for each language. Open es/LC_MESSAGES/django.po with a text editor. At the end of the file, you should be able to see the following:

    #: myshop/settings.py:118
    msgid "English"
    msgstr ""
    #: myshop/settings.py:119
    msgid "Spanish"
    msgstr ""
    Each translation string is preceded by a comment showing details about the file and the line where it was found. Each translation includes two strings:

    msgid: The translation string as it appears in the source code.
    msgstr: The language translation, which is empty by default. This is where you have to enter the actual translation for the given string.
    Fill in the msgstr translations for the given msgid string, as follows:

    #: myshop/settings.py:118
    msgid "English"
    msgstr "Inglés"
    “#: myshop/settings.py:119
    msgid "Spanish"
    msgstr "Español"
    Save the modified message file, open the shell, and run the following command:

    $ django-admin compilemessages

    If everything goes well, you should see an output like the following:

    processing file django.po in /Users/MDRAHALI/Desktop/Fullstack-Django/Online-Shop/online_shop/locale/es/LC_MESSAGES
    processing file django.po in /Users/MDRAHALI/Desktop/Fullstack-Django/Online-Shop/online_shop/locale/en/LC_MESSAGES

    “You have translated the language names themselves. Now, let's translate the model field names that are displayed in the site. Edit the models.py file of the orders application and add names marked for translation for the Order model fields as follows:

    from django.utils.translation import gettext_lazy as _
    class Order(models.Model):
        first_name = models.CharField(_('first name'),
                                      max_length=50)
        last_name = models.CharField(_('last name'),
                                     max_length=50)
        email = models.EmailField(_('e-mail'))
        address = models.CharField(_('address'),
                                   max_length=250)
        postal_code = models.CharField(_('postal code'),
                                       max_length=20)
        city = models.CharField(_('city'),
                                max_length=100)
        # ...

    You have added names for the fields that are displayed when a user is placing a new order. These are first_name, last_name, email, address, postal_code, and city. Remember that you can also use the verbose_name attribute to name the fields.”

    $ django-admin makemessages --all
    $ django-admin compilemessages

    Translating templates
    Django offers the {% trans %} and {% blocktrans %} template tags to translate strings in templates. In order to use the translation template tags, you have to add {% load i18n %} at the top of your template to load them.

    The {% trans %} template tag

    The {% trans %} template tag allows you to mark a literal for translation. Internally, Django executes gettext() on the given text. This is how to mark a string for translation in a template:

    {% trans "Text to be translated" %}
    You can use as to store the translated content in a variable that you can use throughout your template. The following example stores the translated text in a variable called greeting:

    {% trans "Hello!" as greeting %}
    <h1>{{ greeting }}</h1>
    The {% trans %} tag is useful for simple translation strings, but it can't handle content for translation that includes variables.

    The {% blocktrans %} template tag

    The {% blocktrans %} template tag allows you to mark content that includes literals and variable content using placeholders. The following example shows you how to use the {% blocktrans %} tag, including a name variable in the content for translation:

    {% blocktrans %}Hello {{ name }}!{% endblocktrans %}
    You can use with to include template expressions, such as accessing object attributes or applying template filters to
    variables. You always have to use placeholders for these. You can't access expressions or object attributes inside the blocktrans block. The following example shows you how to use with to include an object attribute to which the capfirst filter is applied:

    {% blocktrans with name=user.name|capfirst %}
      Hello {{ name }}!
    {% endblocktrans %}

    ++ Use the {% blocktrans %} tag instead of {% trans %} when you need to include variable content in your translation string.

    - Using the Rosetta translation interface :
    Rosetta is a third-party application that allows you to edit translations using the same interface as the Django administration site. Rosetta makes it easy to edit .po files and it updates compiled translation files. Let's add it to your project.

    - Install Rosetta via pip using this command:

    $ pip install django-rosetta==0.9.3

    Then, add 'rosetta' to the INSTALLED_APPS setting in your project's settings.py file, as follows:

    INSTALLED_APPS = [
        # ...
        'rosetta',
    ]
    You need to add Rosetta's URLs to your main URL configuration. Edit the main urls.py file of your project and add the following URL pattern to it:

    urlpatterns = [
        # ...
        path('rosetta/', include('rosetta.urls')),
        path('', include('shop.urls', namespace='shop')),
    ]
    Make sure you place it before the shop.urls pattern to avoid an undesired pattern match.

    - Open http://127.0.0.1:8000/admin/ and log in.

    -> http://127.0.0.1:8000/rosetta

    Rosetta uses a different background color to display placeholders. When you translate content, make sure that you keep placeholders untranslated. For example, take the following string:

    %(items)s items, $%(total)s
    It is translated into Spanish as follows:

    %(items)s productos, $%(total)s
    You can take a look at the source code that comes along with this chapter to use the same Spanish translations for your project.

    When you add new translations to your production environment, if you serve Django with a real web server, you will have to reload your server after running the compilemessages command, or
    after saving the translations with Rosetta, for changes to take effect.

    - Fuzzy translations :
    You might have noticed that there is a FUZZY column in Rosetta. This is not a Rosetta feature; it is provided by gettext. If the fuzzy flag is active for a translation, it will not be included
    in the compiled message files. This flag marks translation strings that need to be reviewed by a translator. When .po files are updated with new translation strings, it is possible that some
    translation strings will automatically be flagged as fuzzy. This happens when gettext finds some msgid that has been slightly modified. gettext pairs it with what it thinks was the old
    translation and flags it as fuzzy for review. The translator should then review fuzzy translations, remove the fuzzy flag, and compile the translation file again.

    URL patterns for internationalization
    Django offers internationalization capabilities for URLs. It includes two main features for internationalized URLs:

    Language prefix in URL patterns: Adding a language prefix to URLs to serve each language version under a different base URL
    Translated URL patterns: Translating URL patterns so that every URL is different for each language
    A reason for translating URLs is to optimize your site for search engines. By adding a language prefix to your patterns, you will be able to index a URL for each language instead of a single URL
    for all of them. Furthermore, by translating URLs into each language, you will provide search engines with URLs that will rank better for each language.

    Adding a language prefix to URL patterns

    Django allows you to add a language prefix to your URL patterns. For example, the English version of your site can be served under a path starting /en/, and the Spanish version under /es/. To use
    languages in URL patterns, you have to use the LocaleMiddleware provided by Django. The framework will use it to identify the current language from the requested URL. You added it previously to the
    MIDDLEWARE setting of your project, so you don't need to do it now.

    Let's add a language prefix to your URL patterns. Edit the main urls.py file of the myshop project and add i18n_patterns(), as follows:

    from django.conf.urls.i18n import i18n_patterns
    urlpatterns = i18n_patterns(
     path('admin/', admin.site.urls),
     path('cart/', include('cart.urls', namespace='cart')),
     path('orders/', include('orders.urls', namespace='orders')),
     path('payment/', include('payment.urls', namespace='payment')),
     path('coupons/', include('coupons.urls', namespace='coupons')),
     path('rosetta/', include('rosetta.urls')),
     path('', include('shop.urls', namespace='shop')),
    )
    You can combine non-translatable standard URL patterns and patterns under i18n_patterns so that some patterns include a language prefix and others don't. However, it's better to use ”

    Translating models with django-parler
    Django does not provide a solution for translating models out of the box. You have to implement your own solution to manage content stored in different languages, or use a third-party module for model translation. There are several third-party applications that allow you to translate model fields. Each of them takes a different approach to storing and accessing translations. One of these applications is django-parler. This module offers a very effective way to translate models and it integrates smoothly with Django's administration site.

    django-parler generates a separate database table for each model that contains translations. This table includes all the translated fields and a foreign key for the original object that the translation belongs to. It also contains a language field, since each row stores the content for a single language.

    Installing django-parler
    Install django-parler via pip using the following command:

    $ pip install django-parler==2.0.1

    “Translating model fields

    Let's add translations for your product catalog. django-parler provides a TranslatableModel model class and a TranslatedFields wrapper to translate model fields. Edit the models.py file inside the shop application directory and add the following import:

    from parler.models import TranslatableModel, TranslatedFields
    Then, modify the Category model to make the name and slug fields translatable, as follows:

    class Category(TranslatableModel):
        translations = TranslatedFields(
            name = models.CharField(max_length=200,
                                    db_index=True),
            slug = models.SlugField(max_length=200,
                                    db_index=True,
                                    unique=True)
        )
    The Category model now inherits from TranslatableModel instead of models.Model and both the name and slug fields are included in the TranslatedFields wrapper.

    Edit the Product model to add translations for the name, slug, and description fields, as follows:

    class Product(TranslatableModel):
        translations = TranslatedFields(
            name = models.CharField(max_length=200, db_index=True),
            slug = models.SlugField(max_length=200, db_index=True)
            )

django-parler manages translations by generating another model for each translatable model. In the following schema, you can see the fields of the Product model and what the generated ProductTranslation model will look like:
![](./static/TranslableModel.png)

    The ProductTranslation model generated by django-parler includes the name, slug, and description translatable fields, a language_code field, and a ForeignKey for the master Product object. There is a one-to-many relationship from Product to ProductTranslation. A ProductTranslation object will exist for each available language of each Product object.

    Since Django uses a separate table for translations, there are some Django features that you can't use. It is not possible to use a default ordering by a translated field. You can filter by translated fields in queries, but you can't include a translatable field in the ordering Meta options.

    Edit the models.py file of the shop application and comment out the ordering attribute of the Category Meta class:

    class Category(TranslatableModel):
        # ...
        class Meta:
            # ordering = ('name',)
            verbose_name = 'category'
            verbose_name_plural = 'categories'


    You can read more about the django-parler module's compatibility with Django at https://django-parler.readthedocs.io/en/latest/compatibility.html.
    Integrating translations into the administration site

    django-parler integrates smoothly with the Django administration site. It includes a TranslatableAdmin class that overrides the ModelAdmin class provided by Django to manage model translations.

    Edit the admin.py file of the shop application and add the following import to it:

    from parler.admin import TranslatableAdmin
    Modify the CategoryAdmin and ProductAdmin classes to inherit from TranslatableAdmin instead of ModelAdmin. django-parler doesn't support the prepopulated_fields attribute, but it does support the get_prepopulated_fields() method that
    provides the same functionality. Let's change this accordingly.

    ++ Admin Translable :

    @admin.register(Category)
    class CategoryAdmin(TranslatableAdmin):
        list_display = ['name', 'slug']

    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('name',)}

    $ python manage.py makemigrations shop --name 'translations'

    This migration automatically includes the CategoryTranslation and ProductTranslation models created dynamically by django-parler. It's important to note that this migration deletes the previous existing fields from your models. This means that you will lose that data and will need to set your categories and products again in the administration site after running it.

    Edit the file migrations/0002_translations.py of the shop application and replace the two occurrences of the following line:

    bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
    with the following one:

    bases=(parler.models.TranslatableModel, models.Model),
    This is a fix for a minor issue found in the django-parler version you are using. This change is necessary to prevent the migration from failing when applying it. This issue is related to creating translations for existing fields in the model and will probably be fixed in newer django-parler versions.

    Run the following command to apply the migration:

    $ python manage.py migrate shop


    “Adapting views for translations

    You have to adapt your shop views to use translation QuerySets. Run the following command to open the Python shell:

    python manage.py shell
    Let's take a look at how you can retrieve and query translation fields. To get the object with translatable fields translated in a specific language, you can use Django's activate() function, as follows:

    >>> from shop.models import Product
    >>> from django.utils.translation import activate
    >>> activate('es')
    >>> product=Product.objects.first()
    >>> product.name
    'Té verde'
    Another way to do this is by using the language() manager provided by django-parler, as follows:

    >>> product=Product.objects.language('en').first()
    >>> product.name
    'Green tea'
    When you access translated fields, they are resolved using the current language. You can set a different current language for an object to access that specific translation, as follows:

    >>> product.set_current_language('es')
    >>> product.name
    'Té verde'
    >>> product.get_current_language()
    'es”

    “When performing a QuerySet using filter(), you can filter using the related translation objects with the translations__ syntax, as follows:

    >>> Product.objects.filter(translations__name='Green tea')
    <TranslatableQuerySet [<Product: Té verde>]>
    Let's adapt the product catalog views. Edit the views.py file of the shop application and, in the product_list view, find the following line:

    category = get_object_or_404(Category, slug=category_slug)
    Replace it with the following ones:

    language = request.LANGUAGE_CODE
    category = get_object_or_404(Category,
                                 translations__language_code=language,
                                 translations__slug=category_slug)
    Then, edit the product_detail view and find the following lines:

    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    Replace them with the following code:

    language = request.LANGUAGE_CODE
    product = get_object_or_404(Product,
                                id=id,
                                translations__language_code=language,
                                translations__slug=slug,
                                available=True)
    The product_list and product_detail views are now adapted to retrieve objects using translated fields. Run the development server and open http://127.0.0.1:8000/es/ in your browser. You should see the product list page, including all products translated into Spanish”

    Format localization
    Depending on the user's locale, you might want to display dates, times, and numbers in different formats. Localized formatting can be activated by changing the USE_L10N setting to True in the settings.py file of your project.
    When USE_L10N is enabled, Django will try to use a locale-specific format whenever it outputs a value in a template. You can see that decimal numbers in the English version of your site are displayed with a dot separator for decimal places, while in the Spanish version,
    they are displayed using a comma. This is due to the locale formats specified for the es locale by Django.

    Normally, you will set the USE_L10N setting to True and let Django apply the format localization for each locale. However, there might be situations in which you don't want to use localized values. This is especially relevant when outputting JavaScript or JSON that has to provide a machine-readable format.

    Django offers a {% localize %} template tag that allows you to turn on/off localization for template fragments. This gives you control over localized formatting. You will have to load the l10n tags to be able to use this template tag. The following is an example of how to turn localization on and off in a template:

    {% load l10n %}
    {% localize on %}
      {{ value }}
    {% endlocalize %}

    {% localize off %}
     {{ value }}
    {% endlocalize %}
    Django also offers the localize and unlocalize template filters to force or avoid the localization of a value. These filters can be applied as follows:

    {{ value|localize }}
    {{ value|unlocalize }}
    You can also create custom format files to specify locale formatting. You can find further information about format localization at https://docs.djangoproject.com/en/3.0/topics/i18n/formatting/.

    “Using django-localflavor to validate form fields
    django-localflavor is a third-party module that contains a collection of utils, such as form fields or model fields, that are specific for each country. It's very useful for validating local regions, local phone numbers, identity card numbers, social security numbers, and so on. The package is organized into a series of modules named after ISO 3166 country codes.

    Install django-localflavor using the following command:

    $ pip install django-localflavor==3.0.1
    Edit the settings.py file of your project and add localflavor to the INSTALLED_APPS setting, as follows:

    INSTALLED_APPS = [
        # ...
        'localflavor',
    ]
    You are going to add the United States' zip code field so that a valid United States zip code is required to create a new order.

    Edit the forms.py file of the orders application and make it look as follows:

    from django import forms
    from localflavor.us.forms import USZipCodeField
    from .models import Order
    class OrderCreateForm(forms.ModelForm):
        postal_code = USZipCodeField()
        class Meta:
            model = Order
            fields = ['first_name', 'last_name', 'email', 'address',
                      'postal_code', 'city']

    You import the USZipCodeField field from the us package of localflavor and use it for the postal_code field of the OrderCreateForm form.

    This is just a brief example of how to use a custom field from localflavor in your own project for validation purposes. The local components
    provided by localflavor are very useful for adapting your application to specific countries. You can read the django-localflavor documentation
    and see all available local components for each country at https://django-localflavor.readthedocs.io/en/latest/.


    Building a recommendation engine

    A recommendation engine is a system that predicts the preference or rating that a user would give to an item. The system selects relevant items for a user based on their behavior and the knowledge it has about them. Nowadays, recommendation systems are used in many online services.
    They help users by selecting the stuff they might be interested in from the vast amount of available data that is irrelevant to them. Offering good recommendations enhances user engagement. E-commerce sites also benefit from offering relevant product recommendations by increasing their average revenue per user.
    You are going to create a simple, yet powerful, recommendation engine that suggests products that are usually bought together. You will suggest products based on historical sales, thus identifying products that are usually bought together. You are going to suggest complementary products in two different scenarios:
    Product detail page: You will display a list of products that are usually bought with the given product. This will be displayed as users who bought this also bought X, Y, Z. You need a data structure that allows you to store the number of times that each product has been bought together with the product being displayed.
    Cart detail page: Based on the products users add to the cart, you are going to suggest products that are usually bought together with these ones. In this case, the score you calculate to obtain related products has to be aggregated.
    You are going to use Redis to store products that are purchased together. Remember that you already used Redis in Chapter 6, Tracking User Actions. If you haven't installed Redis yet, you can find installation instructions in that chapter.”

    “Recommending products based on previous purchases”

    You will recommend products to users based on what they have added to the cart. You are going to store a key in Redis for each product bought on your site. The product key will contain a Redis sorted set with scores. You will increment the score by 1 for each product bought together every time a new purchase is completed. The sorted set will allow you to give scores to products that are bought together.

    “Remember to install redis-py in your environment using the following command:

    pip install redis==3.4.1
    Edit the settings.py file of your project and add the following settings to it:

    REDIS_HOST = 'localhost'
    REDIS_PORT = 6379
    REDIS_DB = 1
    These are the settings required to establish a connection with the Redis server. Create a new file inside the shop application directory and name it recommender.py. Add the following code to it:

    import redis
    from django.conf import settings
    from .models import Product
    # connect to redis
    r = redis.Redis(host=settings.REDIS_HOST,
                    port=settings.REDIS_PORT,
                    db=settings.REDIS_DB)
    class Recommender(object):
        def get_product_key(self, id):
            return f'product:{id}:purchased_with'
        def products_bought(self, products):
            product_ids = [p.id for p in products]
            for product_id in product_ids:
                for with_id in product_ids:
                    # get the other products bought with each product
                    if product_id != with_id:
                        # increment score for product purchased together
                        r.zincrby(self.get_product_key(product_id),
                                  1,
                                  with_id)
    This is the Recommender class that will allow you to store product purchases and retrieve product suggestions for a given product or products.

    The get_product_key() method receives an ID of a Product object and builds the Redis key for the sorted set where related products are stored, which looks like product:[id]:purchased_with.

    The products_bought() method receives a list of Product objects that have been bought together (that is, belong to the same order).
    In this method, you perform the following tasks:
    You get the product IDs for the given Product objects.


    “You now have a method to store and score the products that were bought together. Next, you need a method to retrieve the products that were bought together for a list of given products. Add the following suggest_products_for() method to the Recommender class:

    def suggest_products_for(self, products, max_results=6):
        product_ids = [p.id for p in products]
        if len(products) == 1:
            # only 1 product
            suggestions = r.zrange(
                             self.get_product_key(product_ids[0]),
                             0, -1, desc=True)[:max_results]
        else:
            # generate a temporary key
            flat_ids = ''.join([str(id) for id in product_ids])
            tmp_key = f'tmp_{flat_ids}'
            # multiple products, combine scores of all products
            # store the resulting sorted set in a temporary key
            keys = [self.get_product_key(id) for id in product_ids]
            r.zunionstore(tmp_key, keys)
            # remove ids for the products the recommendation is for
            r.zrem(tmp_key, *product_ids)
            # get the product ids by their score, descendant sort
            suggestions = r.zrange(tmp_key, 0, -1,
                                   desc=True)[:max_results]
            # remove the temporary key
            r.delete(tmp_key)
        suggested_products_ids = [int(id) for id in suggestions]
        # get suggested products and sort by order of appearance
        suggested_products = list(Product.objects.filter(id__in=suggested_products_ids))
        suggested_products.sort(key=lambda x: suggested_products_ids.index(x.id))
        return suggested_products
    The suggest_products_for() method receives the following parameters:

    products: This is a list of Product objects to get recommendations for. It can contain one or more products.
    max_results: This is an integer that represents the maximum number of recommendations to return.

    In this method, you perform the following actions:

    You get the product IDs for the given Product objects.
    If only one product is given, you retrieve the ID of the products that were bought together with the given product, ordered by the total number of times that they were bought together.
    To do so, you use Redis' ZRANGE command. You limit the number of results to the number specified in the max_results attribute (6 by default).
    If more than one product is given, you generate a temporary Redis key built with the IDs of the products.
    You combine and sum all scores for the items contained in the sorted set of each of the given products. This is done using the Redis ZUNIONSTORE command. The ZUNIONSTORE command performs
    a union of the sorted sets with the given keys, and stores the aggregated sum of scores of the elements in a new Redis key. You can read more about this command at https://redis.io/commands/ZUNIONSTORE.
    You save the aggregated scores in the temporary key.
    Since you are aggregating scores, you might obtain the same products you are getting recommendations for. You remove them from the generated sorted set using[…]”

    + Recommandation simulation :

    >>> from shop.models import Product
    >>> iphone_xs = Product.objects.get(translations__name='Iphone XS')
    >>> lcd_tv = Product.objects.get(translations__name='LCD Television')
    >>> ipod = Product.objects.get(translations__name='IPOD')
    >>> art = Product.objects.get(translations__name='ART')

    Then, add some test purchases to the recommendation engine:

    >>> from shop.recommender import Recommender
    >>> r = Recommender()
    >>> r.products_bought([iphone_xs, lcd_tv])
    >>> r.products_bought([iphone_xs, ipod])
    >>> r.products_bought([lcd_tv, art, ipod])
    >>> r.products_bought([iphone_xs, ipod])
    >>> r.products_bought([art, ipod])
    >>> r.products_bought([lcd_tv, iphone_xs])

    You have stored the following scores:

    art:  lcd_tv (2), ipod (2), iphone_xs (1)
    lcd_tv:    art (2), ipod (1), iphone_xs (1)
    iphone_xs:  art (1), ipod (1), lcd_tv(1)
    ipod: black_tea (2), lcd_tv (1), iphone_xs (1)

    Let's activate a language to retrieve translated products and get product recommendations to buy together with a given single product:

    >>> from django.utils.translation import activate
    >>> activate('en')
    >>> r.suggest_products_for([art])
    [<Product: IPOD>, <Product: LCD Television>]
    >>> r.suggest_products_for([lcd_tv])
    [<Product: Iphone XS>, <Product: ART>, <Product: IPOD>]
    >>> r.suggest_products_for([iphone_xs])
    [<Product: IPOD>, <Product: LCD Television>]
    >>> r.suggest_products_for([ipod])
    [<Product: ART>, <Product: Iphone XS>, <Product: LCD Television>]

    You can see that the order for recommended products is based on their score. Let's get recommendations for multiple products with aggregated scores:

    >>> r.suggest_products_for([iphone_xs, art])
    [<Product: IPOD>, <Product: LCD Television>]
    >>> r.suggest_products_for([ipod, art])
    [<Product: LCD Television>, <Product: Iphone XS>]
    >>> r.suggest_products_for([lcd_tv, iphone_xs])
    [<Product: IPOD>, <Product: ART>]

    Summary

    In this chapter, you created a coupon system using sessions. You also learned the basics of internationalization and localization for Django projects. You marked code and template strings
    for translation, and you discovered how to generate and compile translation files. You also installed Rosetta in your project to manage translations through a browser interface. You translated
    URL patterns and you created a language selector to allow users to switch the language of the site. Then, you used django-parler to translate models and you used django-localflavor to validate
    localized form fields. Finally, you built a recommendation engine using Redis to recommend products that are usually purchased together.

    + TIPS for database :
    - you can dumb data of a database table using this command in JSON format :
    $ python manage.py dumpdata orders --indent=2
    $ python manage.py dumpdata --help # for more commands

    mkdir orders/fixtures
    python manage.py dumpdata orders --indent=2 --output=courses/fixtures/orders.json
    Run the development server and use the administration site to remove the subjects you created. Then, load the fixture into the database using the following command:

    $ python manage.py loaddata subjects.json

    + Coursera platform :
        brew install memcached
        memcached -l 127.0.0.1:11211
        pip install python-memcached==1.59

        pip install django-memcache-status==2.2


