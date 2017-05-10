# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs
# class DovePipeline(object):
#     def process_item(self, item, spider):
#         return item


class IdeadotPipeline(object):  
    def __init__(self):  
        self.file = codecs.open('ideadot.json', 'w', encoding='utf-8')  
  
    def process_item(self, item, spider):
        self.file.write(json.dumps({
                "url":item["url"],
                "title":item["title"],
                "content":item["content"]
            }, indent=2, ensure_ascii=False))
        print(json.dumps({
                "url":item["url"],
                "title":item["title"],
                "content":item["content"]
            }, indent=2, ensure_ascii=False)) 
        return item  
  
    def spider_closed(self, spider):  
        self.file.close() 

class DovePipeline(object):  
    def __init__(self):  
        self.file = codecs.open('aj52zx.json', 'w', encoding='utf-8')  
  
    def process_item(self, item, spider):
        self.file.write(json.dumps({
                "url":item["url"],
                "date":item["date"],
                "title":item["title"],
                "content":item["content"]
            }, indent=2, ensure_ascii=False))
        print(json.dumps({
                "url":item["url"],
                "date":item["date"],
                "title":item["title"],
                # "content":item["content"]
            }, indent=2, ensure_ascii=False)) 
        return item  
  
    def spider_closed(self, spider):  
        self.file.close() 
