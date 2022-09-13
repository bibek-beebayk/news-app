from rest_framework import serializers

from apps.author.models import Author
from apps.news.serializers import NewsListSerializer
from news_app.libs.serializer import ImageKeySerializer


class AuthorDetailsSerializer(serializers.ModelSerializer):
    # image = ImageKeySerializer()
    news = NewsListSerializer(many=True)
    class Meta:
        model = Author
        fields = ['name', 'subtitle', 'slug', 'image', 'description', 'news']


class AuthorListSerializer(serializers.ModelSerializer):
    image = ImageKeySerializer('small')
    class Meta:
        model = Author
        fields = ['name', 'slug', 'image']