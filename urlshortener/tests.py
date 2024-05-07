from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import UrlShortener


class ShortenedUrlTests(APITestCase):
    def test_create_short_url_with_custom_alias(self):
        url = reverse('url-shortener-list')
        data = {'url': 'http://example.com', 'alias': 'custom123'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(UrlShortener.objects.count(), 1)
        self.assertEqual(response.data['alias'], 'custom123')
        self.assertIn('custom123', response.data['short_url'])

    def test_create_short_url_without_custom_alias(self):
        url = reverse('url-shortener-list')
        data = {'url': 'http://example.com'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(UrlShortener.objects.count(), 1)
        self.assertTrue(UrlShortener.objects.get().alias)

    def test_redirect_to_url(self):
        url = reverse('url-shortener-detail', kwargs={'pk': 'custom123'})
        UrlShortener.objects.create(url='http://example.com', alias='custom123')
        response = self.client.get(url)
        self.assertRedirects(response, 'http://example.com', fetch_redirect_response=False)

    def test_alias_not_found(self):
        url = reverse('url-shortener-detail', kwargs={'pk': 'nonexistent'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
