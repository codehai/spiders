# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field

class DoveItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class IdeadotItem(scrapy.Item):
    url = Field()
    title = Field()
    content = Field()


class Aj52zxItem(scrapy.Item):
    url = Field()
    title = Field()
    content = Field()
    date = Field()
