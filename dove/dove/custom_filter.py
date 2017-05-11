from scrapy.dupefilters import RFPDupeFilter
import dove.global_var as global_var

class CustomFilter(RFPDupeFilter):
    """A dupe filter that considers specific ids in the url"""
    
    def request_seen(self, request):
        if request.url in global_var.BLOOM_FILTER:
            print(request.url,' is skip.')
            return True
