from django.contrib.auth import get_user_model
from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)

    def __str__(self):
        return f'Profile for user {self.user.username}'


class Contact(models.Model):
    """
    Using the ORM, you could create a relationship for a user, user1, following another user, user2, like this:

    >> user1 = User.objects.get(id=1)
    >> user2 = User.objects.get(id=2)
    >> Contact.objects.create(user_from=user1, user_to=user2)s

    """
    user_from = models.ForeignKey('auth.User', related_name='rel_from_set', on_delete=models.CASCADE)
    user_to = models.ForeignKey('auth.User', related_name='rel_to_set', on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'{self.user_from} follow {self.user_to}'

# Add following field to User dynamically
user_model = get_user_model()
user_model.add_to_class('following',
                        models.ManyToManyField('self',
                                                through=Contact,
                                                related_name='followers',
                                                symmetrical=False))
"""
Note that the relationship includes symmetrical=False. When you define a ManyToManyField in the model creating a relationship with itself,
Django forces the relationship to be symmetrical. In this case, you are setting symmetrical=False to define a non-symmetrical relationship
(if I follow you, it doesn't mean that you automatically follow me).

"""

