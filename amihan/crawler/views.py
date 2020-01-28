from rest_framework import viewsets

from .serializers import CrawlerSerializer
from .models import Crawler, CrawlerLog


class CrawlerViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Crawler.objects.all()
    serializer_class = CrawlerSerializer
