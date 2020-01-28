from rest_framework import serializers

from .models import Crawler, CrawlerLog


class CrawlerLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrawlerLog
        fields = '__all__'


class CrawlerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crawler
        fields = '__all__'
