from django.shortcuts import redirect, get_object_or_404
from rest_framework import status, viewsets
from rest_framework.response import Response

from .models import UrlShortener
from .serializers import UrlShortenerSerializer


class UrlShortenerView(viewsets.ViewSet):

    def get_serializer_context(self):
        return {'base_url': self.request.build_absolute_uri('/')[:-1]}

    def create(self, request, *args, **kwargs):
        serializer = UrlShortenerSerializer(data=request.data, context=self.get_serializer_context())
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None, *args, **kwargs):
        instance = get_object_or_404(UrlShortener, alias=pk)
        return redirect(instance.url)
