from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UrlShortenerView

router = DefaultRouter()
router.register(r'', UrlShortenerView, basename='url-shortener')

urlpatterns = [
    path('', include(router.urls)),
]
