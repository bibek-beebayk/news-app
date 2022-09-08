from rest_framework import serializers
from versatileimagefield.utils import get_url_from_image_key

class ImageKeySerializer(serializers.ImageField):
    def __init__(self, key, *args, **kwargs):
        self.key = key
        super().__init__(*args, **kwargs)

    def to_representation(self, value):
        if not value:
            return None
        try:
            key = value.instance.SIZES[value.field.name][self.key]
        except KeyError:
            return
        url = get_url_from_image_key(value, key)
        request = self.context.get('request', None)

        if request:
            return request.build_absolute_uri(url)
        else:
            try:
                rep = super().to_representation(url)
                if rep is None:
                    return url
                return rep
            except AttributeError:
                return super().to_native(url)

    to_native = to_representation