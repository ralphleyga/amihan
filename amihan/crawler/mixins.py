import re
import requests
from bs4 import BeautifulSoup


class WebCrawler(object):
    url = '' #Url to scrape

    def get_body(self):
        """Html page code
        """
        page = requests.get(self.url)
        soup = BeautifulSoup(page.content, 'html.parser')
        return soup

    def get_section(self, soup, id='', class_=''):
        """Get text in id or class section
        """
        if id:
            return str(soup.find(id=id))
        else:
            elems = soup.find_all(class_=class_)
            return ''.join(elem.text for elem in elems)

    def is_text_exist(self, text, content):
        """return true if text is found
        """
        if re.search(text, content, re.IGNORECASE):
            return True
        return False
