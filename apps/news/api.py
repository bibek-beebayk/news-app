from rest_framework import viewsets, mixins
from rest_framework.response import Response

from apps.news.models import News, Category
from apps.news.serializers import CategorySerializer, NewsListSerializer, NewsDetailsSerializer
from news_app.libs.pagination import paginate


class NewsViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = News.objects.all().select_related('author', 'category').prefetch_related('tags')
    serializer_class = NewsDetailsSerializer
    lookup_field = 'slug'
    def get_serializer_class(self):
        if self.action == 'list':
            self.serializer_class = NewsListSerializer
        return self.serializer_class


class CategoryViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'

    def retrieve(self, request, *args, **kwargs): 
        instance = self.get_object() 
        news = News.objects.filter(category=instance).select_related('author', 'category').prefetch_related('tags').order_by('-updated_at') 
        serializer_class = NewsListSerializer 
        return Response(paginate(news, request, serializer_class, page_size=20))
