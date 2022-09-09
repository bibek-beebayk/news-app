from versatileimagefield.fields import VersatileImageField, PPOIField
from ckeditor.fields import RichTextField

from django.db import models
from django.dispatch import receiver

from news_app.libs.image import warm


class Author(models.Model):
    name = models.CharField(max_length=256)
    subtitle = models.CharField(max_length=256, blank=True, null=True)
    slug = models.SlugField(max_length=256, blank=True)
    image = VersatileImageField(upload_to='authors/', blank=True, null=True)
    ppoi = PPOIField('Primary Point of Interest')
    description = RichTextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    SIZES = {
        'image': {
            'small': 'thumbnail__320x180',
            'medium': 'thumbnail__640x360',
        },
    }

    def __str__(self) -> str:
        return self.name


@receiver(models.signals.post_save, sender=Author)
def warm_images(sender, instance, **kwargs):
    warm(instance)


@receiver(models.signals.post_delete, sender=Author)
def delete_images(sender, instance, **kwargs):
    instance.image.delete_all_created_images()
