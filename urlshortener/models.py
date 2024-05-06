from django.db import models
import random
import string


def generate_short_id(num=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(num))


class UrlShortener(models.Model):
    original_url = models.URLField()
    alias = models.CharField(max_length=15, unique=True, blank=True, default=generate_short_id)

    def __str__(self):
        return self.original_url
