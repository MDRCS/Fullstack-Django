
### - Make a rest api for recipes :

    1- make Dockerfile
    2- make docker-compose file
    3- mkdir app
    4- build those files :

        docker build .
        docker-compose build

    + create django project :
    $ docker-compose run app sh -c "django-admin startproject app ."

    + create django app `core` :
    $ docker-compose run app sh -c "python manage.py startapp core"

    + run tests :
    $ docker-compose run app sh -c "python manage.py test"

    + make a migration :
    $ docker-compose run app sh -c "python manage.py makemigrations core"

    + run tests and linting usinf Flake8:
    $ docker-compose run app sh -c "python manage.py test && flake8"

    + create a superuser :
    $ docker-compose run app sh -c "python manage.py createsuperuser"

    + create django app `user` :
    $ docker-compose run --rm app sh -c "python manage.py startapp user"

    + create django app `recipe` :
    $ docker-compose run --rm app sh -c "python manage.py startapp recipe"
