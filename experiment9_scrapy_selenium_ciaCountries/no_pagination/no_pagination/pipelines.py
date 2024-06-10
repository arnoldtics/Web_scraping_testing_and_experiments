# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import os
from urllib.parse import urlparse
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request

class CustomImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield Request(image_url, meta={'item': item})

    def file_path(self, request, response=None, info=None):
        item = request.meta['item']
        image_name = 'flag_' + item['name'][0]  
        return f'{image_name}.jpg'  
    
    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]  
        if image_paths:
            item['images'] = 'Downloaded'  
            item['image_name'] = image_paths[0]
        else:
            item['images'] = 'No downloaded'  
            item['image_name'] = None  
        return item


