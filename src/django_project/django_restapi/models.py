from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserProfileManager(BaseUserManager):
    """ helps django to work with our Profile Model"""

    def create_profile(self, email, name, password=None):
        if not email:
            raise ValueError("profile must have an email.")

        email = self.normalize_email(email)  # Normalize the email address by lowercasing the domain part of it.
        user = self.model(email=email, name=name)

        user.set_password(password)  # this function will hash our pswd
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        user = self.create_profile(email, name, password)
        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ This class gonna be a User Profile for our system  """

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = "email"  # this is the field with which you will login
    REQUIRED_FIELDS = ["name"]

    def get_fullname(self):
        return self.name

    def get_shortname(self):
        return self.name

    def __str__(self):
        return self.email


class ProfileFeedItem(models.Model):
    # delete cascade means that if you delete the UserProfile for a user also the feed will be deleted
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.status_text
