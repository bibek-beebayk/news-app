from rest_framework.routers import DefaultRouter

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from apps.author import api as author_api
from apps.news import api as news_api


router = DefaultRouter()

router.register('author', author_api.AuthorViewSet, basename='author')
router.register('news', news_api.NewsViewSet, basename='news')
router.register('category', news_api.CategoryViewSet, basename='category')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('ckeditor/', include('ckeditor_uploader.urls')),

]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)