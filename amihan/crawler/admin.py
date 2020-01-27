from django.contrib import admin

from .models import Crawler, CrawlerLog

admin.site.register(Crawler)
admin.site.register(CrawlerLog)