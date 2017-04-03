from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.core.urlresolvers import reverse


class Image(models.Model):
    """
    Image model for storing images bookmarked
    from different sites.
    """
    # One-to-many
    # User can post multiple images, but each image is posted
    # by a single user.
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='images_created')
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,
                            blank=True)
    url = models.URLField()
    image = models.ImageField(upload_to='images/%Y/%m/%d')
    description = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True,
                               db_index=True)
    # Many-to-many
    # User might like multiple images and image can by like by multi users.
    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                        related_name='images_liked',
                                        blank=True)



    # Canonical URLs
    def get_absolute_url(self):
        return reverse('images:detail', args=[self.id, self.slug])


    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        """
        Override the save() method of the Image model
        to automatically generate the slug field based
        on the value of the title field.
        """
        if not self.slug:
            self.slug = slugify(self.title)
            super(Image, self).save(*args, **kwargs)

    total_likes = models.PositiveIntegerField(db_index=True,
                                              default=0)
