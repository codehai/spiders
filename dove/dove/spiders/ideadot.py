import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from dove.items import IdeadotItem
from bs4 import BeautifulSoup  

add = 0
class IdeadotSpider(CrawlSpider):
    name = 'ideadot'
    allowed_domains = ['ideadot.cn']
    start_urls = ['http://ideadot.cn/']

    rules = (
        Rule(LinkExtractor(allow=r'/\d+/\d+/\d+/.*'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        global add
        item = IdeadotItem()
        data = response.body
        soup = BeautifulSoup(data, "lxml")  
        item['title'] = soup.find('h1', class_="article-title").a.text
        item['url'] = response.url

        for script in soup.find_all("script"):
            script.decompose()

        item['content'] = soup.body.text.replace("\n", " ").replace("\t", " ")
        add += 1
        print("The total number:",add) 
        return item
