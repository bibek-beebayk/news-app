from html.parser import HTMLParser

from django.conf import settings
from django.db.models import Model
from versatileimagefield.image_warmer import VersatileImageFieldWarmer


def warm(instance):
    if hasattr(instance, 'SIZES') and type(instance.SIZES) == dict:
        for field, set in instance.SIZES.items():
            if getattr(instance, field):
                for key, value in set.items():
                    warmer = VersatileImageFieldWarmer(
                        instance_or_queryset=instance,
                        rendition_key_set=[(key, value)],
                        image_attr=field
                    )
                    try:
                        warmer.warm()
                    except AttributeError:
                        pass