# -*- coding: utf-8 -*-
import scrapy
import json
from weibo.items import WeiboItem


class EarthquakeSpider(scrapy.Spider):
    name = 'earthquake'
    allowed_domains = ['m.weibo.cn']
    start_urls = [
        'https://m.weibo.cn/api/container/getIndex?uid=1904228041&luicode=10000011&lfid=100103type%3D3%26q%3D%E5%9C%B0%E9%9C%87%E9%80%9F%E6%8A%A5%26t%3D0&type=uid&value=1904228041&containerid=1076031904228041&page=' +
        str(i) for i in range(1, 10)
    ]

    def parse(self, response):
        js = json.loads(response.text)
        weibo_items = js.get('data').get('cards')
        for weibo_item in weibo_items:
            item = WeiboItem()
            item['time'] = weibo_item.get('mblog').get('created_at')
            item['txt'] = weibo_item.get('mblog').get('text')
            yield item
