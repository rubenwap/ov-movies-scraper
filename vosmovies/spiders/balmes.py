# -*- coding: utf-8 -*-
import scrapy


class BalmesSpider(scrapy.Spider):
    name = 'balmes'
    allowed_domains = ['grupobalana.com']
    start_urls = ['http://grupobalana.com/']

    def parse(self, response):
        pass
