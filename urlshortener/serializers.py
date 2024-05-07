from rest_framework import serializers
from .models import UrlShortener


class UrlShortenerSerializer(serializers.ModelSerializer):
    alias = serializers.CharField(max_length=15, required=False)

    class Meta:
        model = UrlShortener
        fields = ('url', 'alias')

    def validate_alias(self, value):
        if value and UrlShortener.objects.filter(alias=value).exists():
            raise serializers.ValidationError(
                "This alias is already taken. "
                "Please choose a different one or leave it blank to generate it automatically."
            )
        return value

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['short_url'] = f'{self.context["base_url"]}/api/{instance.alias}/'
        return data
