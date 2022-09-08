from versatileimagefield.fields import VersatileImageField
from ckeditor.fields import RichTextField

from django.db import models
from django.dispatch import receiver

from news_app.libs.image import warm


class Author(models.Model):
    name = models.CharField(max_length=256)
    subtitle = models.CharField(max_length=256, blank=True, null=True)
    slug = models.SlugField(max_length=256, blank=True)
    image = VersatileImageField(upload_to='authors/', blank=True, null=True)
    description = RichTextField(blank=True, null=True)

    SIZES = {
        'image': {
            'small': 'thumbnail__320x180',
            'medium': 'thumbnail__640x360',
            'og': 'og__1200x630',
        },
    }

    def __str__(self) -> str:
        return self.name


@receiver(models.signals.post_save, sender=Author)
def warm_images(sender, instance, **kwargs):
    warm(instance)
