from django.db import models
from django.conf import settings
from django.utils.text import slugify

class Image(models.Model):
    """
    Image model for storing images bookmarked
    from different sites.
    """
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
