### + Django Web app - Real Estate Brokerage platform

    $ psql postgres
    CREATE USER postgres WITH ENCRYPTED PASSWORD 'yourpass';

    CREATE DATABASE realestate ENCODING 'UTF8' OWNER=postgres;

    - because we user a new database we should create a new superuser :
    + create a superuser :

    $ python manage.py createsuperuser

     !! IMPORTANT -> Please test the app in incognito because some extension could makes trouble in your static files js/css :
     -> http://127.0.0.1:8000/

    +  Django app deployment from A to Z :
    https://gist.github.com/bradtraversy/cfa565b879ff1458dba08f423cb01d71

