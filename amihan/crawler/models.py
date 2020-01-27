from django.db import models


SELECTOR = (
        ('id', 'ID'),
        ('class', 'Class'),
    )

NOTIFY_WHEN = (
    (1, 'If text found'),
    (2, 'If text not found'),
)


class Crawler(models.Model):

    email = models.EmailField()
    key = models.CharField(max_length=255)
    url = models.TextField()
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    selector = models.CharField(max_length=255, choices=SELECTOR)
    selector_label = models.CharField(max_length=500)
    search_text = models.CharField(max_length=500)
    notify_when = models.IntegerField(choices=NOTIFY_WHEN)

    def __str__(self):
        return self.name


class CrawlerLog(models.Model):

    crawler = models.ForeignKey(Crawler, related_name='crawler_logs', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.crawler.name