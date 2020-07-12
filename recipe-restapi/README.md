
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

    + run server :
    $ docker-compose up

    - Testing uploading images :
    $ http://127.0.0.1:8000/api/recipe/recipes/1/upload-image/

    - Testing Filtering from recipes  :
    $ http://127.0.0.1:8000/api/recipe/recipes/?ingredients=2
    $ http://127.0.0.1:8000/api/recipe/recipes/?ingredients=2&tags=1

    - Testing Filtering from Tags and Ingredients :
    $ http://127.0.0.1:8000/api/recipe/tags/?assigned_only=1
    $ http://127.0.0.1:8000/api/recipe/ingredients/?assigned_only=1
