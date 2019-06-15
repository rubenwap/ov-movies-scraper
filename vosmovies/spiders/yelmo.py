# -*- coding: utf-8 -*-
import scrapy


class YelmoSpider(scrapy.Spider):
    name = 'yelmo'
    allowed_domains = ['yelmocines.es']
    start_urls = ['http://yelmocines.es/']

    def parse(self, response):
        pass
