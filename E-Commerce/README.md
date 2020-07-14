## - Alibaba eCommerce Alike Web application

### - Setting up Third-party APIs :

    + Stripe Integration :

    + MailChimp Integration :
        1- Get api keys
        2- Create webhook from this link (https://us10.admin.mailchimp.com/lists/tools/webhooks-create?id=434529)
        3- for the calling url use requestBin https://requestbin.com/

        *** Example showing how to do this -> https://www.codingforentrepreneurs.com/blog/mailchimp-integration/
        webhook conf -> https://rudrastyh.com/mailchimp-api/webhooks.html

    + s3 static files :
      *** https://www.codingforentrepreneurs.com/blog/s3-static-media-files-for-django
      to push all static files to folders inside amazon s3

    $ python manage.py collectstatic

    --> Full deployement of Django app to Heroku :
    https://www.codingforentrepreneurs.com/blog/go-live-with-django-project-and-heroku
