from unicodedata import category
from rest_framework import serializers

from apps.news.models import News, Category, Tag
from news_app.libs.serializer import ImageKeySerializer


class NewsListSerializer(serializers.ModelSerializer):
    header_image = ImageKeySerializer('small')
    category = serializers.StringRelatedField()
    class Meta:
        model = News
        fields = ['title', 'slug', 'category', 'excerpt', 'header_image', 'published_at']


class NewsDetailsSerializer(serializers.ModelSerializer):
    header_image = ImageKeySerializer('medium')
    author = serializers.StringRelatedField()
    category = serializers.StringRelatedField()
    tags = serializers.StringRelatedField(many=True)
    class Meta:
        model = News
        fields = ['title', 'subtitle', 'slug', 'author', 'category', 'published_at', 'excerpt', 'content', 'header_image', 'tags']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'slug']