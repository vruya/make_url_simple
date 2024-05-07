import random
import string

from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.db import models


def generate_alias(num=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(num))


class UrlShortener(models.Model):
    url = models.TextField()
    alias = models.CharField(max_length=15, unique=True, blank=True, default=generate_alias)

    def clean(self):
        validator = URLValidator()
        try:
            validator(self.url)
        except ValidationError:
            raise ValidationError("Invalid URL")

    def __str__(self):
        return self.url
