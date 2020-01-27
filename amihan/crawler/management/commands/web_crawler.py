from django.core.management.base import BaseCommand, CommandError

from crawler.mixins import WebCrawler
from crawler.models import Crawler, CrawlerLog


class Command(BaseCommand, WebCrawler):

    def handle(self, *args, **options):
        print('start crawler')
        crawlers = Crawler.objects.all()

        for crawler in crawlers:
            log_crawler = False
            self.url = crawler.url
            soup = self.get_body()
            print(f'Parsing:{crawler.name}')

            if crawler.selector == 'id':
                result = self.get_section(soup, id=crawler.selector_label)
            else:
                result = self.get_section(soup, class_=crawler.selector_label)

            is_exist = self.is_text_exist(crawler.search_text, result)

            if crawler.notify_when == 1 and is_exist:
                print(f'"{crawler.search_text}" is found.')
                log_crawler = True
            elif crawler.notify_when == 2 and is_exist is False:
                print(f'"{crawler.search_text}" is not found.')
                log_crawler = True

            if log_crawler is True:
                CrawlerLog.objects.create(crawler=crawler)
            print('----------------------------------------')