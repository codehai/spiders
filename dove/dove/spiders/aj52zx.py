import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from dove.items import Aj52zxItem
from bs4 import BeautifulSoup
import re  

add = 0
class Aj52zxSpider(CrawlSpider):
    name = 'aj52zx'
    allowed_domains = ['aj52zx.com']
    start_urls = ['http://aj52zx.com/racelist.aspx']

    rules = (
        Rule(LinkExtractor(allow=r'\?ssid=.*'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        global add
        item = Aj52zxItem()
        data = response.body
        soup = BeautifulSoup(data, "lxml")  
        item['title'] = soup.find('h1').text.replace("\n", " ").replace("\t", " ")
        item['url'] = response.url

        for script in soup.find_all("script"):
            script.decompose()

        item['content'] = soup.find('div', class_='wrap').text.replace("\n", " ").replace("\t", " ")
        item['date'] = re.findall(r'\d+/\d+/\d+ \d+:\d+:\d+', item['content'])[0]
        add += 1
        print("The total number:",add) 
        return item
