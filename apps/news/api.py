from rest_framework import viewsets, mixins

from apps.news.models import News, Category
from apps.news.serializers import NewsListSerializer, NewsDetailsSerializer, CategoriesListSerializer


class NewsViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = News.objects.all().select_related('author', 'category').prefetch_related('tags')
    serializer_class = NewsDetailsSerializer
    lookup_field = 'slug'
    def get_serializer_class(self):
        if self.action == 'list':
            self.serializer_class = NewsListSerializer
        return self.serializer_class


class CategoriesViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Category.objects.all().prefetch_related('news')
    serializer_class = CategoriesListSerializer
    lookup_field = 'slug'