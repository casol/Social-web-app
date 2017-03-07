from django.db import models
from django.conf import settings

class Profile(models.Model):
    """
    Extending User model by creating Profile model which
    contains all additional fields with one-to-one relationship
    with Django User model.

    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d',
                              blank=True)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)
