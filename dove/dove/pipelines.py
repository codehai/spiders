# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs
import time
import os
from pybloom import BloomFilter

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
        self.file = codecs.open(time.strftime('%Y-%m-%d %X',time.localtime()).replace(':','-')+".json", 'w', encoding='utf-8')  
  
    def open_spider(self, spider):

        isexists =os.path.exists('bloomfilter')

        if isexists == True:
            file = open('bloomfilter', 'rb')
            self.bf = BloomFilter.fromfile(file)
            file.close()
        else:
            self.bf = BloomFilter(capacity=10000000)

    def process_item(self, item, spider):
        flag = self.bf.add(item["url"])
        if flag == False:
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
  
    def close_spider(self, spider):  
        self.file.close()
        file = open('bloomfilter', 'wb')
        self.bf.tofile(file)
        file.close() 
