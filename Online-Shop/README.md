### + Creating an Online Shop :


    In this chapter, you will start a new Django project that consists of a fully featured online shop. This chapter and the following two chapters
    will show you how to build the essential functionalities of an e-commerce platform. Your online shop will enable clients to browse products,
    add them to the cart, apply discount codes, go through the checkout process, pay with a credit card, and obtain an invoice. You will also
    implement a recommendation engine to recommend products to your customers, and you will use internationalization to offer your site in multiple languages.

    In this chapter, you will learn how to:

    Create a product catalog
    Build a shopping cart using Django sessions
    Create custom context processors
    Manage customer orders
    Configure Celery in your project with RabbitMQ as a message broker
    Send asynchronous notifications to customers using Celery
    Monitor Celery using Flower
    Creating an online shop project

    Let's start with a new Django project to build an online shop. Your users will be able to browse through a product catalog and add products to a shopping cart.
    Finally, they will be able to check out the cart and place an order. This chapter will cover the following functionalities

    + Creating the product catalog models, adding them to the administration site, and building the basic views to display the catalog
    + Building a shopping cart system using Django sessions to allow users to keep selected products while they browse the site
    + Creating the form and functionality to place orders on the site
    + Sending an asynchronous email confirmation to users when they place an order.

    - create the project :
    $ django-admin startproject online_shop

    - create the app :
    $ django-admin startapp shop

    Creating product catalog models
    The catalog of your shop will consist of products that are organized into different categories. Each product will have a name, an optional description,
    an optional image, a price, and its availability.


    prepopulated_fields = {'slug': ('name',)}

    * Remember that you use the prepopulated_fields attribute to specify fields where the value is automatically set using the value of other fields. As you have seen before,
    this is convenient for generating slugs.

    list_display = ['name', 'slug', 'price', 'available', 'created', 'updated']
    list_editable = ['price', 'available']

    * You use the list_editable attribute in the ProductAdmin class to set the fields that can be edited from the list display page of the administration site. This will allow
    you to edit multiple rows at once. Any field in list_editable must also be listed in the list_display attribute, since only the fields displayed can be edited.


