from rest_framework import viewsets, mixins

from apps.author.models import Author
from apps.author.serializers import AuthorListSerializer, AuthorDetailsSerializer


class AuthorViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Author.objects.all().prefetch_related('news')
    serializer_class = AuthorDetailsSerializer
    lookup_field = 'slug'

    def get_serializer_class(self):
        if self.action == 'list':
            self.serializer_class = AuthorListSerializer
        return self.serializer_class
