# -*- coding: utf-8 -*-
import scrapy


class EarthquakeSpider(scrapy.Spider):
    name = 'earthquake'
    allowed_domains = ['www.ceic.ac.cn']
    start_urls = ['http://www.ceic.ac.cn/']

    def parse(self, response):
        pass
